from django.test import LiveServerTestCase
from webdriver_manager.firefox import GeckoDriverManager 
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.quit()
