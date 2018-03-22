from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['SECRET_KEY'] = "randomsupersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"


allowed_extensions = app.config['ALLOWED_EXTENSIONS']

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
