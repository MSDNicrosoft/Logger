from time import strftime
from colorama import init


__all__ = [
    "Log"
]


class Log:
    """
    参数:\n
    `Shell` -- 是否输出消息 -> 控制台 (Default：True) | Boolean\n
    `LogFile` -- 是否输出消息 -> 文件 (Default: False) | Boolean\n
    `FileName`[已使用格式化时间] -- 输出文件名（仅 LogFile=True 时此参数有效）（Default：%Y-%m-%d_%H-%M.log） | String\n
    格式化时间请参照如下方：\n
    `%y`      **两位数的年份表示（00-99）**\n
    `%Y`      **四位数的年份表示（000-9999）**\n
    `%m`      **月份（01-12）**\n
    `%d`      **月内中的一天（0-31）**\n
    `%H`      **24 小时制小时数（0-23）**\n
    `%I`      **12 小时制小时数（01-12）**\n
    `%M`      **分钟数（00=59）**\n
    `%S`      **秒（00-59）**\n
    `%a`      **本地简化星期名称**\n
    `%A`      **本地完整星期名称**\n
    `%b`      **本地简化的月份名称**\n
    `%B`      **本地完整的月份名称**\n
    `%c`      **本地相应的日期表示和时间表示**\n
    `%j`      **年内的一天（001-366）**\n
    `%p`      **本地 A.M. 或 P.M. 的等价符**\n
    `%U`      **一年中的星期数（00-53），星期天为星期的开始**\n
    `%w`      **星期（0-6），星期天为星期的开始**\n
    `%W`      **一年中的星期数（00-53），星期一为星期的开始**n
    `%x`      **本地相应的日期表示**\n
    `%X`      **本地相应的时间表示**\n
    `%Z`      **当前时区的名称**\n
    `%%`      **%号本身**
    """

    def __init__(self,
                 Shell=True,
                 LogFile=False,
                 FileName="%Y-%m-%d_%H-%M.log"
                 ):
        self.shell = Shell
        self.file = LogFile
        self.LogFileName = FileName


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


class Console:
    """This class can output colored messages to Shell"""
    sColorSuffix = "\033[0m"
    init(autoreset=True)

    @staticmethod
    def info(Message):
        print(
            strftime(
                f"[%H:%M:%S][\033[32mINFO{Console.sColorSuffix}]: {Message}"
            )
        )

    @staticmethod
    def warn(Message):
        print(
            strftime(
                f"[%H:%M:%S][\033[33mWARN{Console.sColorSuffix}]: {Message}"
            )
        )

    @staticmethod
    def error(Message):
        print(
            strftime(
                f"[%H:%M:%S][\033[31mERROR{Console.sColorSuffix}]: {Message}"
            )
        )

    @staticmethod
    def fatal(Message):
        print(
            strftime(
                f"[%H:%M:%S][\033[1;31;47mFATAL{Console.sColorSuffix}]: {Message}"
            )
        )

    @staticmethod
    def debug(Message):
        print(
            strftime(
                f"[%H:%M:%S][\033[34mDEBUG{Console.sColorSuffix}]: {Message}"
            )
        )


class File:
    """
    This class can output messages to file
    """

    def __init__(self, FileName):
        self.FileName = FileName
        self.File = open(
            strftime(self.FileName),
            "a",
            encoding="utf-8"
        )

    def info(self, Message):
        self.File.write(
            strftime(
                f"[%H:%M:%S][INFO]: {Message}\n"
            )
        )

    def warn(self, Message):
        self.File.write(
            strftime(
                f"[%H:%M:%S][WARN]: {Message}\n"
            )
        )

    def error(self, Message):
        self.File.write(
            strftime(
                f"[%H:%M:%S][ERROR]: {Message}\n"
            )
        )

    def fatal(self, Message):
        self.File.write(
            strftime(
                f"[%H:%M:%S][FATAL]: {Message}\n"
            )
        )

    def debug(self, Message):
        self.File.write(
            strftime(
                f"[%H:%M:%S][DEBUG]: {Message}\n"
            )
        )


if __name__ == '__main__':
    from time import sleep

    logger = Log(LogFile=True)
    logger.info("这是一条正常消息")
    sleep(1)
    logger.warn("这是一条警告消息")
    sleep(2)
    logger.error("这是一条错误消息")
    sleep(3)
    logger.fatal("这是一条致命错误消息")
    sleep(4)
    logger.debug("这是一条调试消息")
