# Add import path
# import sys
# from pathlib import Path
# sys.path.insert(0, Path(__file__).parents[1])

# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

# from testing.config import *

# p = Profiler()

print("starting MQTT... ", end="")

parser = argparse.ArgumentParser(description='Client process for MQTT')
parser.add_argument('--times', metavar='t', type=int,
                    help='times to send json payload')

args = parser.parse_args()

with open(TEST_FILE1, "rb") as test1:
    # Read the docs here: https://github.com/eclipse/paho.mqtt.python
    count = 0

    # p.start_log()
    while count < int(args.times):
        publish.single(TEST_TOPIC1, test1.read(), hostname="localhost")
        count += 1
        print("{}: {}".format('Sent count: ', count))
    # p.end_log()

print("done")
