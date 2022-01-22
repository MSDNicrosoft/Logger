from time import strftime
from colorama import init

init(autoreset=True)


class Console:
    sColorSuffix = "\033[0m"

    def info(Message):
        print(strftime(f"[%Z-%H:%M:%S][\033[32mINFO{Console.sColorSuffix}]: {Message}"))

    def warn(Message):
        print(strftime(f"[%Z-%H:%M:%S][\033[33mWARN{Console.sColorSuffix}]: {Message}"))

    def error(Message):
        print(strftime(f"[%Z-%H:%M:%S][\033[31mERROR{Console.sColorSuffix}]: {Message}"))

    def fatal(Message):
        print(strftime(f"[%Z-%H:%M:%S][\033[1;31;47mFATAL{Console.sColorSuffix}]: {Message}"))

    def debug(Message):
        print(strftime(f"[%Z-%H:%M:%S][\033[34mDEBUG{Console.sColorSuffix}]: {Message}"))


class File:
    def __init__(self, FileName):
        self.FileName = FileName
        self.Operate = open(strftime(self.FileName), 'a', encoding='utf-8')

    def info(self, Message):
        self.Operate.write(strftime(f"[%Z-%H:%M:%S][INFO]: {Message}\n"))

    def warn(self, Message):
        self.Operate.write(strftime(f"[%Z-%H:%M:%S][WARN]: {Message}\n"))

    def error(self, Message):
        self.Operate.write(strftime(f"[%Z-%H:%M:%S][ERROR]: {Message}\n"))

    def fatal(self, Message):
        self.Operate.write(strftime(f"[%Z-%H:%M:%S][FATAL]: {Message}\n"))

    def debug(self, Message):
        self.Operate.write(strftime(f"[%Z-%H:%M:%S][DEBUG]: {Message}\n"))


class Log:
    def __init__(self, Shell=True, LogFile=False, FileName="%Y-%m-%d_%H-%M.log"):
        self.LogFileName = FileName
        self.shell = Shell
        self.file = LogFile

    def info(self, Message):
        if self.shell:
            Console.info(Message)
        if self.file:
            file = File(FileName=self.LogFileName)
            file.info(Message)

    def warn(self, Message):
        if self.shell:
            Console.warn(Message)
        if self.file:
            file = File(FileName=self.LogFileName)
            file.warn(Message)

    def error(self, Message):
        if self.shell:
            Console.error(Message)
        if self.file:
            file = File(FileName=self.LogFileName)
            file.error(Message)

    def fatal(self, Message):
        if self.shell:
            Console.fatal(Message)
        if self.file:
            file = File(FileName=self.LogFileName)
            file.fatal(Message)

    def debug(self, Message):
        if self.shell:
            Console.debug(Message)
        if self.file:
            file = File(FileName=self.LogFileName)
            file.debug(Message)


if __name__ == '__main__':
    from time import sleep

    logger = Log(LogFile=True)
    logger.info("这是一条正常消息")
    sleep(1)
    logger.warn("这是一条警告消息")
    sleep(2)
    logger.error("这是一条错误消息")
    sleep(3)
    logger.debug("这是一条调试消息")
    sleep(4)
    logger.fatal("这是一条致命错误消息")
