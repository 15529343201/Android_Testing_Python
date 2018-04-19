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
https://www.cnblogs.com/yjmyzz/p/4219829.html<br>
https://blog.csdn.net/camlot_/article/details/47424671<br>
```
先要安装jdk
export ANDROID_HOME=/Users/shiyongchao/Downloads/android-sdk
export PATH=${PATH}:${ANDROID_HOME}/platforms
export PATH=${PATH}:${ANDROID_HOME}/tools

shiyongchaodeMac:tools shiyongchao$ adb devices
List of devices attached
```
### 启动时间-冷启动
- 启动App命令 `adb shell am start -W -n package/acitvity`
- 停止App命令 `adb shell am force-stop package`

