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

```Python
#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest

class MytestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.mook.mook'
        desired_caps['appActivity'] = '.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testLogInOk(self):
        self.driver.find_element_by_id("email").send_keys("mooktest@sougou.com")
        self.driver.find_element_by_id("password").send_keys("mooktest")
        self.driver.find_element_by_id("email_sign_in_button").click()

        try:
            if self.driver.find_element_by_id("email_sign_in_button").is_displayed():
                exist = True
        except Exception, e:
            exist = False
        self.assertEqual(exist,False)

    def testLogInFailed(self):
        self.driver.find_element_by_id("email").send_keys("mooktest")
        self.driver.find_element_by_id("password").send_keys("mooktest")
        self.driver.find_element_by_id("email_sign_in_button").click()

        try:
            if self.driver.find_element_by_id("email_sign_in_button").is_displayed():
                exist = True
        except Exception, e:
            exist = False
        self.assertEqual(exist, True)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

## Test Case
- 含义:A test case is the smallest unit of testing.It checks for a specific response to a particular set of inputs

## Test Suite
- 含义:A test suite is a collection of test cases,test suites,or both.It is used to aggregate tests that should be executed together.
 
## Test Runner
- 含义:A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.

```Python
import unittestdemo
import  unittest

mysuite = unittest.TestSuite()
mysuite.addTest(unittestdemo.MyTestCase("testLogInFailed"))
mysuite.addTest(unittestdemo.MyTestCase("testLogInOK"))
cases = unittest.TestLoader().loadTestsFromTestCase(unittestdemo.MyTestCase)
mysuite = unittest.TestSuite([cases])
mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
```

## 数据驱动
- 含义:DDT(Data-Driven Tests)allows you to multiply one test case by running it with defferent test data,and make it appear as multiple test cases.
- 准备第三方库:首先安装ddt库,其次在脚本中引入ddt:https://pypi.org/project/ddt/  `python setup.py install`

```Python
from ddt import ddt,data,unpace
@ddt 
class MookTestCase(unittest.TestCase)
```
- 数据驱动的应用

```Python
使用元组存放被测试的数据,一个参数的情况
@data(1,-3,2,0)
def testcase(self,value):
使用元组存放被测试的数据,多个参数的情况
@data((3,2),(4,3),(5,3))
@unpack
def testcase(self,value1,value2)
```
- 在登录过程中,将登录的数据,使用数据驱动实现

# chapter4
## App API自动化测试
- 基础概念
- Fiddler
- Postman
- DDT在API自动化中的应用

## 基础概念
- 什么是API? API(Application Programming Interface,简称API),又称为应用程序编程接口,就是软件系统不同组成部分衔接的约定。API种类:面向对象语言的API、库与框架的API、API与协议、API与接口设备、Web API与协议、API与接口设备、Web API
- HTTP API:HTTP中的8种不同的方法:GET、POST、PUT、DELETE、OPTIONS、HEAD、TRACE、CONNECT

## Fiddler
- Fiddler的环境准备
- Fiddler的工作原理
- Fiddler的基本界面
- Fiddler设置断点修改Request
- Fiddler设置断点修改Response
- Fiddler小工具
- Fiddler Host设置
- Fiddler构造HTTP请求
- Fiddler抓取手机包

下载Fiddler:https://www.telerik.com/download/fiddler<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/21.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/22.PNG)<br>
安装完成后退出,再启动.<br>

### Fiddler的工作原理
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/23.PNG)<br>
### Fiddler设置断点修改Request
- 设置断点的两种方式:1.通过工具栏设置断点、2.通过命令设置断点

Rules-->Automatic Breakpoints-->Before Requests<br>
命令行拦截:bpu www.google.com.hk<br>
清除:bpu<br>

### Fiddler设置断点修改Response
- 设置断点的三种方式:1.通过工具栏设置断点、2.通过命令设置断点、3.AutoResponse设置

`bpafter www.google.com.hk`<br>
`bpafter`<br>

`工具栏:AutoResponder`<br>
### Fiddler小工具
- 常用的小工具:1.会话的过滤、2.会话的比较、3.编码小工具

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/24.PNG)<br>
对比:选中两个URL,右键compare,下载WinDiff到Fiddler目录下<br>
编码:Tools-->TextWizard<br>

### Fiddler Host的设置
- Host设置方式:

1.找到windows系统下的host文件,进行修改<br>
2.安装一个小工具,帮助修改host<br>
3.借助Fiddler工具,实现host的修改<br>
Tools-->Host<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/25.PNG)<br>

### Fiddler构造HTTP请求
- 构造http请求:1.构造Get请求、2.构造Post请求

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/26.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/27.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/28.PNG)<br>

### Fiddler抓取手机包
- 设置过程:1.配置Fiddler允许监听https、2.配置Fiddler允许远程连接、3.手机端设置代理服务

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/29.PNG)<br>
- 优点:1.无需Root权限、2.Android&IOS均适用

### Post Man
- API接口测试时的问题:1.后端服务提测时间早于客户端、2.很难用客户端模拟异常请求、3.Fiddler的composer无法实现自动化验证
- 适用范围:PC、WAP、App
- 环境准备:1.安装应用包、2.注册新的用户

1.发送一条http Get请求<br>
2.发送一条http Post请求<br>
3.设置检查点,检验请求的返回值<br>
4.自动运行请求集合<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/30.PNG)<br>
构造post请求<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter4/Image/31.PNG)<br>

### DDT在API自动化中的应用
- Python requests模块的准备
- HTTP Get测试脚本的实现
- HTTP Post测试脚本的实现
- 在API自动化中应用DDT

下载requests:<br>
http://docs.python-requests.org/en/master/user/install/#pipenv-install-requests<br>

# chapter5
- 持续集成的概念
- 持续集成工具详解
- 持续集成实例

### 持续集成的概念
- 持续集成的定义

&emsp;&emsp;Martin Fowler和Kent Beck首次提出Continuous Integration(简称:CI),将之描述为:持续集成是一种软件开发实践,团队成员频繁地集成它们的工作。每位成员通常进行日常集成,进而每天会有多种集成。每个集成会由自动的构建(包括测试)来尽可能快地检测错误。许多团队发现这种方法可以显著的减少集成问题并且可以使团队的开发更加快捷。<br>
- 持续集成的流程

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/32.PNG)<br>
- 持续集成的意义

1.尽早发现问题,提高提测质量<br>
2.构建情况清晰,提高项目进度的透明度<br>
3.测试过程完全自动化,提高回归测试效率<br>

### 持续集成工具详解
- 代码管理工具(Git、Github)
- 集成工具(Jenkins) https://jenkins.io/download/thank-you-downloading-windows-installer/

启动:`java -jar jenkins.war -httpPort=8888 day8`<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/33.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/34.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/35.PNG)<br>

#### 工具的配置
- 系统的配置(Git、Github、Gradle、Android)
- JOB的配置(具体项目相关的配置)

手动下载jenkins插件:https://blog.csdn.net/ziwuzhulin/article/details/79820020<br>
Jenkins的安装和启动:https://blog.csdn.net/a804229570/article/details/72630402<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/36.PNG)<br>
创建一个Job<br>

### 持续集成实例
- 使用Jenkins自动测试App

下载:https://github.com/wensen400/MiniBrowser2<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/37.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/38.PNG)<br>
然后保存,立即构建<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/39.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/40.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/41.PNG)<br>
`adb logcat | grep START`<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/42.PNG)<br>
Jenkins工具自动化持续集成<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter5/Image/43.PNG)<br>
Jenkins连接git时异常 Failed to connect to repository:https://blog.csdn.net/mxj588love/article/details/54603191<br>
https://www.cnblogs.com/EasonJim/p/6398213.html<br>

# chapter6
### Android Native App自动化
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter6/Image/44.PNG)<br>
### 课程安排
- 自动化工具简介
- 环境的准备
- 元素识别工具
- 脚本设计原则
- 自动化脚本实现
- 相关API的应用

### 自动化工具简介
- Appium的介绍
- Appium理念
- Appium的特点
- Appium的架构

#### Appium的介绍
- Appium是一个开源、跨平台的自动化测试工具,用于测试Native(原生)和Hybrid(混合)应用,支持IOS,Android和FirefoxOS平台
- Android平台 基于UIAutomator框架

#### Appium的理念
- 无需重新编译应用
- 不局限于语言和框架
- 无需重复造轮子,接口统一
- 无论精神上,还是名义上,必须开源

#### Appium的特点
- 跨架构,Native、Hybrid、Webview
- 跨设备,Android、IOS、Firefox OS
- 跨语言,Java、Python、Ruby、PHP、JavaScript
- 跨进程,不依赖源码(基于UIAutomator)

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter6/Image/45.PNG)<br>
#### 环境的准备
- Appium
- Test Device
- Test App
- Appium-python-client、Selenium
- android-sdk

#### 元素识别工具
- UIAutomatorViewer 工具的启动、工具的应用

`D:\android-sdk\tools`<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter6/Image/46.PNG)<br>
#### 脚本设计原则
- LOVE原则

L:Locate定位元素<br>
O:Operate操作元素<br>
V:Verify验证结果<br>
E:Exception处理异常<br>
#### 自动化脚本实现
以手机上的计算器为例<br>
- 测试计算器的加法、减法功能:Appium的配置、启动,脚本的初始化,脚本的实现-LOVE原则,脚本的运行

`adb logcat | find "START"`<br>

### 相关API的应用
- `find_element_by_id()`
- `find_elements_by_id()`
- `find_element_by_accessibility_id()`
- `find_elements_by_accessibility_id()`
- `find_element_by_class_name()`
- `find_elements_by_class_name()`
- `press_keycode()`
- `send_keys`
- `click`
- `time.sleep()`
- `assertTrue()`
- `assertEqual()`

![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter6/Image/47.PNG)<br>
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter6/Image/48.PNG)<br>
- `scroll()`
- `drag_and_drop()`
- `tap()`
- `swipe()`
- `flick()`
- `current_activity`
- `wait_activity()`
- `background_app()`
- `is_app_installed()`
- `install_app()`
- `remove_app()`
- `launch_app()`
- `close_app()`
- `start_activity()`
- `get_screenshot_as_file()`

# chapter7
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter7/Image/49.PNG)<br>
### 课程安排
- Appium的原理
- 环境的准备
- 元素识别工具
- 脚本设计原则
- 自动化脚本的实现
- 相关API的应用

#### Appium的原理
- 针对于Hybrid的App,Appium基于Selendroid框架实现,而Selendroid框架又是基于Instrumentation框架实现的。
- 可见,Appium本身是借助于其他框架控制App。

#### Selendroid的架构
![image](https://github.com/15529343201/Android_Testing_Python/blob/chapter7/Image/50.PNG)<br>



















