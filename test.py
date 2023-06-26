import unittest
from selenium import webdriver

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_website_loads(self):
        driver = self.driver
        driver.get("https://www.atg.world/")
        assert "ATG World" in driver.title
        
    def tearDown(self):
        self.driver.quit()

if _name_ == "_main_":
    unittest.main()
