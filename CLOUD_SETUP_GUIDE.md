# 🌐 ESP8266 IoT Cloud Setup Guide

Complete guide to set up WiFi, cloud backend, and analytics dashboard for your ESP8266 sensor system.

---

## 📋 **System Architecture**

```
ESP8266 (Sensors) → WiFi → Backend Server → SQLite Database → Streamlit Dashboard
     ↓                                                              ↓
  LCD Display                                              Plotly Charts & Analytics
```

---

## 🚀 **Quick Start (3 Steps)**

### **Step 1: Start Backend Server** (Terminal 1)

```bash
cd /Users/pratikkumar/Desktop/emdNew/backend
pip3 install -r requirements.txt
python3 server.py
```

**Expected output:**
```
✓ Database initialized
ESP8266 IoT Backend Server
Server starting on http://0.0.0.0:5000
```

---

### **Step 2: Flash WiFi Code to ESP8266**

The code already has your WiFi credentials:
- **SSID**: akashesp
- **Password**: 0987654321
- **Server URL**: http://172.17.107.238:5000

```bash
cd /Users/pratikkumar/Desktop/emdNew
cp esp8266_wifi_cloud.ino src/main.cpp
pio run --target upload
```

**Wait for:** "WiFi Connected!" message on LCD and Serial Monitor

---

### **Step 3: Open Dashboard** (Terminal 2)

```bash
cd /Users/pratikkumar/Desktop/emdNew/dashboard
pip3 install -r requirements.txt
streamlit run streamlit_app.py
```

**Dashboard will open in your browser automatically!**

---

## 📊 **Dashboard Features**

### **Real-time Monitoring:**
- 🌡️ **Temperature** - Live readings with trend graphs
- 💧 **Humidity** - Historical data and averages
- ⛽ **Gas Levels** - Analog values with safety thresholds
- 🕐 **Last Update** - Time since last sensor reading

### **Analytics:**
- **Line Charts** - Temperature and humidity trends over time
- **Area Charts** - Gas level monitoring with threshold lines
- **Correlation Heatmap** - Relationships between sensors
- **Statistics** - Min, max, average values (24-hour window)
- **Data Export** - Download CSV for external analysis

### **Controls:**
- ✅ Auto-refresh (2-60 seconds)
- 📊 Data range selector (100-1000 readings)
- 🗑️ Clear database option
- 💾 Export data as CSV

---

## 🔧 **Detailed Setup Instructions**

### **Prerequisites:**

```bash
# Install Python dependencies
pip3 install flask flask-cors streamlit pandas plotly requests
```

---

### **Backend Server Setup:**

#### **File Structure:**
```
backend/
├── server.py           # Flask API server
├── requirements.txt    # Python dependencies
└── sensor_data.db      # SQLite database (auto-created)
```

#### **Start Backend:**

```bash
cd backend
python3 server.py
```

**API Endpoints:**
- `POST /api/sensor-data` - Receive data from ESP8266
- `GET /api/sensor-data?limit=100` - Get historical data
- `GET /api/latest` - Get latest reading
- `GET /api/stats` - Get statistics
- `GET /health` - Health check

**Test backend:**
```bash
curl http://localhost:5000/health
```

---

### **ESP8266 WiFi Configuration:**

#### **1. Update WiFi Credentials** (if needed)

Edit `esp8266_wifi_cloud.ino` lines 23-24:
```cpp
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
```

**Current settings:**
- SSID: `akashesp`
- Password: `0987654321`

#### **2. Verify Server URL**

Line 29:
```cpp
const char* serverUrl = "http://172.17.107.238:5000/api/sensor-data";
```

**If your IP changed:**
```bash
ipconfig getifaddr en0  # Get your Mac's IP
```

#### **3. Flash to ESP8266:**

```bash
cp esp8266_wifi_cloud.ino src/main.cpp
pio run --target upload
```

#### **4. Monitor Connection:**

```bash
python3 simple_capture.py
```

**Look for:**
```
✓ WiFi Connected!
IP Address: 192.168.1.XXX
☁ Cloud Upload #1 - HTTP 201 ✓ SUCCESS
```

---

### **Dashboard Setup:**

#### **File Structure:**
```
dashboard/
├── streamlit_app.py    # Streamlit dashboard
└── requirements.txt    # Python dependencies
```

#### **Start Dashboard:**

```bash
cd dashboard
streamlit run streamlit_app.py
```

**Dashboard URL:** http://localhost:8501

---

## 📱 **ESP8266 LCD Display (4 Screens)**

The LCD now rotates through **4 screens** every 3 seconds:

### **Screen 1: Temperature & Humidity**
```
T:23.0°C H:80%
DHT11 Working
```

### **Screen 2: Gas Level + Bar**
```
Gas: 197/1024
███░░░░░░░░░░░░░
```

### **Screen 3: Gas Status**
```
Sensor Warm-up
Wait 5-10 min
```

### **Screen 4: WiFi & Cloud Status**
```
WiFi: OK
Uploads: 42
```

---

