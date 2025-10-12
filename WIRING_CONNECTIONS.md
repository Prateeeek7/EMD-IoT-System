# ESP8266 Sensor Project - Wiring Connections

## Components:
- ESP8266MOD (ESP-12E/F module)
- DHT22 (Temperature & Humidity Sensor)
- MQ-6 (Gas Sensor)
- JHD 162A LCD (16x2) with I2C adapter
- HW-131 (DC-DC Power Supply Module)

---

## Power Supply Setup (HW-131)

### HW-131 Connections:
- **IN+**: Connect to external power source (+) [7-28V DC recommended]
- **IN-**: Connect to external power source Ground (-)
- **OUT+**: Adjust to 5V output (use onboard potentiometer)
- **OUT-**: Ground output

**Note**: Adjust the output voltage to 5V using the potentiometer before connecting to components.

---

## ESP8266MOD Pin Connections

### ESP8266 Power:
- **VCC (3.3V)**: Connect to 3.3V (NOT 5V!) - Use a 3.3V voltage regulator from HW-131 5V output, or if ESP8266 is on a dev board, connect to its VIN if it has onboard regulator
- **GND**: Connect to common Ground (HW-131 OUT-)
- **CH_PD (EN)**: Connect to 3.3V (enable chip)
- **GPIO15**: Connect to GND (boot mode)
- **GPIO0**: Connect to 3.3V through 10KΩ resistor (normal mode)
- **GPIO2**: Connect to 3.3V through 10KΩ resistor

---

## Sensor and Display Connections

### 1. DHT22 Sensor
| DHT22 Pin | ESP8266 Pin | Notes |
|-----------|-------------|-------|
| VCC (+)   | 3.3V        | Can also use 5V from HW-131 |
| DATA      | GPIO4 (D2)  | Add 10KΩ pull-up resistor to VCC |
| NC        | -           | Not connected |
| GND (-)   | GND         | Common ground |

**Pull-up Resistor**: Connect 10KΩ resistor between DATA pin and VCC

---

### 2. MQ-6 Gas Sensor
| MQ-6 Pin  | Connection  | Notes |
|-----------|-------------|-------|
| VCC       | 5V (HW-131) | MQ-6 requires 5V |
| GND       | GND         | Common ground |
| AOUT      | A0 (ADC)    | ESP8266 analog input |
| DOUT      | -           | Optional digital output (not used) |

**Important**: MQ-6 needs 24-48 hours of burn-in time for accurate readings.

---

### 3. JHD 162A LCD with I2C Module
| I2C Module Pin | ESP8266 Pin | Notes |
|----------------|-------------|-------|
| VCC            | 5V (HW-131) | LCD requires 5V |
| GND            | GND         | Common ground |
| SDA            | GPIO4 (D2)  | I2C Data line |
| SCL            | GPIO5 (D1)  | I2C Clock line |

**Note**: If DHT22 DATA conflicts with I2C SDA (both on GPIO4), move DHT22 to GPIO14 (D5)

---

## Final Pin Assignment (User Configuration)

| Device      | Pin       | ESP8266 Pin | Pin Name | Notes |    
|-------------|-----------|-------------|----------|-------|
| DHT22       | VCC       | 3.3V        | -        | Power |
| DHT22       | GND       | GND         | -        | Ground |
| DHT22       | Data      | GPIO2       | D4       | 10kΩ pull-up to 3.3V |
| MQ-6        | VCC       | 5V (HW-131) | -        | Power (5V required) |
| MQ-6        | GND       | GND         | -        | Ground |
| MQ-6        | AOUT      | A0          | A0       | Analog input (0-1V) |
| LCD I2C     | VCC       | 3.3V        | -        | Power (or 5V if module supports) |
| LCD I2C     | GND       | GND         | -        | Ground |
| LCD I2C     | SDA       | GPIO4       | D2       | I2C Data line |
| LCD I2C     | SCL       | GPIO5       | D1       | I2C Clock line |
| ESP8266     | VIN       | 5V (HW-131) | -        | Power input (onboard regulator) |
| ESP8266     | GND       | GND         | -        | Common ground |

---

## Complete Wiring Diagram (Text Format)

```
HW-131 Power Supply:
   IN+ ----[External Power 9-12V DC]---- IN-
   |                                      |
   OUT+ (5V) ----[Distribution]         OUT- (GND)
                     |                     |
                     |                     |
        +------------+-----+               |
        |            |     |               |
   [ESP8266 VIN] [MQ-6] [LCD VCC]*        |
        |          VCC     |               |
        |                  |               |
    [3.3V Out]            |            [COMMON GND]
        |                  |               |
   +----+------+           |          ESP8266 GND
   |           |           |          MQ-6 GND
[DHT22 VCC] [LCD VCC]*     |          LCD GND
                           |          DHT22 GND

* LCD VCC can be 3.3V or 5V depending on module

ESP8266 Pin Connections:
   GPIO2  (D4) <----[10KΩ to 3.3V]---- DHT22 DATA
   GPIO4  (D2) <----------------------- LCD SDA
   GPIO5  (D1) <----------------------- LCD SCL
   A0      <--------------------------- MQ-6 AOUT
```

---

## Important Notes:

1. **ESP8266 Voltage**: ESP8266 operates at 3.3V. Never connect 5V directly to GPIO pins!

2. **Power Requirements**:
   - ESP8266: 3.3V, peak 300mA
   - DHT22: 3.3V-5V, max 2.5mA
   - MQ-6: 5V, 150mA (heating element)
   - LCD: 5V, ~20-80mA

3. **I2C Address**: Default I2C LCD address is usually 0x27 or 0x3F

4. **Common Ground**: All grounds must be connected together

5. **USB Programming**: When programming via USB, the USB-to-Serial adapter provides power. After programming, use HW-131 for standalone operation.

---

## Testing Sequence:

1. Power on and verify 5V output from HW-131
2. Verify 3.3V at ESP8266 VCC
3. Upload test code via USB
4. Check serial monitor for sensor readings
5. Verify LCD display

