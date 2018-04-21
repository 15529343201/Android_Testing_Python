# coding=utf-8

import requests
import unittest


class testClass(unittest.TestCase):
    def testGet(self):
        # header部分的配置
        headers = {
            'User-Agent': 'hlj-android/3.3.1',
            'Host': 'customer-api.helijia.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }

        # cookies部分的配置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTUuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        # get请求的构造
        res = requests.get(
            "https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110100&requestTime=1472980320170&deviceType=android&device_id=d3cld53d0a8a378f",
            headers=headers,
            cookies=cookies
        )

        print res.text
        print res.status_code

        self.assertTrue(u"http://img.qcdn.static.helijia.com" in res.text)


if __name__ == "__main__":
    unittest.main()
'''
D:\python27\python.exe D:\PyCharm\helpers\pycharm\utrunner.py C:\Users\Administrator\git\Android_Testing_Python\APIAutomation\Get\testget.py true
Testing started at 11:51 ...
{"data":{"backImg":"/upload/20171222/8/4/8434a89a757a443a92de5853ef0cfd5c.png","imageHost":"http://img.qcdn.static.helijia.com"},"processTime":0,"requestId":"cfcb470f-160a-4725-a15d-8b07c3fab169","serverTime":1524282534093,"success":true}
200

Process finished with exit code 0
'''