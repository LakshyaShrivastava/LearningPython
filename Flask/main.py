from flask import Flask



app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "<p>Hello, World</p>"

app.route('/')
def index():
    user = {"username": "Miguel"}
    return '''
    <html>
        <head>
            <title>Home Page - Exploring Flask</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>
    '''


if __name__ == "__main__":
    app.run()
