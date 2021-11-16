# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

from config import *

print("testing 1:")

with open(TEST_FILE1) as test1:
    publish.single(TEST_TOPIC1, test1.readline(), hostname=MQTT_BROKER_IP)

print("Done")
