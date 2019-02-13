import os

class config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joseph:pdatabase@localhost/pitch'
    SECRET_KEY = "steve"
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(config):
     '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
     pass

class DevConfig(config):
     '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
     DEBUG = True

config_options = {
    'production': ProdConfig,
    'development': DevConfig
    
}
