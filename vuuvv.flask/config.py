class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_DB = "vuuvv"
    SECRET_KEY = "KeepThisS3cr3t"

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    MONGODB_DB = "vuuvv_dev"

class Testing(Config):
    TESTING = True
    MONGODB_DB = "vuuvv_test"
