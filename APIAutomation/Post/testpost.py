# coding=utf-8

import requests
import unittest
import json


class testClass(unittest.TestCase):
    def testPost(self):
        keyword = {
            "version": "3.3.1",
            "city": "110100",
            "requestTime": "1472980321726",
            "deviceType": "android",
            "device_id": "d3cld53d0a8a378f",
            "w": ""
        }

        headers = {
            'User-Agent':'hlj-android/3.3.1',
            'Host':'customer-api.helijia.com',
            'Connection':'Keep-Alive',
            'Accept-Encoding':'gzip'
        }

        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTUuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        res=requests.post(
            "https://customer-api.helijia.com/app-customer/transformers/1030/widgets",
            data=keyword,
            headers=headers,
            cookies=cookies
        )

        print res.text
        print res.status_code

        self.assertTrue(u"今日上新" in res.text)

if __name__ == "__main__":
    unittest.main()




