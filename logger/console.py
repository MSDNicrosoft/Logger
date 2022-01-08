from time import strftime
from colorama import init,Fore,Back,Style

init(autoreset=True)

sColorSuffix = "\033[0m"

def info(self):
    print(strftime(f"[%Z-%H:%M:%S][\033[32mINFO{sColorSuffix}]: {self}"))

def warn(self):
    print(strftime(f"[%Z-%H:%M:%S][\033[33mWARN{sColorSuffix}]: {self}"))

def error(self):
    print(strftime(f"[%Z-%H:%M:%S][\033[31mERROR{sColorSuffix}]: {self}"))

def debug(self):
    print(strftime(f"[%Z-%H:%M:%S][\033[34mDEBUG{sColorSuffix}]: {self}"))

def fatal(self):
    print(strftime(f"[%Z-%H:%M:%S][\033[1;31;47mFATAL{sColorSuffix}]: {self}"))

if __name__=='__main__':
    from time import sleep
    info("这是一条正常消息")
    sleep(1)
    warn("这是一条警告消息")
    sleep(2)
    error("这是一条错误消息")
    sleep(3)
    debug("这是一条调试消息")
    sleep(4)
    fatal("这是一条致命错误消息")
