# pip install pandas
# pi[ install matplotlib

import config
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

# log_filename = "here_2021-11-21 04-22-42.csv" #not yet formatted
log_filename = "2021-11-21 06-07-00.csv" #alr formatted
log_fp = Path(config.LOG_PATH, log_filename)

#once logfile reformatted, can immediately plot graph, dunnid reformat again
def reformat_log_csv(log_fp):

    #rearranging > pivot table
    df = pd.read_csv(log_fp, header = None, prefix="var")
    df['var3'] = df['var0'] #duplicate time column
    df['var4'] = df['var0'] #duplicate time column
    df['var3'] = df['var3'].shift(+1).fillna(0) #shift column var3 by 1 row down
    df['time'] = df['var4'] - df['var3'] #create new column "time" difference
    df = df.iloc[1: , :] #remove first row 
    df = df.drop(df.columns[[0, 3, 4]], axis=1) # remove all other extra time columns
    df = df.rename(columns={'var1': 'type','var2': 'value'})
    pivoted = pd.pivot_table(df,index=["time"],columns=["type"],values=["value"]).fillna(method='ffill')
    print(pivoted)
    pivoted.to_csv("./grpc/temp.csv", encoding='utf-8', index=True) #will always be overwritten 

    # pivot table > drop multi rows > so that can plot
    saved_pivot_table = pd.read_csv("./grpc/temp.csv", header = None, prefix="var")
    df = saved_pivot_table.rename(columns={'var0': 'time','var1': 'GetCpuUsage','var2': 'GetMemUsage', 'var3': 'GetNetworkUsage'})
    df = df.iloc[3: , :] #drop unecessary rows
    df.to_csv(log_fp, encoding='utf-8', index=False) 
    print(df) # to check

    return None

# reformat_log_csv(log_fp)

def plotAllMetricsGraph(log_fp):
    #input from csv file
    file = pd.read_csv(log_fp)
    #plot specifications
    plt.figure(figsize=(8,5))
    plt.title('Performance Metrics over Time (secs)', fontdict={'fontweight':'bold', 'fontsize': 10})
    plt.xlabel('Metrics')
    plt.ylabel('time (sec)')
    plt.plot(file.time, file.GetCpuUsage, 'bo-', label='Cpu Usage (%)')  # blue
    plt.plot(file.time, file.GetMemUsage, 'yo-', label='Memory Usage (%)')  # yellow
    plt.plot(file.time, file.GetNetworkUsage, 'go-', label='Bandwith (bytes) ')  # green
    plt.legend()
    # plt.savefig() before plt.show() > to save pic into folder
    plt.savefig('./grpc/AllMetricsGraph.png', dpi=300)
    plt.show()
    return None

def plotCpuGraph(log_fp):
    #input from csv file
    file = pd.read_csv(log_fp)
    #plot specifications
    plt.figure(figsize=(8,5))
    plt.title('Performance Metrics over Time (secs)', fontdict={'fontweight':'bold', 'fontsize': 10})
    plt.xlabel('Metrics')
    plt.ylabel('time (sec)')
    plt.plot(file.time, file.GetCpuUsage, 'bo-', label='Cpu Usage (%)')  # blue
    plt.legend()
    plt.savefig('./grpc/CpuGraph.png', dpi=300)
    plt.show()
    return None

def plotMemGraph(log_fp):
    #input from csv file
    file = pd.read_csv(log_fp)
    #plot specifications
    plt.figure(figsize=(8,5))
    plt.title('Performance Metrics over Time (secs)', fontdict={'fontweight':'bold', 'fontsize': 10})
    plt.xlabel('Metrics')
    plt.ylabel('time (sec)')
    plt.plot(file.time, file.GetMemUsage, 'yo-', label='Memory Usage (%)')  # yellow
    plt.legend() 
    plt.savefig('./grpc/MemGraph.png', dpi=300)
    plt.show()
    return None


def plotNetworkGraph(log_fp):
    #input from csv file
    file = pd.read_csv(log_fp)
    #plot specifications
    plt.figure(figsize=(8,5))
    plt.title('Performance Metrics over Time (secs)', fontdict={'fontweight':'bold', 'fontsize': 10})
    plt.xlabel('Metrics')
    plt.ylabel('time (sec)')
    plt.plot(file.time, file.GetNetworkUsage, 'go-', label='Bandwith (bytes) ')  # green
    plt.legend()
    plt.savefig('./grpc/NetworkGraph.png', dpi=300)
    plt.show()
    return None

plotAllMetricsGraph(log_fp)
plotCpuGraph(log_fp)
plotMemGraph(log_fp)
plotNetworkGraph(log_fp)