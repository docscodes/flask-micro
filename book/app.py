import os
from flask import Flask
from routes import book_blueprint
from models import db, init_app
from flask_migrate import Migrate


app = Flask(__name__)

database_path = os.path.join(os.path.dirname(__file__), 'database/book.db')

app.config['SECRET_KEY'] = '5fPxNUWP2Srzded6fayMeA'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(book_blueprint)
init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
