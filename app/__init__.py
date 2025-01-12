from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.utils import simpanGambar
from flask_mail import Mail
import datetime
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'abs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fajarajah320@gmail.com'
app.config['MAIL_PASSWORD'] = 'emph lqrx ohrv tnkl'
app.config['MAIL_DEFAULT_SENDER'] = 'SIPANDA Support<fajarajah320@gmail.com>'
app.config['JWT_SECRET_KEY'] = 'bigfours'  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)  
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 900  


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
cache = Cache(app)

jwt = JWTManager(app)
mail = Mail(app)

from app import routes