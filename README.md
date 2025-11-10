# IoT Security Camera System (ESP32 + Raspberry Pi 4)

This project creates a **Wi-Fi-based security camera system** where an **ESP32** detects nearby movement using an **HC-SR04 ultrasonic sensor** and notifies a **Raspberry Pi 4** via **MQTT**.  
The Raspberry Pi captures an image using a **USB webcam** whenever the ESP32 detects proximity.

---

## Features

- Object detection via HC-SR04 ultrasonic sensor  
- Wireless communication over MQTT  
- Automatic photo capture on detection  
- Saved images timestamped on the Raspberry Pi  
- Lightweight and runs in real-time

---

## Hardware Used

| Component | Description |
|------------|--------------|
| Raspberry Pi 4 | Runs MQTT broker & camera capture script |
| ESP32 WROOM-32 | Sends detection messages |
| HC-SR04 | Ultrasonic distance sensor |
| Logitech USB Webcam | Captures images |
| Wi-Fi Network | Common connection between ESP32 & RPi |

---

## System Architecture

    +-------------------+
    |   ESP32 + HC-SR04 |
    |                   |
    | Detects object     |
    | Publishes MQTT msg |
    +---------+----------+
              |
              | Wi-Fi (MQTT)
              v
    +---------+----------+
    |   Raspberry Pi 4   |
    | Runs Mosquitto     |
    | Subscribes to MQTT |
    | Captures image     |
    +--------------------+


---

## Setup Guide

### Raspberry Pi Setup

1. **Install Mosquitto MQTT Broker**
   ```bash
   sudo apt update
   sudo apt install mosquitto mosquitto-clients -y
   sudo systemctl enable mosquitto
   sudo systemctl start mosquitto

2. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/iot-security-camera.git
   cd iot-security-camera/rpi

3. **Create virtual environment & install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r ../requirements.txt

4. **Run the capture script**
   ```bash
   python3 camera2.py

5. **Check for saved images**
   Each image will be saved as:
    capture_YYYYMMDD_HHMMSS.jpg

## ESP32 Setup

1. **Open** `esp32/esp32_ultrasonic_mqtt.ino` in Arduino IDE.

2. **Install required libraries**
   - Use **Sketch Include Library Manage Libraries...** and install:
     - **PubSubClient** by Nick Leary  
     - **WiFi** (included with the ESP32 Arduino core)

3. **Edit Wi-Fi and broker settings** in the sketch:
   ```cpp
   const char* ssid = "YOUR_WIFI_NAME";
   const char* password = "YOUR_WIFI_PASSWORD";
   const char* mqtt_server = "192.168.1.5000"; // Your Raspberry Pi IP

4. **Upload** the sketch to your ESP32.
5. **Open Serial Monitor** at **115200 baud** to confirm:
   i) Wi-Fi connection (shows ESP32 local IP)
   ii) MQTT connection (shows successful connect or reconnect messages)
   iii) Distance readings and 'capture' publish events

## Example Outputs

1. **Raspberri Pi terminal**
   ```bash
   Waiting for capture messages...
   Received: capture
   Image captured: capture_20251110_172320.jpg
  
2. **ESP32 Serial Monitor (115200)**
   ```bash
   Connecting to YOUR_WIFI_NAME...
   Wifi connected! ESP32 IP: 192.168.1.5100
   Attempting MQTT connection... connected
   Distance: 34 cm
   Object detected -> Sending message
