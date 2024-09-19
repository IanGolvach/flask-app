from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello MSOE, and hello USA!\nWe\'re cooking now!'


if __name__ == "__main__":
    app.run()
