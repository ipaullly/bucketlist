import os

class Config(object):
    """parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "fghg9rt-192kd"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """configurations for development"""
    DEBUG = True

class TestingConfig(Config):
    """configurations for testing with a seperate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:polmog9439@localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """configurations for staging"""
    DEBUG = True

class ProductionConfig(Config):
    """configurations for production"""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}