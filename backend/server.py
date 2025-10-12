"""
Flask Backend Server for ESP8266 IoT Sensor Data
Receives sensor data via HTTP POST and stores in SQLite database
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import sqlite3
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Database configuration
DB_PATH = 'sensor_data.db'

def init_database():
    """Initialize SQLite database with sensor data table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            device_id TEXT,
            temperature REAL,
            humidity REAL,
            gas_analog INTEGER,
            gas_digital INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✓ Database initialized")

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    """Receive sensor data from ESP8266"""
    try:
        data = request.get_json()
        
        # Extract data
        device_id = data.get('device_id', 'unknown')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        gas_analog = data.get('gas_analog')
        gas_digital = data.get('gas_digital')
        
        # Store in database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sensor_readings 
            (device_id, temperature, humidity, gas_analog, gas_digital)
            VALUES (?, ?, ?, ?, ?)
        ''', (device_id, temperature, humidity, gas_analog, gas_digital))
        
        conn.commit()
        conn.close()
        
        print(f"✓ Data received: T={temperature}°C, H={humidity}%, Gas={gas_analog}")
        
        return jsonify({
            'status': 'success',
            'message': 'Data stored successfully'
        }), 201
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    """Get sensor data for dashboard"""
    try:
        limit = request.args.get('limit', 100, type=int)
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, timestamp, device_id, temperature, humidity, gas_analog, gas_digital
            FROM sensor_readings
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'timestamp': row[1],
                'device_id': row[2],
                'temperature': row[3],
                'humidity': row[4],
                'gas_analog': row[5],
                'gas_digital': row[6]
            })
        
        return jsonify(data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/latest', methods=['GET'])
def get_latest():
    """Get latest sensor reading"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT timestamp, temperature, humidity, gas_analog, gas_digital
            FROM sensor_readings
            ORDER BY timestamp DESC
            LIMIT 1
        ''')
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return jsonify({
                'timestamp': row[0],
                'temperature': row[1],
                'humidity': row[2],
                'gas_analog': row[3],
                'gas_digital': row[4]
            }), 200
        else:
            return jsonify({'message': 'No data available'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics for dashboard"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get latest 24 hours of data
        cursor.execute('''
            SELECT 
                COUNT(*) as total_readings,
                AVG(temperature) as avg_temp,
                MIN(temperature) as min_temp,
                MAX(temperature) as max_temp,
                AVG(humidity) as avg_humidity,
                MIN(humidity) as min_humidity,
                MAX(humidity) as max_humidity,
                AVG(gas_analog) as avg_gas,
                MAX(gas_analog) as max_gas
            FROM sensor_readings
            WHERE timestamp >= datetime('now', '-24 hours')
        ''')
        
        row = cursor.fetchone()
        conn.close()
        
        return jsonify({
            'total_readings': row[0],
            'temperature': {
                'average': round(row[1], 1) if row[1] else 0,
                'min': round(row[2], 1) if row[2] else 0,
                'max': round(row[3], 1) if row[3] else 0
            },
            'humidity': {
                'average': round(row[4], 1) if row[4] else 0,
                'min': round(row[5], 1) if row[5] else 0,
                'max': round(row[6], 1) if row[6] else 0
            },
            'gas': {
                'average': round(row[7], 1) if row[7] else 0,
                'max': round(row[8], 1) if row[8] else 0
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'ESP8266 IoT Backend',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    init_database()
    
    print("\n" + "=" * 50)
    print("ESP8266 IoT Backend Server")
    print("=" * 50)
    print("Server starting on http://0.0.0.0:5001")
    print("API Endpoints:")
    print("  POST /api/sensor-data  - Receive sensor data")
    print("  GET  /api/sensor-data  - Get historical data")
    print("  GET  /api/latest       - Get latest reading")
    print("  GET  /api/stats        - Get statistics")
    print("  GET  /health           - Health check")
    print("=" * 50 + "\n")
    
    app.run(host='0.0.0.0', port=5001, debug=True)

