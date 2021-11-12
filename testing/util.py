import logging
import os
import threading
from datetime import datetime
from pathlib import Path

import psutil

import config


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


class Profiler:

    # Place all your logging functions here:
    LOG_FN_LIST = [GetCpuUsage, GetMemUsage, GetNetworkUsage]

    def __init__(self):
        self.pid = os.getpid()
        self.process = psutil.Process(self.pid)

        log_filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S') + ".txt"
        log_fp = Path(config.LOG_PATH, log_filename)

        logging.basicConfig(filename=log_fp, level=logging.DEBUG,
                            format="%(asctime)s - ")

        logging.debug('starting')

        # TODO: Pass object to another process

    def _log_wrapper(self, func):
        def wrap(*args, **kwargs):
            output = f"{func(*args, **kwargs)}"
            logging.debug(output)
            print(output)
            a = self._create_thread(wrap, args, kwargs).start()
            return a
        return wrap

    def _create_thread(self, func, *args, **kwargs):
        # threading.Timer(config.LOG_INTERVAL, log_wrapper, (log_fn,))
        # print(args)
        # if args == tuple():
        #     return periodicrun.periodicrun(config.LOG_INTERVAL, func)
        # else:
        #     return periodicrun.periodicrun(config.LOG_INTERVAL, func, args=args)

        # if args == tuple() and kwargs == {}:
        #     return threading.Timer(config.LOG_INTERVAL, func)
        # elif args == tuple():
        #     return threading.Timer(config.LOG_INTERVAL, func, kwargs)
        # elif kwargs == {}:
        #     return threading.Timer(config.LOG_INTERVAL, func, args)
        # else:
        return threading.Timer(config.LOG_INTERVAL, func, *args, **kwargs)
        # threading.Timer(config.LOG_INTERVAL, self._create_thread, (func, *args), **kwargs).start()

        return

    def start_log(self):
        ''' Start all the required logging in separate functions 
            logging is threaded and triggers the functions at precise intervals
        '''
        self.threads = []

        # log_wrapper = lambda x, *args, **kw: logging.debug(f"{x(*args, **kw)}")

        for log_fn in self.LOG_FN_LIST:
            # self.threads.append(self._log_wrapper(log_fn))
            self.threads.append(self._create_thread(self._log_wrapper(log_fn)))

        for thr in self.threads:
            thr.start()

    def end_log(self):
        ''' Stop the logging threads '''

        for thr in self.threads:
            thr.cancel()
