from datetime import datetime
from flask import Flask, render_template,request, redirect, session, url_for, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test1234@164.125.219.21:13306/dummy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def main(): 
    return 'Hello World!'


@app.route('/insert', methods=['POST'])
def insert_user():
    new_user = User(username=request.form['username'])
    db.session.add(new_user)
    db.session.commit()
    return 'Registration done!'
   

class User(db.Model):
    __table_name__ = 'user'
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User('{self.id}', '{self.username}')>"

if __name__ == '__main__':
    app.run()