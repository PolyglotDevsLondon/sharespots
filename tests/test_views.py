from django.test import TestCase, Client
from core.models import Venue

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.default_rating = 5
        Venue.objects.create(
            name="The Ramp",
            featured=True,
            address_1="95A Rye Lane",
            address_2="London",
            post_code="SE15 4ST",
            description="The Ramp is a co-working space, in Peckham. It offers full-time desk option as well as hot-desks, on a monthly basis (two months minimum.) Membership includes use of a meeting room, telephone booths and lockers.\r\n\r\nIt is on the third floor of an old disused multi-storey carpark, that was converted into into a creative work space.\r\n\r\nOn other floors of the building you'll find small hip business studios/offices, a food court, bars, art exhibitions, event spaces, and on the roof during the summer, the famous 'Frank's' bar/cafe with it's signature campari cocktails, festival atmosphere, and great views across London.",
            created_at="2019-10-08T16:15:09.855Z",
            wifi=self.default_rating,
            food=self.default_rating,
            atmosphere=self.default_rating,
            sockets=self.default_rating,
            coffee=self.default_rating,
            slogan="Co-working in a hip, colourful converted old multi-storey carpark in Peckham",
            image="https://i.picsum.photos/id/1016/3844/2563.jpg"
        )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_about_us_page(self):
        response = self.client.get("/about-us")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about_us.html')
    
    def test_venue_detail_404(self):
        response = self.client.get("/venue-detail/2")
        self.assertEquals(response.status_code, 404)   
    
    def test_venue_detail_with_venue(self):
        response = self.client.get("/venue-detail/1")
        self.assertEquals(response.status_code, 200)    
        self.assertTemplateUsed(response, 'core/venue.html')
    
    def test_contact_us_page(self):
        response = self.client.get("/contact")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
