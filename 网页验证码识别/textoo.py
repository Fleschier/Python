# -*- coding: utf-8 -*-
import random
from io import BytesIO
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config,time
from selenium import webdriver
from PIL import Image

class CrackGreetest():
    def __init__(self):
        self.url = "https://account.geetest.com/register"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = '1409472133@qq.com'

    def open(self):
        """
        打开网页输入用户名密码
        :return:
        """
        self.browser.get(self.url)
        email = self.wait.until(expected_conditions.presence_of_element_located((By.ID,'email')))
        # password = self.wait.until(expected_conditions.presence_of_element_located((By.ID,'password')))
        email.send_keys(self.email)
        # password.send_keys(self.password)

    def get_geetest_button(self):
        '''
        获取初始验证码按钮
        :return: 按钮对象
        '''
        button = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    # def get_screenshot(self):
    #     """
    #     获取网页截图
    #     :return: 截图对象
    #     """
    #     screenshot = self.browser.get_screenshot_as_png()
    #     screenshot = Image.open(BytesIO(screenshot))
    #     return screenshot

    # def get_position(self,pos):
    #     """
    #     获取验证码位置
    #     :return: 验证码位置元组
    #     """
    #     img = self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,pos)))
    #     time.sleep(2)
    #     location = img.location
    #     size = img.size
    #     top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
    #     return (top,bottom,left,right)

    def get_unFull_image(self, path):
        """
        获取未完整验证码图片
        :param name:
        :return: 图片对象
        """
        element = self.browser.find_element_by_css_selector(
            "body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute")

        unfull_captcha = element.screenshot(path)

        # top,bottom,left,right = self.get_position(pos="canvas.geetest_canvas_slice.geetest_absolute")
        #         # print('验证码位置',top,bottom,left,right)
        #         # screenshot = self.get_screenshot()
        #         # unfull_captcha = screenshot.crop((left,top,right,bottom))
        #         # unfull_captcha.save(name)

        return unfull_captcha

    def get_full_image(self,path):
        '''
        获取完整验证码图片
        :param name:
        :return:
        '''
        # 这里要执行JavaScript脚本才能拿到完整图片的截图
        show_Full_img1 = "document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='block'"
        self.browser.execute_script(show_Full_img1)
        show_Full_img2 = "document.getElementsByClassName('geetest_canvas_fullbg')[0].style.opacity=1"
        self.browser.execute_script(show_Full_img2)
        # 等待完整图片加载
        time.sleep(2)
        element = self.browser.find_element_by_css_selector(
            "body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > canvas")
        full_captcha = element.screenshot(path)

        return full_captcha

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    # # 判断两张图片同一位置的像素是否相同。比较两张图的RGB的绝对值是否均小于定义的阈值threshold
    # # 如果绝对值均在阈值值内，则代表像素点相同，继续遍历，否者代表不相同的像素点，即缺口的位置
    # def is_pixel_equal(self,image1,image2,x,y):
    #     '''
    #     判断两个像素是否相同
    #     :param image1: 图片1
    #     :param image2: 图片2
    #     :param x: 位置x
    #     :param y: 位置y
    #     :return: 像素是否相同
    #     '''
    #     # 取两个图片的像素点
    #     pixel1 = image1.load()[x,y]
    #     pixel2 = image2.load()[x,y]
    #     # 像素对比阈值
    #     threshold = 60
    #     if abs(pixel1[0]-pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
    #         return True
    #     else:
    #         return False

    def get_gap(self,image1,image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口的图片
        :param image2: 带缺口的图片
        :return: 像素是否相同
        """
        # 缺口在滑块右侧，设定遍历初始横坐标left为65
        left = 65
        # 像素对比阈值
        threshold = 40
        for i in range(left,image1.size[0]):
            for j in range(image1.size[1]):
                rgb1 = image1.load()[i, j]
                rgb2 = image2.load()[i, j]
                print(rgb1)

                res1 = abs(rgb2[0] - rgb1[0])
                res2 = abs(rgb2[1] - rgb1[1])
                res3 = abs(rgb2[2] - rgb1[2])
                if  (res1 > threshold and res2 > threshold and res3 > threshold):
                    return i - 3   # 返回缺口偏移距离，这里需测试几次

    def get_track(self,distanc):
        '''
        x=v0*t+0.5*a*t*t
        v=v0+a*t
        根据偏移量获取移动轨迹
        :param distanc: 偏移量
        :return: 移动轨迹
        '''

        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distanc * 4 / 5
        # 计算间隔
        # t = 0.2
        t = random.randint(2,3)/10
        # 初速度
        v = 0

        while current < distanc:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            v0 = v
            # 当前速度v = v0+at
            v=v0+a*t
            # 移动距离x=v0*t+1/2*a*t*t
            move = v0*t+1/2*a*t*t
            # 当前位移
            current+=move
            # 加入轨迹
            track.append(round(move))
        track.append(-2)
        track.append(-1)
        return track

    def move_to_grap(self,slider,track):
        '''
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        '''
        # 调用ActionChains的click_and_hold()方法按住拖动底部滑块，遍历运动轨迹获取每小段位置距离，调用move_by_offset()方法移动此位移，最后调用release()方法松开鼠标
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.3)
        ActionChains(self.browser).release().perform()

    def login(self):
        """
        点击登陆
        :return:
        """
        submit = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')


    def crack(self):
        try:
            # 输入用户名
            self.open()

            # 模拟点击按钮
            button = self.get_geetest_button()
            button.click()
            time.sleep(2)

            # 获取验证码图片
            unfull_path = r'C:/Users/Y/Desktop/临时文件处理/ans/pic1.png'
            self.get_unFull_image(unfull_path)
            image1 = Image.open(unfull_path)

            # 获取带缺口的验证码图片
            full_path = r'C:/Users/Y/Desktop/临时文件处理/ans/pic2.png'
            self.get_full_image(full_path)
            image2 = Image.open(full_path)

            # 对比两张图片像素点，获取缺口位置，得到偏移距离
            # 获取缺口位置
            distance = self.get_gap(image2,image1)
            print("缺口位置",distance)

            # 获取移动轨迹
            track = self.get_track(distance)
            print("滑动轨迹",track)

            # 模拟人的行为，拖动滑块，完成验证
            slider = self.get_slider()
            # slider.click()

            # 拖动滑块
            self.move_to_grap(slider,track)
            success = self.wait.until(
                expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
            print('success')
        except:
            self.crack()

if __name__ == "__main__":
    crack = CrackGreetest()
    crack.crack()