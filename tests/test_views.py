from django.test import TestCase, Client
from core.models import Venue

# Create your tests here.
class TestView(TestCase):
    fixtures = ["seed_data.json"]

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_about_us_page(self):
        response = self.client.get("/about-us")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about_us.html')
    
    def test_venue_detail_404(self):
        response = self.client.get("/venue-detail/5")
        self.assertEquals(response.status_code, 404)   
    
    def test_venue_detail_with_venue(self):
        response = self.client.get("/venue-detail/1")
        self.assertEquals(response.status_code, 200)    
        self.assertTemplateUsed(response, 'core/venue.html')
    
    def test_contact_us_page(self):
        response = self.client.get("/contact")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
