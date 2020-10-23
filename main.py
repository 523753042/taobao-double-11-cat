from os import system, popen
import re
import sys
from random import uniform, randint
from time import sleep

from tqdm import tqdm

info = {}


def get_phone_width_height():
    size_str = popen('adb shell wm size').read()
    if not size_str:
        # print('error no adb')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        info = {
            'height': m.group(2),
            'width':  m.group(1)
        }
        print('info', info)
        print('adb shell input tap 900 '+info.get('width'))
        # return info


def touch_back():
    """
    模拟点击安卓的返回键
    :return:
    """
    system('adb shell input keyevent KEYCODE_BACK')


def swipe():
    """
    模拟滑动
    :return:
    """
    system('adb shell input swipe {} 1600 {} 1200'.format(
        randint(800, 1000), randint(800, 1000)))


def shop_around():
    """
    逛店铺
    :return:
    """
    for i in range(20):
        system('adb shell input tap 900 1250')
        bar = tqdm(range(25))

        for item in bar:
            bar.set_description('开始逛第 {} 间店铺'.format(i + 1))
            system('adb shell input swipe {} 1600 {} 1200'.format(
                randint(800, 1000), randint(800, 1000)))

        touch_back()
        sleep(uniform(2, 4))


def conference_hall():
    """
    浏览20个分会场
    :return:
    """
    for i in range(8):
        system('adb shell input tap 900 1100')

        bar = tqdm(range(25))
        for item in bar:
            bar.set_description('开始浏览第 {} 个分会场'.format(i + 1))
            system('adb shell input swipe {} 1600 {} 1200'.format(
                randint(800, 1000), randint(800, 1000)))

        touch_back()
        sleep(uniform(2, 4))
        swipe()


def main_conference_hall():
    """
    浏览双十一主会场
    :return:
    """
    system('adb shell input tap 900 1250')

    bar = tqdm(range(25))
    for item in bar:
        bar.set_description('开始浏览双十一主会场')
        system('adb shell input swipe {} 1600 {} 1200'.format(
            randint(800, 1000), randint(800, 1000)))

    touch_back()
    sleep(uniform(2, 4))
    swipe()


def other(num=1, index=4):
    """
    其他猫币任务
    :return:
    """
    tapY = 150*index+900
    for i in range(num):
        system('adb shell input tap 900 {}'.format(tapY))

        bar = tqdm(range(25))
        for item in bar:
            bar.set_description('开始其他猫币任务 {} '.format(i + 1))
            system('adb shell input swipe {} 1600 {} 1200'.format(
                randint(800, 1000), randint(800, 1000)))

        touch_back()
        sleep(uniform(2, 4))
        swipe()


def farm():
    """
    天猫农场
    :return:
    """
    system('adb shell input tap 900 1500')
    sleep(uniform(2, 4))

    bar = tqdm(range(100))
    for item in bar:
        bar.set_description('正在打开天猫农场')
        sleep(0.05)

    system('adb shell input tap 150 1550')

    bar = tqdm(range(100))
    for item in bar:
        bar.set_description('开始浏览天猫农场')
        sleep(0.40)

    touch_back()
    touch_back()


if __name__ == '__main__':
    # swipe()
    get_phone_width_height()
    # conference_hall()
    # main_conference_hall()
    # other(1, 4)
    # other(2, 5)

    # shop_around()
    # other()
    # swipe()
    # farm()
