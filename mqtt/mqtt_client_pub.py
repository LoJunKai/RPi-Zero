# Add import path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

from testing.config import *
from testing.util import Profiler

import argparse

p = Profiler()

print("starting MQTT... ", end="")

parser = argparse.ArgumentParser(description='Client process for MQTT')
parser.add_argument('--times', metavar='t', type=int,
                    help='times to send json payload')

args = parser.parse_args()

test1 = open(TEST_FILE1, "rb").read()

# Read the docs here: https://github.com/eclipse/paho.mqtt.python
count = 0

p.start_log()
while count < int(args.times):
    publish.single(TEST_TOPIC1, test1, hostname="localhost")
    count += 1
    print("{}: {}".format('Sent count: ', count))
p.end_log()

print("done")
