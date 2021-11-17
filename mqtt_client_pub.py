# Add import path
import sys
from pathlib import Path
sys.path.insert(0, Path(__file__).parents[1])

# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

from config import *

print("testing 1... ", end="")

with open(TEST_FILE2, "rb") as test1:
    # Read the docs here: https://github.com/eclipse/paho.mqtt.python
    publish.single(TEST_TOPIC1, test1.read(), hostname="localhost")

print("done")
