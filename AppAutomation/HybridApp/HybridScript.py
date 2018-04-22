# urs/bin/python
# encoding:utf-8
import time
from appium import webdriver
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 定义初始化的属性信息
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.3'
        self.desired_caps['deviceName'] = '192.168.56.101:5555'
        self.desired_caps['appPackage'] = 'com.example.zhangjian.minibrowser2'
        self.desired_caps['appActivity'] = '.myapplication.MainActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        self.desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    '''def testSearch(self):
        #Locate 定位输入框
        input = self.driver.find_element_by_id("url")
        #Operate 操作
        input.send_keys("http://wap.sogou.com")

        searchbutton = self.driver.find_element_by_id("searchbutton")
        searchbutton.click()

        time.sleep(5)

        #Switch 切换当前的上下文
        print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        print self.driver.current_context
        time.sleep(5)

        #定位web输入框
        webinput = self.driver.find_element_by_xpath('//*[@id="keyword"]')
        webinput.click()
        webinput.send_keys("mook")
        websearchbutton = self.driver.find_element_by_xpath('//*[@id="searchform"]/div/div[1]/div[3]/input')
        websearchbutton.click()
        time.sleep(5)

        #检验查询结果
        firstresult = self.driver.find_element_by_xpath('//*[@id="mainBody"]/div[2]/div[2]/a')
        self.assertTrue(u"中国大学" in firstresult.text)'''

    def testFindElements(self):
        # Locate 定位输入框
        input = self.driver.find_element_by_id("url")
        # Operate 操作
        input.send_keys("http://wap.sogou.com")

        searchbutton = self.driver.find_element_by_id("searchbutton")
        searchbutton.click()

        time.sleep(5)

        # Switch 切换当前的上下文
        print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        print self.driver.current_context
        time.sleep(5)

        #定位元素组
        elements = self.driver.find_elements_by_xpath('//*[@id="page"]/div[2]/div[2]/div/table/tbody/tr/td')

        #输出所有元素的名称
        for el in elements:
            print el.text

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
