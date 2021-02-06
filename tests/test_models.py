from unittest import mock
from django.utils import timezone
from django.test import TestCase
from core.models import Venue
import pytest


class TestVenueModel(TestCase):
    ## SET UP DEFAULT VENUE MODEL ##
    def setUp(self):
        self.default_rating = 5

        Venue.objects.create(name='test cafe',
                             address_1='10',
                             address_2='test street',
                             post_code='W1D 3PU',
                             description='This is a cafe.',
                             wifi=self.default_rating,
                             food=self.default_rating,
                             atmosphere=self.default_rating,
                             sockets=self.default_rating,
                             coffee=self.default_rating)

        self.default_cafe = Venue.objects.get(name='test cafe')

    ## TEST DEFAULT VALUES ARE ADDED CORRECTLY ##
    def test_get_default_cafe_pk(self):
        self.assertEqual(type(self.default_cafe.pk), int)

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

    def test_get_default_cafe_wifi(self):
        self.assertEqual(self.default_cafe.wifi, self.default_rating)

    def test_get_default_cafe_food(self):
        self.assertEqual(self.default_cafe.food, self.default_rating)

    def test_get_default_cafe_atmosphere(self):
        self.assertEqual(self.default_cafe.atmosphere, self.default_rating)

    def test_get_default_cafe_sockets(self):
        self.assertEqual(self.default_cafe.sockets, self.default_rating)

    def test_get_default_cafe_coffee(self):
        self.assertEqual(self.default_cafe.coffee, self.default_rating)

    ## MOCK THE DATETIME VALUE SO THAT AUTO_NOW_ADD USES THE MOCKED VALUE ##
    def test_get_default_cafe_created_at(self):
        testtime = timezone.now()
        with mock.patch('django.utils.timezone.now') as test_now:
            test_now.return_value = testtime
            new_venue = Venue(name='test cafe 2',
                             address_1='20',
                             address_2='mock street',
                             post_code='E1D 3PU',
                             description='This is a mock cafe.',
                             wifi=self.default_rating,
                             food=self.default_rating,
                             atmosphere=self.default_rating,
                             sockets=self.default_rating,
                             coffee=self.default_rating)
            new_venue.save()

        self.assertEqual(testtime, new_venue.created_at)
