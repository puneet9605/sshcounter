from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp/ssh_counter.db"
db = SQLAlchemy(app)


class ssh_count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    count = db.Column(db.Integer)


@app.route('/')
def hello():
    text = ''
    machines = ssh_count.query.all()
    for machine in machines:
        text += "{} ssh log-in attempts were made at {}<br>".format(machine.count, machine.name)
    return text


@app.route('/updatecounter/<string:machine_id>', methods=["POST"])
def sshcounter(machine_id):
    machine = ssh_count.query.filter_by(name=machine_id).all()
    if not machine:
        machine = ssh_count(name=machine_id, count=1)
        db.session.add(machine)
    else:
        machine[0].count += 1
    db.session.commit()
    return "SSH attempt has been made for machine {}".format(machine_id)