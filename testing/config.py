# Configuration file to keep track of shared variables
from pathlib import Path

# Test files
TEST_FILE1 = "./files/cMsg.json"
TEST_FILE2 = "./files/sMsg.json"

LOG_PATH = "./"
LOG_INTERVAL = 0.1  # [s]


# gRPC


# MQTT
MQTT_BROKER_IP = "192.168.193.36"  # Fill this up with the mqtt broker hostname

TEST_TOPIC1 = "testing/bandwidth_test"


# Setup

TEST_FILE1 = str(Path(Path(__file__).parent, TEST_FILE1).resolve())
TEST_FILE2 = str(Path(Path(__file__).parent, TEST_FILE2).resolve())
LOG_PATH = str(Path(Path(__file__).parent, LOG_PATH).resolve())
