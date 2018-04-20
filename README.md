# chapter1
APP在启动过程中的耗时情况<br>
- CPU占比率
- 流量消耗情况
- 电量消耗情况
- 闪存消耗情况
- 流畅度

测试一些网络API接口<br>
- UIAutomator|
- Appium     |----> Native App/Hybrid App
- Unittest   |

持续集成<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter1/Image/1.PNG)

APP的性能问题<br>
- 命令测试
- python脚本自动化测试

测试完后统计结果分析<br>
UIAutomator Appium Unittest<br>
API接口测试<br>
理论-->工具-->脚本-->框架<br>

持续集成<br>
git jenkins<br>
- 尽早发现问题
- 提高提测质量
- 提高项目进度的透明度
- 提高回归测试效率

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter1/Image/2.PNG)

# chapter2
### 内容
1.启动时间<br>
2.CPU<br>
3.流量<br>
4.电量<br>
5.内存<br>
6.FPS<br>
7.过度渲染<br>
### 环境准备
- Android SDK
- Python2.7
- PyCharm

下载android-sdk_r24.4.1-macosx.zip:<br>
http://tools.android-studio.org/index.php/sdk<br>
https://blog.csdn.net/jdfkldjlkjdl/article/details/72528551<br>
https://www.cnblogs.com/yjmyzz/p/4219829.html<br>
https://blog.csdn.net/camlot_/article/details/47424671<br>
https://blog.csdn.net/lsd200624101033/article/details/51898619<br>
```
先要安装jdk
export ANDROID_HOME=/Users/shiyongchao/Downloads/android-sdk
export PATH=${PATH}:${ANDROID_HOME}/platforms
export PATH=${PATH}:${ANDROID_HOME}/tools

shiyongchaodeMac:tools shiyongchao$ adb devices
List of devices attached
```
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/3.PNG)
### 启动时间-冷启动
- 启动App命令 `adb shell am start -W -n package/acitvity`
- 停止App命令 `adb shell am force-stop package`
- 获取包名 `adb logcat | grep start`

打开自带模拟器的浏览器:<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/4.PNG)<br>
关掉自带的app<br>
然后执行:<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/5.PNG)

### 启动时间-热启动
- 启动App命令 `adb shell am start -W -n package/acitvity`
- 停止App命令 `adb shell input keyevent 3`

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/6.PNG)
### 自动化脚本的实现
- 获取命令执行时间,作为启动时间参考值
- 在命令前后加上时间戳,以差值作为参考值

### 执行时间
- App Class:LaunchApp、StopApp、GetLaunchedTime
- Controller Class:run、collectAllData、SaveDataToCSV

打开pycharm:创建mookStartTime工程<br>
### 时间戳差值
- App Class:LaunchApp、StopApp、CalculateTime、TimeBeforeLaunch、TimeAfterLaunch
- Controller Class:run、collectAllData、SaveDataToCSV

## CPU
- 获取数据:`adb shell dumpsys cpuinfo | grep packagename`

## 流量
- 获取进程ID指令:`adb shell ps | grep packagename`
- 获取进程ID流量:`adb shell cat /proc/pid/net/dev`

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/7.PNG)
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/8.PNG)

## 电量
- 获取电量:`adb shell dumpsys battery`
- 切换非充电状态:`adb shell dumpsys battery set status 1`

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/9.PNG)
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/10.PNG)

## 内存
- 获取内存:`adb shell top` `VSS-Virtual Set Size 虚拟耗用内存` `RSS-Resident Set Size 实际使用物理内存`

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/11.PNG)
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/12.PNG)

- `adb shell top -d 1 > meminfo`
- `cat meminfo | grep com.android.browser`

## FPS&过度渲染
- FPS:frames per second - 每秒的帧数
- 过度渲染:描述的是屏幕上的某个像素在同一帧的时间内被绘制了多次

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/13.PNG)
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter2/Image/14.PNG)

# chapter3 
## 自动化实现的问题
- 代码混乱,难阅读
- 重复编码,效率低
- 需求变化,难维护

## 应用测试框架的意义
- 提高代码的易读性
- 提高编码效率
- 提高代码的易维护性

## 课程安排
- 自动化实例
- Unittest
- 数据驱动
- 实践

## 准备一个测试的App
- 在App登录页面进行登录,登录成功后自动退出

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/15.PNG)

## 准备自动化测试环境
- Appium
- Android SDK
- Appium-python-client
- Selenium
- UIAutomatorViewer
- PyCharm

Appium环境搭建:https://blog.csdn.net/kuangshow0227/article/details/73200984<br>

## 自动化实例
- 确认自动化环境
- 自动化脚本编写
- 自动化脚本的运行

进入D:\android-sdk\tools找到uiautomatorviewer并启动<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/16.PNG)<br>
`adb devices` 获取手机名称<br>
```Python
#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.mook.mook'
desired_caps['appActivity'] = '.LoginActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("email").send_keys("mooktest")
driver.find_element_by_id("password").send_keys("mooktest")
driver.find_element_by_id("email_sign_in_button").click()

try:
    if driver.find_element_by_id("email_sign_in_button").is_displayed():
        print "fail"
except Exception, e:
        print e
        print "pass"

driver.quit()

time.sleep(5)
```
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/17.PNG)
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/18.PNG)<br>

## Test Fixture
- 含义:A test fixture represents the preparation needed to perform one or more tests,and any associate cleanup actions.
- 结构:setup()、testcase()、teardown()

```Python
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
```
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/19.PNG)<br>
```Python
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "setup"

    def test_something(self):
        print "test something"
        self.assertEqual(True, False)

    def test_anything(self):
        print "test anything"
        self.assertEqual(True, True)

    def tearDown(self):
        print "teardown"


if __name__ == '__main__':
    unittest.main()
```
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter3/Image/20.PNG)<br>


