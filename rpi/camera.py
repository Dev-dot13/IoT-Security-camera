(Updated & working version)

```python
import paho.mqtt.client as mqtt
import cv2
from datetime import datetime
import time

BROKER = "192.168.1.5000"
TOPIC = "security/capture"

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("âŒ Failed to open camera.")
    exit()

def capture_image():
    for _ in range(5):
        camera.read()
        time.sleep(0.05)
    ret, frame = camera.read()
    if ret:
        filename = f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"âœ… Image captured: {filename}")
    else:
        print("âŒ Failed to capture image")

def on_message(client, userdata, message):
    msg = message.payload.decode()
    print(f"Received: {msg}")
    if msg.lower() in ["capture", "near"]:
        capture_image()

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883)
client.subscribe(TOPIC)

print("ðŸ“· Waiting for capture messages...")
client.loop_forever()
