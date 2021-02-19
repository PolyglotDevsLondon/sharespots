from django.test import TestCase, Client
from core.models import Venue
from django.urls import reverse

class TestSearch(TestCase):
    """Test search functionality"""
    fixtures = ["seed_data.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse("search")

    """Search for 'Office Club' cafe via partial postcode"""
    def test_search_via_partial_postcode(self):
        response = self.client.get(self.url, {"search": "4SL"})
        venue = response.context["searched_venues"].values()
        venue_name = venue[0]["name"]

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(venue)
        self.assertEqual(len(venue), 1)
        self.assertEqual(venue_name, "Office Club")
        self.assertTemplateUsed(response, "search/venues.html")

    """Search for 'The Ramp' cafe"""
    def test_search_the_ramp(self):
        response = self.client.get(self.url, {"search": "the ramp"})
        venue = response.context["searched_venues"].values()
        venue_name = venue[0]["name"]

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(venue)
        self.assertEqual(len(venue), 1)
        self.assertEqual(venue_name, "The Ramp")
        self.assertTemplateUsed(response, "search/venues.html")

    """List all venues if search param is empty"""
    def test_search_page_show_all_venues(self):
        response = self.client.get(self.url)
        venues = response.context["searched_venues"]

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(venues)
        self.assertEqual(len(venues), 3)
        self.assertTemplateUsed(response, "search/venues.html")
