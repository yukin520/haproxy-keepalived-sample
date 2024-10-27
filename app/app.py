
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = os.getenv(key="RETURN_MSG", default="this is default message.")
    return msg

if __name__ == '__main__':
    app.run(debug=False)
