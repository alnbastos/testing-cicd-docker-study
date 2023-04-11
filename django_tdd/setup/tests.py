from django.test import LiveServerTestCase
from webdriver_manager.firefox import GeckoDriverManager 
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=10).install())
        self.driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_buscando_um_novo_animal(self):
        """ Teste se um usuário encontra um animal pesquisando. """
        
        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.driver.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito "busca animal".
        brand_element = self.driver.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome.

        # Ele pesquisa por "Leão" e clica no botão pesquisar.

        # O site exibe 4 características do animal pesquisado.

        # Ele desiste de adotar um animal.
        
        pass
