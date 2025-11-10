# IoT Security Camera System (ESP32 + Raspberry Pi 4)

This project creates a **Wi-Fi-based security camera system** where an **ESP32** detects nearby movement using an **HC-SR04 ultrasonic sensor** and notifies a **Raspberry Pi 4** via **MQTT**.  
The Raspberry Pi captures an image using a **USB webcam** whenever the ESP32 detects proximity.

---

## Features

- ðŸ§  Object detection via HC-SR04 ultrasonic sensor  
- ðŸ“¡ Wireless communication over MQTT  
- ðŸ“· Automatic photo capture on detection  
- ðŸ’¾ Saved images timestamped on the Raspberry Pi  
- âš¡ Lightweight and runs in real-time

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
   - Use **Sketch â†’ Include Library â†’ Manage Libraries...** and install:
     - **PubSubClient** by Nick Oâ€™Leary  
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
      iii) Distance readings and â€œcaptureâ€ publish events

## How it works

1. The HC-SR04 ultrasonic sensor measures distance continuously.
2. When an object is detected closer than the threshold (default: 50 cm), the ESP32 publishes the message "capture" to the MQTT topic security/capture.
3. The Raspberry Pi subscribes to security/capture; when it receives the message it captures a fresh image from the USB webcam and saves it with a timestamped filename.
