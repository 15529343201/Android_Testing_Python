# urs/bin/python
# encoding:utf-8
import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        '''
        C:\Users\Administrator>adb devices
        List of devices attached
        192.168.28.101:5555     device
        '''
        desired_caps['deviceName'] = '192.168.28.101:5555'
        '''
        adb logcat | find "START"
        '''
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 释放实例,释放资源
    def tearDown(self):
        self.driver.quit()

    # 测试的脚本, LOVE原则
    def testAdd(self):
        # Locate 定位一个元素
        number8 = self.driver.find_element_by_id("digit8")
        # Operate 操作一个元素
        number8.click()
        # Locate 定位一个元素
        addopertion = self.driver.find_element_by_id("plus")
        # Operate 操作一个元素
        addopertion.click()
        # Locate 定位一个元素
        number5 = self.driver.find_element_by_id("digit5")
        # Operate 操作一个元素
        number5.click()
        # Locate 定位一个元素
        equal = self.driver.find_element_by_id("equal")
        # Operate 操作一个元素
        equal.click()

        # Verify 验证操作的结果
        try:
            result = self.driver.find_element_by_class_name("android.widget.EditText")
            value = result.text
            self.assertEqual(u"13", value)
        except Exception:
            print "程序出现异常了"
            self.fail("程序出现异常")
            # Exception 处理异常的情况


if __name__ == '__main__':
    unittest.main()
