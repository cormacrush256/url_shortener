import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3' #os.environ.get('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False