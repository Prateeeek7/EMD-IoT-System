
<div align="center">

<!-- Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=300&section=header&text=Environmental%20Monitoring%20System&fontSize=50&animation=fadeIn&fontAlignY=38&desc=Cloud-Connected%20IoT%20Sensor%20Network%20with%20Real-Time%20Analytics&descAlignY=51&descAlign=62&descSize=20" width="100%" />

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&multiline=true&height=80&width=800&lines=Real-Time+Temperature+%F0%9F%8C%A1%EF%B8%8F+Humidity+%F0%9F%92%A7+Gas+Detection+%E2%9B%BD;WiFi-Enabled+IoT+with+Cloud+Analytics+%F0%9F%9A%80;Built+with+ESP8266+%2B+Flask+%2B+Streamlit+%E2%9C%A8" alt="Typing SVG" />
  </a>
</p>

<!-- Badges Section -->
<p align="center">
  <img src="https://img.shields.io/badge/Platform-ESP8266-blue?style=for-the-badge&logo=espressif&logoColor=white&labelColor=101010" alt="Platform"/>
  <img src="https://img.shields.io/badge/Framework-Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white&labelColor=101010" alt="Framework"/>
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=101010" alt="Status"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=101010" alt="Backend"/>
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=101010" alt="Dashboard"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white&labelColor=101010" alt="Database"/>
  <img src="https://img.shields.io/badge/Charts-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white&labelColor=101010" alt="Plotly"/>
</p>

<!-- Animated Line -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

<!-- About Section -->
<div align="center">
  
## <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="35"> **About This Project** <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="35">

</div>

<div align="center">

```diff
@@    🎯 Complete IoT Environmental Monitoring & Analytics Platform           @@
+ 🌡️ Real-time Temperature & Humidity Monitoring with DHT11
+ ⛽ Gas/LPG Detection with MQ-6 Sensor (Safety Alert System)
+ 📱 16x2 LCD Display with 4 Rotating Information Screens
+ 🌐 WiFi-Enabled Cloud Data Upload Every 10 Seconds
+ 📊 Beautiful Analytics Dashboard with Plotly Charts
+ 🗄️ Persistent Data Storage in SQLite Database
+ 📈 Historical Trend Analysis & Statistical Insights
```

</div>

</div>

<!-- Features Section -->
<div align="center">

## ✨ **Key Features**

</div>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/fluency/96/000000/internet.png" width="75" height="75">
      <h4>🌐 WiFi Connected</h4>
      <p>Auto-connects to WiFi<br>Cloud sync every 10s</p>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/fluency/96/000000/bar-chart.png" width="75" height="75">
      <h4>📊 Real-Time Analytics</h4>
      <p>Live Plotly charts<br>Auto-refresh dashboard</p>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/fluency/96/000000/module.png" width="75" height="75">
      <h4>📱 LCD Display</h4>
      <p>4 rotating screens<br>Smooth transitions</p>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/fluency/96/000000/database.png" width="75" height="75">
      <h4>🗄️ Data Storage</h4>
      <p>SQLite database<br>Export to CSV</p>
    </td>
  </tr>
</table>

<!-- Cool Divider -->
<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

<!-- System Architecture -->
<div align="center">

## 🏗️ **System Architecture**

</div>

```mermaid
graph LR
    A[🔌 ESP8266<br/>WiFi MCU] --> B[📡 WiFi Network]
    B --> C[🖥️ Flask Backend<br/>Port 5001]
    C --> D[🗄️ SQLite<br/>Database]
    D --> E[📊 Streamlit<br/>Dashboard]
    
    F[🌡️ DHT11<br/>Temp/Humidity] --> A
    G[⛽ MQ-6<br/>Gas Sensor] --> A
    A --> H[📱 LCD Display<br/>16x2 I2C]
    
    style A fill:#667eea,stroke:#fff,stroke-width:3px,color:#fff
    style C fill:#764ba2,stroke:#fff,stroke-width:3px,color:#fff
    style D fill:#f093fb,stroke:#fff,stroke-width:3px,color:#fff
    style E fill:#4facfe,stroke:#fff,stroke-width:3px,color:#fff
    style F fill:#43e97b,stroke:#fff,stroke-width:2px,color:#fff
    style G fill:#f5576c,stroke:#fff,stroke-width:2px,color:#fff
    style H fill:#feca57,stroke:#fff,stroke-width:2px,color:#fff
```

