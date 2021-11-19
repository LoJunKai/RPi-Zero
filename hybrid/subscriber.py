import paho.mqtt.client as mqtt

from config import *

def on_connect(client, userdata, flags, rc):
    print(f"Subscribing to {TOPIC}")
    client.connected_flag = True
    client.subscribe(TOPIC)


def on_message(client, userdata, message):
    print(f"message: {message.payload}")
    print(f"topic: {message.topic}")
    print(f"qos: {message.qos}")
    print(f"retain flag: {message.retain}")


print("Creating Client")
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print(f"Connecting to localhost")
client.connect("localhost")

# loop start
client.loop_forever()
