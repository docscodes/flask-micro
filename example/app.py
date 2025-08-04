from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "My Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})


@app.route('/')
def hello():
    """
    This is an example endpoint that returns 'Hello, World!'
    ---
    tags:
        - Greetings
    description: Returns a friendly greeting.
    responses:
        200:
            description: A successful response
            examples:
                application/json: "Hello, World!"
    """
    return {'message': 'Hello, World!'}


if __name__ == '__main__':
    app.run()
