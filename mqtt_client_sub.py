import paho.mqtt.client as subscriber
import time

from config import *

def on_message(client, userdata, message):
    print(f"message: {message.payload}")
    print(f"topic: {message.topic}")
    print(f"qos: {message.qos}")
    print(f"retain flag: {message.retain}")

print("Creating Client")
client = subscriber.Client("sub1")
client.on_message = on_message

print(f"Connecting to {MQTT_BROKER_IP}")
client.connect("localhost")

#loop start
client.loop_forever()

print(f"Subscribing to {TEST_TOPIC1}")
client.subscribe(TEST_TOPIC1)

# time.sleep(10)

# client.loop_stop()