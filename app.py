from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ssh_counter.db"
db = SQLAlchemy(app)


class ssh_count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    count = db.Column(db.int)

@app.route('/')
def hello():
    return "ssh log-in attempts were made at "
