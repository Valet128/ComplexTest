from django.test import TestCase, Client
from http import HTTPStatus



class ViewsTestCase(TestCase):
    def test_get_index(self):
        c = Client()
        response = c.get('')
        self.assertEqual(HTTPStatus.OK, response.status_code)
        response = c.post('')
        self.assertEqual('Ошибка ввода данных!', response.context[1]['city'])
       
        

  