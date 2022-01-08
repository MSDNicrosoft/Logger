from time import strftime

sLogName = strftime('%Y-%m-%d_%H-%M.log')

f = open(sLogName, 'w',encoding='utf-8')

def info(self):
    f.write(strftime(f"[%Z-%H:%M:%S][INFO]: {self}\n"))
    f.flush()

def warn(self):
    f.write(strftime(f"[%Z-%H:%M:%S][WARN]: {self}\n"))
    f.flush()

def error(self):
    f.write(strftime(f"[%Z-%H:%M:%S][ERROR]: {self}\n"))
    f.flush()

def debug(self):
    f.write(strftime(f"[%Z-%H:%M:%S][DEBUG]: {self}\n"))
    f.flush()

def fatal(self):
    f.write(strftime(f"[%Z-%H:%M:%S][FATAL]: {self}\n"))
    f.flush()

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
