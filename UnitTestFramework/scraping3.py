import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/abdulsalam/Documents/dll/chromedriver")
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("Test")
        assert True
    
    def not_a_test(self):
        print("This wont print")
    
    def tearDown(self):
        self.driver.close()

if __name__ == "_main_":
    unittest.main()
    