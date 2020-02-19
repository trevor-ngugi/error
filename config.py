import os
class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcode@localhost/pitch'
  ##DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
  ##SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

  ## email configs
  MAIL_SERVER ='smtp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  #pass

class ProdConfig(Config):

  """
   Pruduction configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
  """
  #pass
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  #pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcode@localhost/pitch'

  DEBUG = True
  #pass



config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}