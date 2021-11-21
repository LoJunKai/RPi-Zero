import logging
import os
import threading
import time
from datetime import datetime
from multiprocessing import Event, Process
from pathlib import Path

import psutil

import testing.config as config

# import plot_metrics #TODO edit here

def GetCpuUsage(p: psutil.Process):
    return p.cpu_percent(interval=0.1)/psutil.cpu_count()


def GetMemUsage(p: psutil.Process):
    return p.memory_percent()


def GetNetworkUsage(p: psutil.Process):
    net1_out = psutil.net_io_counters().bytes_sent
    net1_in = psutil.net_io_counters().bytes_recv

    time.sleep(0.01)

    # Get new net in/out
    net2_out = psutil.net_io_counters().bytes_sent
    net2_in = psutil.net_io_counters().bytes_recv

    # Compare and get current speed
    if net1_in > net2_in:
        current_in = 0
    else:
        current_in = net2_in - net1_in

    if net1_out > net2_out:
        current_out = 0
    else:
        current_out = net2_out - net1_out

    # network = {"traffic_in" : current_in, "traffic_out" : current_out}

    if current_in == current_out:
        network_traffic = current_in # or current_out, eitherway

    return network_traffic


# Place all your logging functions here:
LOG_FN_LIST = [GetCpuUsage, GetMemUsage, GetNetworkUsage]


class Profiler:
    ''' 
    Profiles the code by:
        1: Creating a new process to run all the logging functions
        2: Spawn multiple threads, with each thread logging a specific quantity
        3: Log statements are written into a file

    When running, if you want to exit from `ctrl + c`, 
    do remember to wrap this function within a `try-catch` statement
    ```Eg:
    Try:
        a = Profiler()
        a.start_log()
    catch KeyboardInterrupt:
        a.end_log()
    ```

    To change the quantities being logged, update the LOG_FN_LIST below.
    Currently this class will pass in the `psutil.process` as an argument
    '''

    def __init__(self):
        self.pid = os.getpid()
        self.start_stop_event = Event()
        self._profiler = Process(target=run_profiler, args=(self.pid, self.start_stop_event))
        self._profiler.start()

    def start_log(self):
        ''' Start all the required logging in separate functions 
            logging is threaded and triggers the functions at precise intervals
        '''
        self.start_stop_event.set()

    def end_log(self):
        ''' Stop the logging threads '''
        print("Stopping logger... ", end="")
        while self.start_stop_event.is_set():
            # Too fast, logging process has not started yet
            time.sleep(0.01)

        self.start_stop_event.set()
        # print("stopping event sent", self.start_stop_event.is_set())
        self._profiler.join()
        print("sucessful")


def run_profiler(profiling_pid, event: Event):
    profiler = _Profiler(profiling_pid)

    event.wait()
    profiler.start_log()
    event.clear()

    # print("run_profiler started logs", event.is_set())
    event.wait()
    # print("run_profiler ending logs")
    profiler.end_log()
    # print("run_profiler logs ended")
    event.clear()
    # print("run_profiler ends")


class _Profiler:

    def __init__(self, profiling_pid):
        self.process = psutil.Process(profiling_pid)

        log_filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S') + ".csv"
        self.log_fp = Path(config.LOG_PATH, log_filename)

        logging.basicConfig(filename=self.log_fp, level=logging.INFO,  # Can change to debug to reveal debug statements
                            format="%(asctime)s%(msecs)03d,%(message)s", datefmt="%S",
                            force=True)

        logging.debug('logger initialised')

    def _log_wrapper(self, func, *args, **kwargs):
        def wrap(*args, **kwargs):
            output = f"{func(*args, **kwargs)}"
            logging.info(f"{func.__name__},{output}")
            logging.debug(func.__name__, output)

        return self._create_thread(wrap, *args, **kwargs)

    def _create_thread(self, func, *args, **kwargs):
        return SetInterval(config.LOG_INTERVAL, func, *args, **kwargs)

    def start_log(self):
        ''' Start all the required logging in separate functions 
            logging is threaded and triggers the functions at precise intervals
        '''
        self.threads = []

        for log_fn in LOG_FN_LIST:
            self.threads.append(self._log_wrapper(log_fn, self.process))

        for thr in self.threads:
            thr.start()

    def end_log(self):
        ''' Stop the logging threads '''

        for thr in self.threads:
            thr.cancel()

    # TODO > added here, need to link?
    # def plot_logs(self):        
    #     plot_metrics.reformat_log_csv(self.log_fp)
    #     plot_metrics.plotAllMetricsGraph(self.log_fp)


class SetInterval:
    # Class copied from https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval/48709380#48709380
    def __init__(self, interval, action, *args):
        self.interval = interval
        self.action = action
        self.args = args
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.__setInterval)

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.action(*self.args)

    def start(self):
        self.thread.start()

    def cancel(self):
        self.stopEvent.set()


if __name__ == "__main__":
    try:
        a = Profiler()
        a.start_log()

        i = 0
        while i < 50:
            time.sleep(0.1)
            i += 1

    finally:
        a.end_log()
        # TODO > added here, need to link?
        # a.plot_logs()
