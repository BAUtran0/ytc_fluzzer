from flask import Flask

api = Flask(__name__)

@api.route('/get_chat')
def get_chat():
    response_body = {
        "lmao": 123,
    }
    return response_body
