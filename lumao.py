from os import system
from time import sleep
from random import uniform, randint


for i in range(200):
    print('开始第 {} 轮点击'.format(i+1))
    for j in range(50):
        system('adb shell input tap 700 700')
    sleepTime = uniform(2, 4)
    print('结束第 {} 轮点击，休息 {} 秒'.format(i+1, sleepTime))
    sleep(sleepTime)
