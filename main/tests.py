from django.test import TestCase, Client
from django.http import HttpResponse

# Create your tests here.
class MainTest(TestCase):
    def test_main_exists(self):
        response: HttpResponse = Client().get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_main_template_test(self):
        response: HttpResponse = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_information_test(self):
        response: HttpResponse = Client().get('/')
        self.assertContains(response, "Muhammad Oka")
        self.assertContains(response, "PBP KKI")