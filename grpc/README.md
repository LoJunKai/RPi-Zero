# gRPC (google Remote Procedure Call)

After installing all the requirements (I recommend creating virtual environment using venv), you can start using the gRPC packages.

1. cd into the project folder with the '.proto' file. You need to generate the library from the proto file using:

    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./example.proto
    ```

2. After the code is generated, you can run:

    ```bash
    python client.py --name client --times 10
    ```

3. Do the same for the server (your computer) then run:

    ```bash
    python server.py --name server
    ```

You will get the below output from the server and client commad line:  
![grpc1](../images/grpc1.png)  
At this point, you might need to connect to the host server (your computer), thus you need to bind the ports remote from the raspberry pi to the server by using:

```bash
ssh -R 50051:localhost:50051 pi@darryl.local
```

This connects the port from the raspberry pi to the port in the server, to allow data transfer.  
**NOTE**: if you are having trouble compiling the proto file, please look at the debugging section for common bugs and how to overcome them.

## Debugging

1. When compiling the proto file, you occur 'cannot import libatomic.so.1', follow this [source](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/issues/67):
![debug1](../images/debug1.jpg)