from .models import Venue

## CLASS CONTAINS HELPER FUNCTIONS FOR VENUE MODEL INTERACTIONS ##
class VenueHelpers:

    def __init__(self):
        self.name = 'Test Cafe'
        self.address_1 = '10'
        self.address_2 = 'Test Street'
        self.post_code = 'W1D 3PU'
        self.description = 'I am a cafe.'

    def create_default_venue(self):
        new_venue = Venue.objects.create(name=self.name,
                            address_1=self.address_1,
                            address_2=self.address_2,
                            post_code=self.post_code,
                            description=self.description)
        return new_venue


    def check_default_venue_exists(self):
        try:
            venue = Venue.objects.get(name=self.name)
        except Venue.DoesNotExist as e:
            print('No Default Venue in your Database: {}'.format(e))
            return False
        return True

    def get_default_venue(self):
        try:
            venue = Venue.objects.get(name=self.name)
        except Venue.DoesNotExist as e:
            print('No Default Venue in your Database: {}'.format(e))
            return None

        return venue

    def get_venue(self, id):
        try:
            venue = Venue.objects.get(id=id)
        except Venue.DoesNotExist as e:
            print('Venue Not in Database: {}'.format(e))
            return None
       
        return venue