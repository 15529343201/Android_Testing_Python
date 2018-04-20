import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):

    @data((1, 2), (2, 3))
    @unpack
    def test_something(self, value1, value2):
        print value1, value2
        self.assertEqual(value2, value1+1)

if __name__ == '__main__':
    unittest.main()
'''
D:\python27\python.exe D:\PyCharm\helpers\pycharm\utrunner.py C:\Users\Administrator\git\Android_Testing_Python\mooktest\ddttest.py true
Testing started at 21:39 ...
1 2
2 3

Process finished with exit code 0
'''