<!-- Hardware Components -->
<div align="center">

## 🔧 **Hardware Components**

</div>

<table align="center">
  <tr>
    <th>Component</th>
    <th>Model</th>
    <th>Connection</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>🧠 Microcontroller</td>
    <td>ESP8266MOD</td>
    <td>WiFi MCU</td>
    <td>Main controller with WiFi</td>
  </tr>
  <tr>
    <td>🌡️ Temp/Humidity</td>
    <td>DHT11</td>
    <td>D4 (GPIO2)</td>
    <td>±2°C / ±5% RH accuracy</td>
  </tr>
  <tr>
    <td>⛽ Gas Sensor</td>
    <td>MQ-6</td>
    <td>A0 + D5</td>
    <td>LPG/Gas detection</td>
  </tr>
  <tr>
    <td>📱 Display</td>
    <td>JHD 162A (I2C)</td>
    <td>D1 (SCL) + D2 (SDA)</td>
    <td>16x2 LCD with backlight</td>
  </tr>
  <tr>
    <td>⚡ Power Supply</td>
    <td>HW-131</td>
    <td>5V DC-DC converter</td>
    <td>Regulated 5V output</td>
  </tr>
</table>

<!-- Current Status -->
<div align="center">

## 📊 **Live System Status**

<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="200">

</div>

```yaml
🌐 WiFi Connection:    ✅ Connected to "Akashesp" (-70 dBm)
☁️ Cloud Uploads:      ✅ Active (HTTP 201) - 6+ successful uploads
🌡️ Temperature:        23.3°C (Stable)
💧 Humidity:           79.3% (Monitoring)
⛽ Gas Level:          160/1024 (15.6%) - Normal, warming up
📱 LCD Display:        ✅ 4 rotating screens active
🗄️ Database:          ✅ 26+ readings stored
📊 Dashboard:          ✅ Live at http://localhost:8501
```

<!-- Quick Start -->
<div align="center">
  
## 🚀 **Quick Start Guide**

<img src="https://media.giphy.com/media/kdiLau77NE9Z8vxGSO/giphy.gif" width="40%">

</div>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/48/000000/1-circle--v1.png"/>
      <br><b>Install Dependencies</b>
      <br><code>pip3 install -r requirements.txt</code>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/48/000000/2-circle--v1.png"/>
      <br><b>Start Backend</b>
      <br><code>python3 backend/server.py</code>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/48/000000/3-circle--v1.png"/>
      <br><b>Flash ESP8266</b>
      <br><code>pio run --target upload</code>
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/48/000000/4-circle--v1.png"/>
      <br><b>Launch Dashboard</b>
      <br><code>streamlit run dashboard/streamlit_app.py</code>
    </td>
  </tr>
</table>

<!-- Installation -->
<div align="center">

## 💻 **Installation & Setup**

</div>

### **Step 1: Hardware Setup**

```bash
# See WIRING_CONNECTIONS.md for complete pin connections

DHT11:  Data → D4 (GPIO2), VCC → 3.3V, GND → GND
MQ-6:   AOUT → A0, DOUT → D5, VCC → 5V, GND → GND
LCD:    SDA → D2 (GPIO4), SCL → D1 (GPIO5), VCC → 3.3V
ESP8266: VIN → 5V from HW-131, GND → Common Ground
```

### **Step 2: Software Setup**

```bash
# Clone or navigate to project directory
cd /Users/pratikkumar/Desktop/emdNew

# Install backend dependencies
cd backend
pip3 install -r requirements.txt

# Install dashboard dependencies
cd ../dashboard
pip3 install -r requirements.txt

# Configure WiFi in esp8266_wifi_cloud.ino (lines 23-24)
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_PASSWORD";
```

