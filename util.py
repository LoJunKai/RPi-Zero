import psutil

def GetCpuUsage():
    return psutil.cpu_percent()

def GetMemUsage():
    return psutil.virtual_memory()

def GetNetworkUsage(addr):
    # TODO 
    # Get address and port of the MQTT or gRPC connection
    # return amount of bytes sent and such
    # placeholder return now
    return psutil.net_io_counters()