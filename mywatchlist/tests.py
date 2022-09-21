from django.test import TestCase, Client

# Create your tests here.
class MyWatchlistTest(TestCase):
    def test_contoh_app_url_html_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    def test_contoh_app_url_json_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    def test_contoh_app_url_xml_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)