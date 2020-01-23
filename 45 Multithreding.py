#multithriding in python
from threading import Thread
from time import sleep
class Google(Thread):
    def run(self):
        for i in range(1,51):

            print("Google task",i)
            sleep(1)


class Facebook(Thread):
    def run(self):
        for i in range(1,51):

            print("Facebook task",i)
            sleep(1)


class LinkedIn(Thread):
    def run(self):
        for i in range(1,51):

            print("LinkedIn task",i)
            sleep(1)

thread1=Google()
thread2=Facebook()
thread3=LinkedIn()
thread1.start()
sleep(0.2)
thread2.start()
sleep(0.2)
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("bye")