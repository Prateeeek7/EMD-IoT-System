"""
Streamlit Dashboard for ESP8266 IoT Sensor Monitoring
Real-time analytics with Plotly charts
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import requests
import sqlite3
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="ESP8266 Sensor Monitor",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Database path
DB_PATH = '../backend/sensor_data.db'

@st.cache_data(ttl=2)
def load_data(limit=500):
    """Load sensor data from database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        query = f"""
            SELECT timestamp, temperature, humidity, gas_analog, gas_digital
            FROM sensor_readings
            ORDER BY timestamp DESC
            LIMIT {limit}
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        
        return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

def get_latest_reading():
    """Get the most recent sensor reading"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT timestamp, temperature, humidity, gas_analog, gas_digital
            FROM sensor_readings
            ORDER BY timestamp DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'timestamp': row[0],
                'temperature': row[1],
                'humidity': row[2],
                'gas_analog': row[3],
                'gas_digital': row[4]
            }
        return None
    except:
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🌡️ ESP8266 IoT Sensor Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        auto_refresh = st.checkbox("Auto Refresh", value=True)
        refresh_interval = st.slider("Refresh Interval (seconds)", 2, 60, 5)
        
        data_range = st.selectbox(
            "Data Range",
            ["Last 100 readings", "Last 500 readings", "Last 1000 readings", "All data"]
        )
        
        # Map selection to limit
        limit_map = {
            "Last 100 readings": 100,
            "Last 500 readings": 500,
            "Last 1000 readings": 1000,
            "All data": 10000
        }
        data_limit = limit_map[data_range]
        
        st.markdown("---")
        st.markdown("### 📊 Dashboard Info")
        st.info("Real-time monitoring of temperature, humidity, and gas levels from your ESP8266 sensor system.")
        
        if st.button("🗑️ Clear All Data"):
            if st.checkbox("Confirm deletion"):
                try:
                    conn = sqlite3.connect(DB_PATH)
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM sensor_readings")
                    conn.commit()
                    conn.close()
                    st.success("All data cleared!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    # Load data
    df = load_data(data_limit)
    latest = get_latest_reading()
    
    if df.empty:
        st.warning("⚠️ No data available yet. Waiting for ESP8266 to send data...")
        st.info("Make sure:\n1. Backend server is running\n2. ESP8266 is connected to WiFi\n3. Server URL is correct in ESP8266 code")
        return
    
    # Current Status Cards
    st.markdown("### 📊 Current Readings")
    
    col1, col2, col3, col4 = st.columns(4)
    
    if latest:
        with col1:
            temp = latest['temperature']
            temp_delta = round(temp - df['temperature'].mean(), 1)
            st.metric(
                label="🌡️ Temperature",
                value=f"{temp:.1f} °C",
                delta=f"{temp_delta:+.1f}°C from avg"
            )
        
        with col2:
            hum = latest['humidity']
            hum_delta = round(hum - df['humidity'].mean(), 1)
            st.metric(
                label="💧 Humidity",
                value=f"{hum:.1f} %",
                delta=f"{hum_delta:+.1f}% from avg"
            )
        
        with col3:
            gas = latest['gas_analog']
            gas_percent = (gas / 1024) * 100
            st.metric(
                label="⛽ Gas Level",
                value=f"{gas} / 1024",
                delta=f"{gas_percent:.1f}%"
            )
        
        with col4:
            # Time since last update
            last_time = pd.to_datetime(latest['timestamp'])
            time_diff = (datetime.now() - last_time).total_seconds()
            st.metric(
                label="🕐 Last Update",
                value=f"{int(time_diff)}s ago",
                delta="Live" if time_diff < 30 else "Delayed"
            )
    
    # Statistics
    st.markdown("### 📈 Statistics (Last 24 Hours)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🌡️ Temperature**")
        st.write(f"Average: {df['temperature'].mean():.1f}°C")
        st.write(f"Min: {df['temperature'].min():.1f}°C")
        st.write(f"Max: {df['temperature'].max():.1f}°C")
    
    with col2:
        st.markdown("**💧 Humidity**")
        st.write(f"Average: {df['humidity'].mean():.1f}%")
        st.write(f"Min: {df['humidity'].min():.1f}%")
        st.write(f"Max: {df['humidity'].max():.1f}%")
    
    with col3:
        st.markdown("**⛽ Gas Sensor**")
        st.write(f"Average: {df['gas_analog'].mean():.0f} / 1024")
        st.write(f"Min: {df['gas_analog'].min()} / 1024")
        st.write(f"Max: {df['gas_analog'].max()} / 1024")
    
    st.markdown("---")
    
    # Charts
    st.markdown("### 📊 Sensor Trends")
    
    # Temperature & Humidity Chart
    fig1 = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Temperature Over Time', 'Humidity Over Time'),
        vertical_spacing=0.12
    )
    
    # Temperature trace
    fig1.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['temperature'],
            name='Temperature',
            line=dict(color='#ff6b6b', width=2),
            fill='tozeroy',
            fillcolor='rgba(255, 107, 107, 0.2)'
        ),
        row=1, col=1
    )
    
    # Humidity trace
    fig1.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['humidity'],
            name='Humidity',
            line=dict(color='#4ecdc4', width=2),
            fill='tozeroy',
            fillcolor='rgba(78, 205, 196, 0.2)'
        ),
        row=2, col=1
    )
    
    fig1.update_xaxes(title_text="Time", row=2, col=1)
    fig1.update_yaxes(title_text="°C", row=1, col=1)
    fig1.update_yaxes(title_text="%", row=2, col=1)
    
    fig1.update_layout(
        height=600,
        showlegend=True,
        hovermode='x unified',
        template='plotly_white'
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Gas Sensor Chart
    st.markdown("### ⛽ Gas Sensor Readings")
    
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['gas_analog'],
        name='Gas Level',
        line=dict(color='#95e1d3', width=3),
        fill='tozeroy',
        fillcolor='rgba(149, 225, 211, 0.3)'
    ))
    
    # Add threshold lines
    fig2.add_hline(y=100, line_dash="dash", line_color="green", 
                   annotation_text="Safe Threshold")
    fig2.add_hline(y=300, line_dash="dash", line_color="orange", 
                   annotation_text="Warning Threshold")
    fig2.add_hline(y=500, line_dash="dash", line_color="red", 
                   annotation_text="Danger Threshold")
    
    fig2.update_layout(
        title="Gas Sensor Analog Value (0-1024)",
        xaxis_title="Time",
        yaxis_title="Analog Value",
        height=400,
        template='plotly_white',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Correlation Heatmap
    st.markdown("### 🔥 Sensor Correlation Heatmap")
    
    corr_df = df[['temperature', 'humidity', 'gas_analog']].corr()
    
    fig3 = go.Figure(data=go.Heatmap(
        z=corr_df.values,
        x=['Temperature', 'Humidity', 'Gas Level'],
        y=['Temperature', 'Humidity', 'Gas Level'],
        colorscale='RdBu',
        zmid=0,
        text=corr_df.values,
        texttemplate='%{text:.2f}',
        textfont={"size": 14},
        colorbar=dict(title="Correlation")
    ))
    
    fig3.update_layout(
        title="Correlation Between Sensors",
        height=400,
        template='plotly_white'
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Recent Data Table
    with st.expander("📋 View Recent Data Table"):
        st.dataframe(
            df[['timestamp', 'temperature', 'humidity', 'gas_analog', 'gas_digital']].head(50),
            use_container_width=True
        )
    
    # Data export
    with st.expander("💾 Export Data"):
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    # Footer
    st.markdown("---")
    st.markdown(f"**Total Readings:** {len(df)} | **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Auto refresh
    if auto_refresh:
        time.sleep(refresh_interval)
        st.rerun()

if __name__ == "__main__":
    main()

