import os

class Config(object):
    HOST = str(os.getenv("DB_HOST"))
    DATABASE = str(os.getenv("DB_DATABASE"))
    USERNAME = str(os.getenv("DB_USERNAME"))
    PASSWORD = str(os.getenv("DB_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://" + USERNAME + ":" + PASSWORD + "@" + HOST + "/" + DATABASE
    )
    