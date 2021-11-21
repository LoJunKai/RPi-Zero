# Add import path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

# MQTT Publish Demo
# Publish two messages, to two different topics

import argparse

import paho.mqtt.publish as publish
from testing.config import *
from testing.util import Profiler

# from testing.config import *
from config import *
from util import *

p = Profiler()

print("starting MQTT... ", end="")

parser = argparse.ArgumentParser(description='Client process for MQTT')
parser.add_argument('-t', '--times', metavar='t', type=int, required=True,
                    help='times to send json payload')

args = parser.parse_args()


def run():
    test1 = open(TEST_FILE1, "rb").read()
    count = 0

    p.start_log()
    while count < args.times:
        # Read the docs here: https://github.com/eclipse/paho.mqtt.python
        publish.single(TEST_TOPIC1, test1, hostname="localhost")
        count += 1
        print("{}: {}".format('Sent count: ', count))
    p.end_log()

    print("done")
    

if __name__ == "__main__":
    if args.times <= 0:
        raise argparse.ArgumentTypeError("Please input a positive integer for --times.")
    run()