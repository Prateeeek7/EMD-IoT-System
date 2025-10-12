/*
 * ESP8266 IoT Sensor Monitor with WiFi Cloud Integration
 * 
 * Sensors: DHT11 (Temp/Humidity), MQ-6 (Gas), LCD I2C (Display)
 * Features: WiFi connectivity, Cloud data upload, Local LCD display
 * 
 * Hardware:
 * - DHT11: Data → D4 (GPIO2), 8.2kΩ pull-up, VCC → 3.3V
 * - MQ-6:  AOUT → A0, DOUT → D5, VCC → 5V
 * - LCD:   SDA → D2 (GPIO4), SCL → D1 (GPIO5), VCC → 3.3V
 */

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// ========== WiFi CONFIGURATION ==========
// CHANGE THESE TO YOUR WiFi CREDENTIALS!
const char* ssid = "Akashesp";           // Your hotspot name
const char* password = "";                // Empty for open network (no password)

// ========== CLOUD SERVER CONFIGURATION ==========
// Your computer's IP address on Akashesp hotspot
// Current IP: 10.108.168.147
const char* serverUrl = "http://10.108.168.147:5001/api/sensor-data";

// ========== PIN DEFINITIONS ==========
#define DHT_PIN 2              // GPIO2 = D4
#define DHT_TYPE DHT11
#define MQ6_ANALOG A0
#define MQ6_DIGITAL 14         // GPIO14 = D5

// ========== LCD SETUP ==========
#define LCD_ADDRESS 0x27
LiquidCrystal_I2C lcd(LCD_ADDRESS, 16, 2);

// ========== SENSOR INITIALIZATION ==========
DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient wifiClient;

// ========== VARIABLES ==========
float temperature = 0.0;
float humidity = 0.0;
int gasAnalog = 0;
int gasDigital = 0;

unsigned long lastSensorRead = 0;
unsigned long lastCloudUpload = 0;
unsigned long lastDisplayUpdate = 0;

const unsigned long SENSOR_INTERVAL = 2000;    // Read sensors every 2 seconds
const unsigned long CLOUD_INTERVAL = 10000;    // Upload to cloud every 10 seconds
const unsigned long DISPLAY_INTERVAL = 3000;   // Change display every 3 seconds

int displayMode = 0;
bool wifiConnected = false;
int uploadCount = 0;

// Function declarations
void connectWiFi();
void readSensors();
void uploadToCloud();
void updateLCD();
void printSerialData();

void setup() {
  // ========== SERIAL MONITOR ==========
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n\n========================================");
  Serial.println("ESP8266 IoT Sensor Monitor with WiFi");
  Serial.println("========================================");
  
  // ========== SENSORS INITIALIZATION ==========
  Serial.println("Initializing sensors...");
  dht.begin();
  pinMode(MQ6_DIGITAL, INPUT);
  
  // ========== LCD INITIALIZATION ==========
  Wire.begin(4, 5);  // SDA, SCL
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("IoT Sensor");
  lcd.setCursor(0, 1);
  lcd.print("Connecting WiFi");
  
  Serial.println("✓ Sensors initialized");
  Serial.println("✓ LCD initialized");
  
  // ========== WiFi CONNECTION ==========
  connectWiFi();
  
  Serial.println("\n========================================");
  Serial.println("Setup Complete!");
  Serial.println("========================================\n");
  
  delay(2000);
}

void loop() {
  unsigned long currentMillis = millis();
  
  // Check WiFi connection
  if (WiFi.status() != WL_CONNECTED) {
    wifiConnected = false;
    connectWiFi();
  } else {
    wifiConnected = true;
  }
  
  // Read sensors
  if (currentMillis - lastSensorRead >= SENSOR_INTERVAL) {
    lastSensorRead = currentMillis;
    readSensors();
    printSerialData();
  }
  
  // Upload to cloud
  if (currentMillis - lastCloudUpload >= CLOUD_INTERVAL) {
    lastCloudUpload = currentMillis;
    if (wifiConnected) {
      uploadToCloud();
    }
  }
  
  // Update LCD display
  if (currentMillis - lastDisplayUpdate >= DISPLAY_INTERVAL) {
    lastDisplayUpdate = currentMillis;
    displayMode = (displayMode + 1) % 4;  // 4 screens
  }
  updateLCD();
  
  delay(100);
}

// ========== WiFi CONNECTION ==========
void connectWiFi() {
  Serial.println("\nConnecting to WiFi...");
  Serial.print("SSID: ");
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\n✓ WiFi Connected!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    Serial.print("Signal Strength: ");
    Serial.print(WiFi.RSSI());
    Serial.println(" dBm");
    
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("WiFi Connected!");
    lcd.setCursor(0, 1);
    lcd.print(WiFi.localIP());
    delay(2000);
    
    wifiConnected = true;
  } else {
    Serial.println("\n✗ WiFi Connection Failed!");
    Serial.println("Check SSID and password");
    
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("WiFi Failed!");
    lcd.setCursor(0, 1);
    lcd.print("Check settings");
    delay(2000);
    
    wifiConnected = false;
  }
}

