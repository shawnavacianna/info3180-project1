import datetime
from . import db


class UserProfile(db.Model):
    user_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    biography = db.Column(db.String(200))
    created_on = db.Column(db.String(255))
    photo = db.Column(db.String(80))

    __tablename__= "users"
    
    def __init__(self,user_ID,FirstName,LastName,gender,Email,Location,Biography,photo,created_on):
        self.user_ID = user_ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.gender = gender
        self.Email = Email
        self.Location = Location
        self.Biography = Biography
        self.photo = photo
        self.created_on = created_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
