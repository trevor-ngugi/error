from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)

  #app configs
  app.config.from_object(config_options[config_name])
  #initializing flask extensions
  bootstrap.init_app(app)

  #register blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  #will add pitch and forms

  return app
