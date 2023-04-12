from django.test import LiveServerTestCase
from webdriver_manager.firefox import GeckoDriverManager 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
        busca_animal_input = self.driver.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(busca_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        # Ele pesquisa por "Leão" e clica no botão pesquisar.
        busca_animal_input.send_keys('leão')
        self.driver.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 características do animal pesquisado.
        caracteristicas = self.driver.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um animal.

