# Testing
This folder is used for measuring the performance of MQTT and gRPC. You can tune the number of files that are sent in the client/publisher run commands, '--times'.

For our test we ran with a simple JSOn file of 558 bytes for 100, 1000, 10000 times.

For the full results, pleas follow this [link](https://drive.google.com/drive/folders/1MuwJo2DjKXCEa0BCpPB7SQcP2kZnXVBb?usp=sharing)

# Results
## gRPC 100
![gRPC 100](../images/grpc_100.png)
## gRPC 1000
![gRPC 1000](../images/grpc_1000.png)
## gRPC 10000
![gRPC 10000](../images/grpc_10000.png)
## MQTT 100
![MQTT 100](../images/mqtt_100.png)
## MQTT 1000
![MQTT 1000](../images/mqtt_1000.png)
## MQTT 10000
![MQTT 10000](../images/mqtt_10000.png)