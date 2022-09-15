from django.test import TestCase, Client
from django.urls import resolve
from .views import show_katalog
# Create your tests here.

class KatalogTest(TestCase):
    def test_contoh_app_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code,200)
    def test_contoh_app_use_template(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response,'katalog.html')