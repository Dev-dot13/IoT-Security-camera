# IoT Security Camera System (ESP32 + Raspberry Pi 4)

This project creates a **Wi-Fi-based security camera system** where an **ESP32** detects nearby movement using an **HC-SR04 ultrasonic sensor** and notifies a **Raspberry Pi 4** via **MQTT**.  
The Raspberry Pi captures an image using a **USB webcam** whenever the ESP32 detects proximity.

---

## ðŸ§© Features

- ðŸ§  Object detection via HC-SR04 ultrasonic sensor  
- ðŸ“¡ Wireless communication over MQTT  
- ðŸ“· Automatic photo capture on detection  
- ðŸ’¾ Saved images timestamped on the Raspberry Pi  
- âš¡ Lightweight and runs in real-time

---

## ðŸ–¥ï¸ Hardware Used

| Component | Description |
|------------|--------------|
| Raspberry Pi 4 | Runs MQTT broker & camera capture script |
| ESP32 WROOM-32 | Sends detection messages |
| HC-SR04 | Ultrasonic distance sensor |
| Logitech USB Webcam | Captures images |
| Wi-Fi Network | Common connection between ESP32 & RPi |

---

## âš™ï¸ System Architecture

