import os
from flask import Flask


app = Flask(__name__)


database_path = os.path.join(os.path.dirname(__file__), 'database/order.db')

app.config['SECRET_KEY'] = "pSaOCtBJ90oNkW9nigTXAw"
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)