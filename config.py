import os
class Config:
  pass

class ProdConfig(Config):
    """
   Pruduction configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   """
  pass

class TestConfig(Config):
    """
  Testing configuration child class
  Args:
      Config: The parent configuration class with General configuration settings
  """
  pass

class DevConfig(Config):
  DEBUG= True
  pass








config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}