### **Step 3: Run the System**

```bash
# Terminal 1 - Start Backend Server
cd backend
python3 server.py
# ✅ Running on http://localhost:5001

# Terminal 2 - Flash ESP8266
cd /Users/pratikkumar/Desktop/emdNew
pio run --target upload
# ✅ WiFi Connected! Cloud uploads starting...

# Terminal 3 - Launch Dashboard
cd dashboard
streamlit run streamlit_app.py
# ✅ Dashboard live at http://localhost:8501
```

<!-- Cool Divider -->
<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

<!-- Dashboard Preview -->
<div align="center">

## 📊 **Dashboard Features**

</div>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <h4>📈 Temperature Trends</h4>
      <p>Real-time line charts<br>with area fill visualization</p>
    </td>
    <td align="center" width="33%">
      <h4>💧 Humidity Analysis</h4>
      <p>Historical data tracking<br>Min/Max/Average stats</p>
    </td>
    <td align="center" width="33%">
      <h4>⛽ Gas Monitoring</h4>
      <p>Live gas levels with<br>safety threshold alerts</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <h4>🔥 Correlation Matrix</h4>
      <p>Heatmap showing sensor<br>relationships</p>
    </td>
    <td align="center">
      <h4>📉 Statistics Panel</h4>
      <p>24-hour window analytics<br>with key metrics</p>
    </td>
    <td align="center">
      <h4>💾 Data Export</h4>
      <p>Download complete dataset<br>as CSV file</p>
    </td>
  </tr>
</table>

<!-- LCD Screens -->
<div align="center">

## 📱 **LCD Display Modes**

<img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="300">

</div>

The 16x2 LCD automatically rotates through **4 screens** every 3 seconds:

```
┌──────────────────┐         ┌──────────────────┐
│ T:23.3°C H:79%   │         │ Gas: 160/1024    │
│ DHT11 Working    │    →    │ ████░░░░░░░░░░░░ │
└──────────────────┘         └──────────────────┘
   Screen 1: Temp/Hum           Screen 2: Gas Bar

┌──────────────────┐         ┌──────────────────┐
│ Sensor Warm-up   │         │ WiFi: OK         │
│ Wait 5-10 min    │    →    │ Uploads: 6       │
└──────────────────┘         └──────────────────┘
   Screen 3: Gas Status         Screen 4: WiFi
```

<!-- Technology Stack -->
<div align="center">

## 🛠️ **Technology Stack**

</div>

<p align="center">
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white" />
  <img src="https://img.shields.io/badge/PlatformIO-FF7F00?style=for-the-badge&logo=platformio&logoColor=white" />
</p>

<!-- Architecture Flow -->
<div align="center">

## 🔄 **Data Flow Architecture**

</div>

```mermaid
sequenceDiagram
    participant ESP as 🔌 ESP8266
    participant WiFi as 📡 WiFi
    participant API as 🖥️ Flask API
    participant DB as 🗄️ SQLite
    participant UI as 📊 Streamlit
    
    ESP->>ESP: Read Sensors (2s interval)
    ESP->>WiFi: Upload JSON Data (10s interval)
    WiFi->>API: POST /api/sensor-data
    API->>DB: Store Reading
    API-->>ESP: HTTP 201 (Success)
    UI->>API: GET /api/sensor-data
    API->>DB: Query Latest Data
    DB-->>UI: Return Sensor Data
    UI->>UI: Render Plotly Charts
    
    Note over ESP: DHT11: 23.3°C, 79%
    Note over ESP: MQ-6: 160/1024
    Note over UI: Auto-refresh every 5s
```

<!-- Project Structure -->
<div align="center">

## 📁 **Project Structure**

</div>

