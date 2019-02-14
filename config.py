import os

class config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joseph:pdatabase@localhost/pitch'
    SECRET_KEY = "32451618"
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
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     SECRET_KEY = os.environ.get("SECRET_KEY")

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
