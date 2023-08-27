class MySQLDB:
    HOST = ""
    USERNAME = ""
    PASSWORD = ""
    DATABASE_NAME = ""
    URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:3306/{DATABASE_NAME}"

class SQLiteDB:
    URI = "sqlite:///database.db"

# ----------------------------- #
DEBUG = True
PORT = 5000
SQLALCHEMY_DATABASE_URI = SQLiteDB.URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your_secret_key'

