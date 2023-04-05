from django.test import LiveServerTestCase
from webdriver_manager.firefox import GeckoDriverManager 
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=10).install())
        self.driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_abre_janela_do_browser(self):
        self.driver.get(self.live_server_url)

    def test_falho_de_proposito(self):
        """teste de exemplo de erro"""
        self.fail('Teste falhou')