#!/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

msg = [
"哎...今天够累的，签到来了",
"今天簽到了~",
"开心，非常开心！",
"仿真什么时候能出结果，好久呀！",
"打卡睡觉，走一个！",
"道道道道道道道道道道道道道道道道",
"每天一次，精",
"睡不着，居然醒了，蚊子多",
"天天开心",
"单相永磁直流无电机仿真问题",
"永磁同步注入信号",
"气隙径向磁密傅里叶分解",
"不是很懂，我也有这样的困惑",
"说的非常的好啊啊",
"谐波次数怎么算啊",
"电机优化设计的方法",
"不错，谢谢，看看!",
"非常感谢LZ，马上学习。",
"下载看看，支持下",
"继续支持下，跟着学",
"这个好，谢谢分享！",
"无私奉献辛苦了！谢谢分享",
"讲的很好，谢谢分享！",
"感谢分享 ，收藏了",
]


def send_input(get_type, key ,content):
	if get_type == "id":
		elem = driver.find_element_by_id(key)
	elem.clear()
	elem.send_keys(content)

def send_click(get_type, key):
	if get_type == "id":
		elem = driver.find_element_by_id(key)
	elif get_type == "name":
		elem = driver.find_element_by_name(key)
	actions = ActionChains(driver)
	actions.move_to_element(elem)
	actions.click(elem)
	actions.perform()

def wait_id(_id, time_out):
	while True:
		try:
			elem = driver.find_element_by_id("wl")
			return
		except Exception as e:
			time.sleep(1)
			time_out = time_out - 1
			if time_out < 1:
				raise e

def main():
	try:

		driver.get('http://bbs.simol.cn/forum.php')

		f = open('password.txt', 'r+')
		username = f.readline().strip()
		password = f.readline().strip()
		f.close()

		send_input("id", "ls_username", "wang199302")
		send_input("id", "ls_password", "simol@930716")

		elem = driver.find_element_by_id("ls_password")
		elem.send_keys(Keys.RETURN)


		wait_id("wl", 20)
		send_click("id", "wl")

		s = msg[random.randint(0, len(msg)-1)].decode('utf-8')
		send_input("id", "todaysay", s)
		elem = driver.find_element_by_id("todaysay")
		elem.send_keys(Keys.RETURN)

		time.sleep(5)
	except Exception as e:
		pass

	
	driver.close()
	driver.quit()
	sys.exit(0)


if __name__ == "__main__":
    main()