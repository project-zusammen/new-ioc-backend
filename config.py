import os

class Config(object):
    APP_ENV = os.environ.get('APP_ENV',"localhost")
    APP_DEBUG = os.environ.get("APP_DEBUG", False)
    APP_PORT = os.environ.get("APP_PORT",5000)
    
    HOST = str(os.getenv("DB_HOST"))
    DATABASE = str(os.getenv("DB_DATABASE"))
    USERNAME = str(os.getenv("DB_USERNAME"))
    PASSWORD = str(os.getenv("DB_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://" + USERNAME + ":" + PASSWORD + "@" + HOST + "/" + DATABASE
    )
    