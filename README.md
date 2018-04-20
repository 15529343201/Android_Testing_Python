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



