from flask import Flask
from routes import user_blueprint
import models
from flask_migrate import Migrate
import os

app = Flask(__name__)

database_path = os.path.join(os.path.dirname(__file__), 'database/user.db')

app.config['SECRET_KEY'] = 'vZK7siKrV8BL46KsyAIPoQ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
models.init_app(app)


app.register_blueprint(user_blueprint)

migrate = Migrate(app, models.db)

if __name__ == '__main__':
    app.run(debug=True)
