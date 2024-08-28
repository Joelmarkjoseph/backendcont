from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://joel:0K8r39zuE0zWY5jti41Ukx1jLXsJfEAR@dpg-cr7qu3a3esus73c1221g-a.oregon-postgres.render.com/contdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
