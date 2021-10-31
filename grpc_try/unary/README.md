<!-- set up first -->
mkdir grpc_example
cd grpc_example

python3 -m virtualenv env
source env/bin/activate
pip install grpcio grpcio-tools

python3 -m pip install grpcio
python3 -m pip install grpcio-tools

python3 -m pip install protobuf