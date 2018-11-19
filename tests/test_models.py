from unittest import mock
from django.utils import timezone
from django.test import TestCase
from core.models import Venue


class TestVenueModel(TestCase):
     ## SET UP DEFAULT CAFE MODEL ##
    def setUp(self):
        Venue.objects.create(name='test cafe',
                             address_1='10',
                             address_2='test street',
                             post_code='W1D 3PU',
                             description='This is a cafe.')

        self.default_cafe = Venue.objects.get(name='test cafe')

    def test_default_cafe_is_true(self):
        self.assertTrue(self.default_cafe)

    def test_get_default_cafe_name(self):
        self.assertEqual(type(self.default_cafe.name), str)
        self.assertEqual(self.default_cafe.name, 'test cafe')
    
    def test_get_default_cafe_address_1(self):
        self.assertEqual(type(self.default_cafe.address_1), str)
        self.assertEqual(self.default_cafe.address_1, '10')
        
    def test_get_default_cafe_address_2(self):
        self.assertEqual(type(self.default_cafe.address_2), str)
        self.assertEqual(self.default_cafe.address_2, 'test street')

    def test_get_default_cafe_postcode(self):
        self.assertEqual(type(self.default_cafe.post_code), str)
        self.assertEqual(self.default_cafe.post_code, 'W1D 3PU')

    def test_get_default_cafe_description(self):
        self.assertEqual(type(self.default_cafe.description), str)
        self.assertEqual(self.default_cafe.description, 'This is a cafe.')

    ## MOCK THE DATETIME VALUE SO THAT AUTO_NOW_ADD USES THE MOCKED VALUE ##
    def test_get_default_cafe_created_at(self):
        testtime = timezone.now()
        with mock.patch('django.utils.timezone.now') as test_now:
            test_now.return_value = testtime
            new_venue = Venue()
            new_venue.save()
        
        self.assertEqual(type(self.default_cafe.post_code), str)
        self.assertEqual(testtime, new_venue.created_at)
 