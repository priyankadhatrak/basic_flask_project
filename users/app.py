from pickle import TRUE
from flask import Flask
from users.config import DB_URL,DB_CREDENTIALS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRUE