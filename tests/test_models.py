from unittest import mock
from django.utils import timezone
from django.test import TestCase
from core.models import Venue, Rating


class TestRatingModel(TestCase):
    ## SET UP RATING MODEL ##
    def setUp(self):
        self.valid_rating = Rating.objects.create(rate=5)
        self.too_big_rating = Rating.objects.create(rate=6)
        self.too_small_rating = Rating.objects.create(rate=-1)

    ## TEST RATING VALUES ARE VALID ##
    def test_rating_is_integer(self):
        self.assertEqual(type(self.valid_rating.rate), int)

    def test_rating_is_bigger_than_0_and_smaller_than_6(self):
        self.assertTrue(self.valid_rating.rate > 0)
        self.assertTrue(self.valid_rating.rate <= 5)

    def test_rating_is_not_less_than_0(self):
        self.assertFalse(self.too_small_rating.rate > 0)

    def test_rating_is_not_bigger_than_5(self):
        self.assertFalse(self.too_big_rating.rate <= 5)


class TestVenueModel(TestCase):
    ## SET UP DEFAULT VENUE MODEL ##
    def setUp(self):
        Rating.objects.create(rate=5)
        self.default_rating = Rating.objects.get(rate=5)

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
        self.assertTrue(isinstance(self.default_cafe.wifi, Rating))
        self.assertEqual(self.default_cafe.wifi, self.default_rating)

    def test_get_default_cafe_food(self):
        self.assertTrue(isinstance(self.default_cafe.food, Rating))
        self.assertEqual(self.default_cafe.food, self.default_rating)

    def test_get_default_cafe_atmosphere(self):
        self.assertTrue(isinstance(self.default_cafe.atmosphere, Rating))
        self.assertEqual(self.default_cafe.atmosphere, self.default_rating)

    def test_get_default_cafe_sockets(self):
        self.assertTrue(isinstance(self.default_cafe.sockets, Rating))
        self.assertEqual(self.default_cafe.sockets, self.default_rating)

    def test_get_default_cafe_coffee(self):
        self.assertTrue(isinstance(self.default_cafe.coffee, Rating))
        self.assertEqual(self.default_cafe.coffee, self.default_rating)

    ## MOCK THE DATETIME VALUE SO THAT AUTO_NOW_ADD USES THE MOCKED VALUE ##
    def test_get_default_cafe_created_at(self):
        testtime = timezone.now()
        with mock.patch('django.utils.timezone.now') as test_now:
            test_now.return_value = testtime
            new_venue = Venue()
            new_venue.save()

        self.assertEqual(type(self.default_cafe.post_code), str)
        self.assertEqual(testtime, new_venue.created_at)
