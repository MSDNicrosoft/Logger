from . import console

class Log:
    def __init__(self,Console=True,File=False):
        self.console = Console
        self.file = File

    def info(self,i):
        if self.console:
            console.info(i)
        if self.file:
            from . import file
            file.info(i)
    
    def warn(self,i):
        if self.console:
            console.warn(i)
        if self.file:
            from . import file
            file.warn(i)

    def error(self,i):
        if self.console:
            console.error(i)
        if self.file:
            from . import file
            file.error(i)

    def debug(self,i):
        if self.console:
            console.debug(i)
        if self.file:
            from . import file
            file.debug(i)

    def fatal(self,i):
        if self.console:
            console.fatal(i)
        if self.file:
            from . import file
            file.fatal(i)

if __name__=='__main__':
    from time import sleep
    logger = Log(File=True)
    logger.info("这是一条正常消息")
    sleep(1)
    logger.warn("这是一条警告消息")
    sleep(2)
    logger.error("这是一条错误消息")
    sleep(3)
    logger.debug("这是一条调试消息")
    sleep(4)
    logger.fatal("这是一条致命错误消息")
