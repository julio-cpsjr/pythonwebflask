from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# server = Server(host="0.0.0.0",port=7996)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# manager.add_comand('runserver',server)


lm = LoginManager(app)
lm.init_app(app)

from app.models import tables
from app.controllers import default