## 🌐 **Data Flow**

```
1. ESP8266 reads sensors every 2 seconds
2. ESP8266 uploads to cloud every 10 seconds
3. Backend stores data in SQLite
4. Dashboard auto-refreshes every 5 seconds
5. You see real-time charts and analytics!
```

---

## 🎯 **What You'll See**

### **In Serial Monitor:**
```
========================================
Sensor Readings:
----------------------------------------
DHT11: ✓ Working
  Temperature: 23.0 °C
  Humidity:    80.1 %

MQ-6 Gas Sensor:
  Analog:  197 / 1024 (19.2%)
  Digital: HIGH

WiFi: ✓ Connected (-45 dBm)
Cloud Uploads: 42
========================================

☁ Cloud Upload #42 - HTTP 201 ✓ SUCCESS
```

### **On LCD Display:**
- Rotating screens showing all sensor data
- WiFi status and upload count
- Real-time updates

### **On Streamlit Dashboard:**
- 📊 Beautiful Plotly charts
- 📈 Real-time temperature/humidity trends
- ⛽ Gas level monitoring with thresholds
- 📉 24-hour statistics
- 🔥 Correlation heatmap
- 💾 CSV export capability

---

## 🔧 **Troubleshooting**

### **WiFi Not Connecting:**
- ✓ Check SSID and password in code
- ✓ ESP8266 and computer on same WiFi network
- ✓ WiFi is 2.4GHz (ESP8266 doesn't support 5GHz)

### **Cloud Upload Failed:**
- ✓ Backend server running on port 5000
- ✓ Check IP address: `ipconfig getifaddr en0`
- ✓ Firewall not blocking port 5000
- ✓ ESP8266 and computer on same network

### **Dashboard Shows No Data:**
- ✓ Backend server running
- ✓ ESP8266 successfully uploading (check Serial Monitor)
- ✓ Database file exists: `backend/sensor_data.db`

---

## 📊 **Expected Dashboard Screenshots**

### **Metrics Cards:**
```
🌡️ Temperature    💧 Humidity      ⛽ Gas Level     🕐 Last Update
   23.0 °C           80.1 %         197/1024         5s ago
 +0.2°C from avg  +1.5% from avg    19.2%            Live
```

### **Charts:**
- **Temperature Over Time** - Smooth line chart with area fill
- **Humidity Over Time** - Trend visualization
- **Gas Sensor** - Real-time monitoring with threshold lines
- **Correlation Heatmap** - See relationships between sensors

---

## 💡 **Advanced Features**

### **Custom Time Ranges:**
Use the sidebar to select:
- Last 100 readings (~3 minutes)
- Last 500 readings (~15 minutes)
- Last 1000 readings (~30 minutes)
- All data (complete history)

### **Auto Refresh:**
- Enable/disable auto-refresh
- Adjust refresh interval (2-60 seconds)
- Dashboard updates automatically!

### **Data Export:**
- Download complete dataset as CSV
- Use in Excel, Pandas, or other analytics tools

---

## 🎨 **Streamlit vs React**

**I chose Streamlit because:**
- ✅ **Faster setup** - No build process, runs immediately
- ✅ **Built-in refresh** - Auto-updates with live data
- ✅ **Plotly integration** - Beautiful charts out of the box
- ✅ **Python-based** - Works seamlessly with Flask backend
- ✅ **Responsive design** - Looks great on all devices

**If you prefer React**, I can create a React dashboard too, but Streamlit is perfect for IoT analytics!

---

## 📦 **Complete File Structure**

```
emdNew/
├── esp8266_wifi_cloud.ino       # WiFi-enabled ESP8266 code
├── backend/
│   ├── server.py                # Flask API backend
│   ├── requirements.txt         # Backend dependencies
│   └── sensor_data.db           # SQLite database (auto-created)
├── dashboard/
│   ├── streamlit_app.py         # Streamlit analytics dashboard
│   └── requirements.txt         # Dashboard dependencies
└── CLOUD_SETUP_GUIDE.md         # This file
```

---

## 🚀 **Ready to Deploy!**

Run these commands in order:

```bash
# Terminal 1 - Start Backend
cd /Users/pratikkumar/Desktop/emdNew/backend
pip3 install -r requirements.txt
python3 server.py

# Terminal 2 - Flash ESP8266 (wait for Terminal 1 to start)
cd /Users/pratikkumar/Desktop/emdNew
cp esp8266_wifi_cloud.ino src/main.cpp
pio run --target upload

# Terminal 3 - Start Dashboard (wait for data to arrive)
cd /Users/pratikkumar/Desktop/emdNew/dashboard
pip3 install -r requirements.txt
streamlit run streamlit_app.py
```

**Your IoT cloud analytics system will be live!** 🎉

---

## 📞 **Support**

- **Backend not receiving data?** Check firewall and IP address
- **Dashboard blank?** Wait for ESP8266 to upload first data
- **WiFi issues?** Ensure 2.4GHz network, check credentials

**Your sensor data will be beautifully visualized with real-time analytics!** 📊✨

