import urllib2
import requests
import unittest
import time

class RemoteCall:
    def __init__(self, link):
        self.url = link
		
    def testScaffold(self, line):
        results = requests.get(self.url+line, headers={'User-Agent': 'Mozilla/5.0'})
        return results.text.strip(), results.status_code

class TestMockServer(unittest.TestCase):
    def setUp(self):
        self.remote_call = RemoteCall("http://127.0.0.1:3001/")

    def testReadLineOutput(self):
        actual_output, resp_code = self.remote_call.testScaffold("12")
        time.sleep(2)
        expected_output = '\"of non-white space characters\\"). When \"'
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(resp_code, 200)

if __name__ == "__main__":
    unittest.main()