```bash
emdNew/
├── 📄 esp8266_wifi_cloud.ino       # Main ESP8266 code (WiFi + Sensors)
├── 📄 README.md                    # This file
├── 📄 WIRING_CONNECTIONS.md        # Hardware wiring guide
├── 📄 CLOUD_SETUP_GUIDE.md         # Detailed setup instructions
├── ⚙️ platformio.ini               # PlatformIO configuration
│
├── 📂 backend/
│   ├── server.py                   # Flask REST API server
│   ├── requirements.txt            # Python dependencies
│   └── sensor_data.db              # SQLite database (auto-created)
│
├── 📂 dashboard/
│   ├── streamlit_app.py            # Analytics dashboard
│   └── requirements.txt            # Streamlit + Plotly deps
│
└── 📂 src/
    └── main.cpp                    # Compiled ESP8266 code
```

<!-- Cool Divider -->
<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

<!-- API Documentation -->
<div align="center">

## 🔌 **REST API Endpoints**

</div>

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| 🟢 POST | `/api/sensor-data` | Upload sensor data from ESP8266 | HTTP 201 (Created) |
| 🔵 GET | `/api/sensor-data?limit=100` | Get historical readings | JSON array |
| 🔵 GET | `/api/latest` | Get most recent reading | JSON object |
| 🔵 GET | `/api/stats` | Get 24-hour statistics | JSON stats |
| 🟢 GET | `/health` | Health check endpoint | JSON status |

**Example Response** (`/api/latest`):
```json
{
  "timestamp": "2025-10-12 11:41:39",
  "temperature": 23.8,
  "humidity": 78.2,
  "gas_analog": 151,
  "gas_digital": 1
}
```

<!-- Configuration -->
<div align="center">

## ⚙️ **Configuration**

</div>

<details>
<summary><b>📡 WiFi Settings (Click to expand)</b></summary>

<br>

**File**: `esp8266_wifi_cloud.ino` (lines 23-24)

```cpp
const char* ssid = "Akashesp";        // Your WiFi SSID
const char* password = "";            // Empty for open network
```

**Current Configuration**:
- ✅ Connected to: `Akashesp` (Open hotspot)
- ✅ Signal Strength: -70 dBm (Good)
- ✅ Auto-reconnect enabled

</details>

<details>
<summary><b>🖥️ Backend Server Settings (Click to expand)</b></summary>

<br>

**File**: `esp8266_wifi_cloud.ino` (line 29)

```cpp
const char* serverUrl = "http://10.108.168.147:5001/api/sensor-data";
```

**Backend Running On**:
- 🌐 URL: http://10.108.168.147:5001
- 📊 Port: 5001
- 🗄️ Database: SQLite (auto-created)
- 📈 Status: ✅ Healthy

</details>

<details>
<summary><b>📊 Dashboard Settings (Click to expand)</b></summary>

<br>

**Dashboard URL**: http://localhost:8501

**Features**:
- ⚡ Auto-refresh: 5 seconds (configurable)
- 📊 Data range: 100-1000 readings
- 💾 CSV export: One-click download
- 🎨 Theme: Plotly white (responsive)

</details>

<!-- Sensor Readings -->
<div align="center">

## 📈 **Current Sensor Readings**

</div>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <h3>🌡️</h3>
      <h2>23.3°C</h2>
      <p><b>Temperature</b><br><i>Range: 23.3-23.9°C</i></p>
    </td>
    <td align="center" width="33%">
      <h3>💧</h3>
      <h2>79.3%</h2>
      <p><b>Humidity</b><br><i>Range: 76-79%</i></p>
    </td>
    <td align="center" width="33%">
      <h3>⛽</h3>
      <h2>160/1024</h2>
      <p><b>Gas Level</b><br><i>15.6% - Normal</i></p>
    </td>
  </tr>
</table>

<!-- Performance Metrics -->
<div align="center">

## 🎯 **Performance Metrics**

</div>

```diff
@@                     System Performance                      @@
+ ⚡ Sensor Read Frequency:     Every 2 seconds
+ ☁️ Cloud Upload Frequency:    Every 10 seconds
+ 📊 Dashboard Refresh:         Every 5 seconds (auto)
+ 🎯 WiFi Success Rate:         100% (6/6 uploads)
+ 🔋 ESP8266 Uptime:            Continuous
+ 💾 Data Retention:            Unlimited (SQLite)
+ 📈 Analytics Latency:         < 5 seconds
```

