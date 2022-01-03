import string
from .extensions import db
from random import choices

#class that forms the links between the original url and the shortened url
class URL_Connector(db.Model):

    CONST_MAX_STRING_LENGTH = 600
    CONST_MAX_SHORT_URL_LENGTH = 5

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(CONST_MAX_STRING_LENGTH))
    short_url = db.Column(db.String(CONST_MAX_SHORT_URL_LENGTH), unique = True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.create_shortened_url()

    def create_shortened_url(self):

        #combines all alphanumeric chars (upper and lower case (62 total)) into a list
        alphanumeric_chars = string.digits + string.ascii_letters

        #randomly creates an object  of length 'CONST_MAX_SHORT_URL_LENGTH'
        #916132832 combinations
        short_url = ''.join(choices(alphanumeric_chars, k = URL_Connector.CONST_MAX_SHORT_URL_LENGTH))

        #a check to see if shortened url already exists
        #if short url already exists in database function is called again
        link = self.query.filter_by(short_url=short_url).first() #use exists?

        if link:
            return self.create_shortened_url()

        return short_url
