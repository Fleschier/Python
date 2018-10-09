# #12306的验证码初步突破
# import requests
#
#
# my_session = requests.session()#建立一个会话，自动保存cookie值
# login_url = "http://www.hdb.com/login/"
# url = 'http://www.hdb.com/suzhou/'
# "http://www.hdb.com/joinInformation/pvj92.html"
# username = "18896921733"
# password = "971231drq"
# data = {"lg_form_account": username, "lg_form_password": password}
# headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# login_res = my_session.post(login_url, data=data , headers = headers)
#
# res = my_session.get(url, cookies = login_res.cookies, headers = headers)
# # print(login_res.content)
# print(res.content.decode('utf-8'))
#

from selenium import webdriver
from requests import Session
from time import sleep

from ctypes import *
import time

def test():
    # wd.get('http://www.hdb.com/party/z7dw2.html')
    # sleep(1)
    # wd.find_element_by_class_name('myApply').click()

    wd.get('http://www.hdb.com/joinInformation/qedw2.html')
    sleep(0.5)
    wd.find_element_by_id('property_0_0').find_element_by_tag_name('input').clear()
    wd.find_element_by_id('property_0_0').find_element_by_tag_name('input').send_keys('陆甄敏')
    wd.find_element_by_id('property_0_1').find_element_by_tag_name('input').clear()
    wd.find_element_by_id('property_0_1').find_element_by_tag_name('input').send_keys('18118166751')
    wd.find_element_by_id('property_0_2').find_element_by_tag_name('input').clear()
    wd.find_element_by_id('property_0_2').find_element_by_tag_name('input').send_keys('1610404027')
    wd.find_element_by_id('property_0_3').find_element_by_tag_name('input').clear()
    wd.find_element_by_id('property_0_3').find_element_by_tag_name('input').send_keys('敬文书院')
    # wd.find_element_by_class_name('danx_i thisover').click()
    for i in range(0,3):
        wd.find_element_by_class_name('submit').find_element_by_tag_name('a').click()



req = Session()
req.headers.clear()
chromePath = r"E:\chromedriver.exe"
wd = webdriver.Chrome(executable_path =chromePath)
LogInUrl = 'http://www.hdb.com/login/'
Signupurl = 'http://www.hdb.com/party/qedw2.html'
wd.get(LogInUrl)

sleep(0.1)        #等待加载

wd.find_element_by_xpath("//div[contains(@onclick,'loginHDB.loginToggle')]").click()
wd.find_element_by_id('lg_form_account').clear()
wd.find_element_by_id('lg_form_account').send_keys('18118166751')
wd.find_element_by_id("lg_form_password").clear()
wd.find_element_by_id('lg_form_password').send_keys('123456789@')
wd.find_element_by_class_name('login_Btn').click()

sleep(0.1)        #等待加载
wd.get('http://www.hdb.com/party/qedw2.html')
sleep(0.5)
# current_time = time.localtime(time.time())
# if((current_time.tm_hour == 18) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
#     while True:
#         test()


while True:
    test()