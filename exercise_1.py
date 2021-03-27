
from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1, 501)]

# 模拟卖票 w 表达窗口
def sell(w):
    while ticket:
        print("%s 窗口卖出:%s"%(w,ticket.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target = sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
