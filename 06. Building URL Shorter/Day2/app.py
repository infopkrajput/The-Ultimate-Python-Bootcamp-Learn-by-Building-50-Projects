from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello to Developers'

@app.route("/about")
def about():
    return 'Hello Developers you are in about section'


if __name__ == '__main__':
    app.run(debug=True)


# To run this application we can just run
# flash run