// ========== READ SENSORS ==========
void readSensors() {
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();
  gasAnalog = analogRead(MQ6_ANALOG);
  gasDigital = digitalRead(MQ6_DIGITAL);
}

// ========== UPLOAD TO CLOUD ==========
void uploadToCloud() {
  if (!wifiConnected) return;
  
  HTTPClient http;
  
  // Create JSON payload
  String jsonData = "{";
  jsonData += "\"temperature\":" + String(temperature, 1) + ",";
  jsonData += "\"humidity\":" + String(humidity, 1) + ",";
  jsonData += "\"gas_analog\":" + String(gasAnalog) + ",";
  jsonData += "\"gas_digital\":" + String(gasDigital) + ",";
  jsonData += "\"timestamp\":" + String(millis()) + ",";
  jsonData += "\"device_id\":\"ESP8266_" + WiFi.macAddress() + "\"";
  jsonData += "}";
  
  http.begin(wifiClient, serverUrl);
  http.addHeader("Content-Type", "application/json");
  
  int httpCode = http.POST(jsonData);
  
  if (httpCode > 0) {
    uploadCount++;
    Serial.print("☁ Cloud Upload #");
    Serial.print(uploadCount);
    Serial.print(" - HTTP ");
    Serial.print(httpCode);
    
    if (httpCode == 200 || httpCode == 201) {
      Serial.println(" ✓ SUCCESS");
    } else {
      Serial.println(" - Response: " + http.getString());
    }
  } else {
    Serial.print("✗ Upload failed: ");
    Serial.println(http.errorToString(httpCode));
  }
  
  http.end();
}

// ========== PRINT SERIAL DATA ==========
void printSerialData() {
  Serial.println("========================================");
  Serial.println("Sensor Readings:");
  Serial.println("----------------------------------------");
  
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("DHT11: ✗ Failed to read");
  } else {
    Serial.println("DHT11: ✓ Working");
    Serial.print("  Temperature: ");
    Serial.print(temperature, 1);
    Serial.println(" °C");
    Serial.print("  Humidity:    ");
    Serial.print(humidity, 1);
    Serial.println(" %");
  }
  
  Serial.println("\nMQ-6 Gas Sensor:");
  Serial.print("  Analog:  ");
  Serial.print(gasAnalog);
  Serial.print(" / 1024 (");
  Serial.print((gasAnalog / 1024.0) * 100, 1);
  Serial.println("%)");
  Serial.print("  Digital: ");
  Serial.println(gasDigital == HIGH ? "HIGH" : "LOW");
  
  Serial.print("\nWiFi: ");
  Serial.print(wifiConnected ? "✓ Connected (" : "✗ Disconnected");
  if (wifiConnected) {
    Serial.print(WiFi.RSSI());
    Serial.println(" dBm)");
  } else {
    Serial.println();
  }
  Serial.print("Cloud Uploads: ");
  Serial.println(uploadCount);
  
  Serial.println("========================================\n");
}

// ========== UPDATE LCD DISPLAY ==========
void updateLCD() {
  switch (displayMode) {
    case 0:  // Temperature & Humidity
    {
      lcd.setCursor(0, 0);
      if (isnan(temperature)) {
        lcd.print("Temp: ERROR     ");
      } else {
        lcd.print("T:");
        lcd.print(temperature, 1);
        lcd.print((char)223);
        lcd.print("C H:");
        lcd.print(humidity, 0);
        lcd.print("%  ");
      }
      
      lcd.setCursor(0, 1);
      lcd.print("DHT11 Working   ");
      break;
    }
      
    case 1:  // Gas Level with Bar
    {
      lcd.setCursor(0, 0);
      lcd.print("Gas: ");
      if (gasAnalog < 10) lcd.print("  ");
      else if (gasAnalog < 100) lcd.print(" ");
      lcd.print(gasAnalog);
      lcd.print("/1024  ");
      
      lcd.setCursor(0, 1);
      int bars = map(gasAnalog, 0, 1024, 0, 16);
      for(int i = 0; i < 16; i++) {
        lcd.print(i < bars ? (char)255 : ' ');
      }
      break;
    }
      
    case 2:  // Gas Status
    {
      lcd.setCursor(0, 0);
      if (gasAnalog < 100) {
        lcd.print("Air: GOOD       ");
        lcd.setCursor(0, 1);
        lcd.print("Safe to breathe ");
      } else if (gasAnalog < 300) {
        lcd.print("Sensor Warm-up  ");
        lcd.setCursor(0, 1);
        lcd.print("Wait 5-10 min   ");
      } else {
        lcd.print("Gas ELEVATED!   ");
        lcd.setCursor(0, 1);
        lcd.print("Check area      ");
      }
      break;
    }
    
    case 3:  // WiFi & Cloud Status
    {
      lcd.setCursor(0, 0);
      if (wifiConnected) {
        lcd.print("WiFi: OK        ");
        lcd.setCursor(0, 1);
        lcd.print("Uploads: ");
        lcd.print(uploadCount);
        lcd.print("      ");
      } else {
        lcd.print("WiFi: OFFLINE   ");
        lcd.setCursor(0, 1);
        lcd.print("Reconnecting... ");
      }
      break;
    }
  }
}