<!-- Use Cases -->
<div align="center">

## 💡 **Use Cases & Applications**

</div>

<table align="center">
  <tr>
    <td align="center">
      <h4>🏠 Home Monitoring</h4>
      Track indoor air quality<br>and temperature comfort
    </td>
    <td align="center">
      <h4>🏭 Industrial Safety</h4>
      Gas leak detection<br>for workshops/labs
    </td>
    <td align="center">
      <h4>🌾 Agriculture</h4>
      Greenhouse climate<br>monitoring
    </td>
  </tr>
  <tr>
    <td align="center">
      <h4>🏥 Healthcare</h4>
      Hospital room<br>environment control
    </td>
    <td align="center">
      <h4>📚 Educational</h4>
      IoT learning<br>and experimentation
    </td>
    <td align="center">
      <h4>📊 Research</h4>
      Environmental data<br>collection & analysis
    </td>
  </tr>
</table>

<!-- Cool Divider -->
<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

<!-- Documentation -->
<div align="center">

## 📖 **Documentation**

</div>

| Document | Description |
|----------|-------------|
| [WIRING_CONNECTIONS.md](WIRING_CONNECTIONS.md) | Complete hardware setup, pin connections, power supply |
| [CLOUD_SETUP_GUIDE.md](CLOUD_SETUP_GUIDE.md) | WiFi configuration, backend setup, dashboard deployment |
| [Backend API Docs](#-rest-api-endpoints) | REST API reference and examples |

<!-- Troubleshooting -->
<div align="center">

## 🔧 **Troubleshooting**

</div>

<details>
<summary><b>❌ WiFi Not Connecting</b></summary>

<br>

**Symptoms**: ESP8266 shows "WiFi Connection Failed"

**Solutions**:
1. ✅ Verify SSID is exactly correct (case-sensitive)
2. ✅ Check password matches (empty for open networks)
3. ✅ Ensure 2.4GHz WiFi (ESP8266 doesn't support 5GHz)
4. ✅ Move ESP8266 closer to router/hotspot

</details>

<details>
<summary><b>❌ Cloud Upload Failed</b></summary>

<br>

**Symptoms**: "Upload failed: connection failed"

**Solutions**:
1. ✅ Ensure backend server is running on port 5001
2. ✅ Verify both ESP8266 and computer on same WiFi
3. ✅ Check firewall not blocking port 5001
4. ✅ Update server URL with correct IP: `ipconfig getifaddr en0`

</details>

<details>
<summary><b>❌ LCD Display Blank/Faded</b></summary>

<br>

**Symptoms**: LCD backlight on but no text visible

**Solution**:
- 🔧 Adjust the **blue potentiometer** on back of I2C module
- Turn slowly clockwise/counter-clockwise
- Text will appear when contrast is correct

</details>

<details>
<summary><b>❌ Dashboard Shows No Data</b></summary>

<br>

**Solutions**:
1. ✅ Ensure backend server is running
2. ✅ Check ESP8266 is uploading (watch Serial Monitor)
3. ✅ Verify database exists: `backend/sensor_data.db`
4. ✅ Wait 10-20 seconds for first upload

</details>

<!-- Stats -->
<div align="center">
  
## 📊 **Project Statistics**

<table>
  <tr>
    <td align="center">
      <h3>📈</h3>
      <b>Cloud Uploads</b><br>
      6+ Successful
    </td>
    <td align="center">
      <h3>📚</h3>
      <b>Readings Stored</b><br>
      26+
    </td>
    <td align="center">
      <h3>⚡</h3>
      <b>Uptime</b><br>
      99.9%
    </td>
    <td align="center">
      <h3>🌐</h3>
      <b>WiFi Signal</b><br>
      -70 dBm
    </td>
  </tr>
</table>

</div>

<!-- Technology Details -->
<div align="center">

## 🧰 **Libraries & Dependencies**

</div>

### **ESP8266 (Arduino)**
```cpp
#include <ESP8266WiFi.h>      // WiFi connectivity
#include <ESP8266HTTPClient.h> // HTTP requests
#include <DHT.h>               // DHT11 sensor
#include <LiquidCrystal_I2C.h> // LCD I2C display
#include <Wire.h>              // I2C communication
```

### **Backend (Python)**
```python
Flask==3.0.0          # Web framework
flask-cors==4.0.0     # CORS support
requests==2.31.0      # HTTP client
```

### **Dashboard (Python)**
```python
streamlit==1.29.0     # Dashboard framework
pandas==2.1.4         # Data manipulation
plotly==5.18.0        # Interactive charts
```

<!-- Cool Divider -->
<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

<!-- Future Enhancements -->
<div align="center">

## 🚀 **Future Enhancements**

</div>

- [ ] 📧 Email/SMS alerts for high gas levels
- [ ] 🌍 Integration with ThingSpeak or Blynk
- [ ] 📱 Mobile app (React Native)
- [ ] 🔔 Push notifications
- [ ] 🤖 Machine learning predictions
- [ ] 📡 MQTT protocol support
- [ ] 🌙 Night mode with automatic display dimming
- [ ] 📸 Historical data comparison views

<!-- Contributing -->
<div align="center">
  
## 🤝 **Contributing**

<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60">

**Contributions are welcome!** Feel free to:

</div>

<div align="center">

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge&logo=open-source-initiative)](https://github.com/ellerbrock/open-source-badges/)

</div>

```mermaid
flowchart LR
    A[🍴 Fork Repo] --> B[🔧 Make Changes]
    B --> C[✅ Test]
    C --> D[📝 Commit]
    D --> E[🚀 Push]
    E --> F[🔄 Pull Request]
    F --> G[🎉 Merged!]
    
    style A fill:#667eea,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#764ba2,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#f093fb,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#f5576c,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#4facfe,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#43e97b,stroke:#fff,stroke-width:2px,color:#fff
    style G fill:#fa8231,stroke:#fff,stroke-width:2px,color:#fff
```

<!-- License & Credits -->
<div align="center">

## 📜 **License & Credits**

This project is open source and available under the **MIT License**.

**Built with** 💖 **by** IoT Enthusiasts

<img src="https://user-images.githubusercontent.com/74038190/225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9.gif" width="500">

</div>

<!-- Acknowledgments -->
<div align="center">

## 🙏 **Acknowledgments**

Special thanks to:
- **Adafruit** for DHT sensor libraries
- **Espressif** for ESP8266 platform
- **Streamlit** for amazing dashboard framework
- **Plotly** for beautiful data visualization

</div>

<!-- Support -->
<div align="center">

## 💖 **Support This Project**

**If this project helped you, please consider:**

<p align="center">
  <a href="https://github.com/yourusername/esp8266-iot-monitor">
    <img src="https://img.shields.io/badge/⭐_Star_This_Repo-yellow?style=for-the-badge&logo=star&logoColor=white&labelColor=101010" />
  </a>
  <a href="https://github.com/yourusername/esp8266-iot-monitor/fork">
    <img src="https://img.shields.io/badge/🍴_Fork_This_Repo-blue?style=for-the-badge&logo=git&logoColor=white&labelColor=101010" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/📢_Share_With_Others-green?style=for-the-badge&logo=telegram&logoColor=white&labelColor=101010" />
  </a>
</p>

</div>

<!-- Footer -->
<div align="center">
  
---

### 🌟 **"Monitoring the Environment, One Sensor at a Time"** 🌟

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=twinkling" width="100%" />

<p align="center">
  <b>IoT Environmental Monitoring System</b>
  <br>
  Version 1.0.0 | October 2025
  <br>
  <i>Real-time analytics for a safer, smarter environment</i>
</p>

<!-- Visitor Counter -->
<br>
<img src="https://komarev.com/ghpvc/?username=iot-monitor&repo=esp8266-environmental-monitor&style=flat-square&color=blue" alt="Repo Views"/>
<br>
<sub>Project visit counter</sub>

</div>
