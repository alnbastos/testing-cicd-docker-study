from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    

    def test_rota_url_utiliza_view_index(self):
        """ Teste se a home da aplicação utiliza a função index da view. """
        request = self.factory.get('/') # pega a '/' e envia ao index (função da view)

        with self.assertTemplateUsed('index.html'):
            response = index(request) # resposta da função index (view.py)
            self.assertEqual(response.status_code, 200)
