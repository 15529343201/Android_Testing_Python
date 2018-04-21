# coding=utf-8

import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):

    @ddt.data("d3c1d53d0a8a378f","","!#$^","ASJHDJAHSJD")
    def testGet(self,device_id):
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
            "https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110100&requestTime=1472980320170&deviceType=android&device_id="+device_id,
            headers=headers,
            cookies=cookies
        )

        print res.text
        print res.status_code

        self.assertTrue(u"http://img.qcdn.static.helijia.com" in res.text)


if __name__ == "__main__":
    unittest.main()

'''
D:\python27\python.exe D:\PyCharm\helpers\pycharm\utrunner.py C:\Users\Administrator\git\Android_Testing_Python\APIAutomation\Get\testget1.py true
Testing started at 12:10 ...
{"data":{"backImg":"/upload/20171222/8/4/8434a89a757a443a92de5853ef0cfd5c.png","imageHost":"http://img.qcdn.static.helijia.com"},"processTime":0,"requestId":"57574fc3-4a64-4b2d-8bd1-002b974d40c2","serverTime":1524283656572,"success":true}
200
{"data":{"backImg":"/upload/20171222/8/4/8434a89a757a443a92de5853ef0cfd5c.png","imageHost":"http://img.qcdn.static.helijia.com"},"processTime":0,"requestId":"eae2a669-ed7d-431d-a3bf-6e926b8b1fcc","serverTime":1524283656714,"success":true}
200
{"data":{"backImg":"/upload/20171222/8/4/8434a89a757a443a92de5853ef0cfd5c.png","imageHost":"http://img.qcdn.static.helijia.com"},"processTime":0,"requestId":"626f3b0d-9d33-4283-9183-140a6ba25381","serverTime":1524283656875,"success":true}
200
{"data":{"backImg":"/upload/20171222/8/4/8434a89a757a443a92de5853ef0cfd5c.png","imageHost":"http://img.qcdn.static.helijia.com"},"processTime":0,"requestId":"2554d4b7-cf4d-4c62-b8f9-bda6999df690","serverTime":1524283657021,"success":true}
200

Process finished with exit code 0
'''