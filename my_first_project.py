"""
Building a backend server to give a data when what user wants
API -> Application programming interface: Layer that you put on top of an application so that it can communicate to
other apps

Flask
- Flask is a micro web framework written in python

Routers -> Decides what is shown when a route is hit, pass control to controller
Controllers -> What is done when a route is hit, decides what view the user see
Views -> What is shown when a route is hit, conceptual view of what you see, images/videos
Models -> Data models to store image/videos that the user see, part of the view

Templates
"""
import json
from typing import Dict, Any

import flask
from flask import request
from pydantic import BaseModel

app = flask.Flask(__name__) #hidden variabe, __name__ :str == "main.py"


# class User(BaseModel):
#     email: str
#
#     property functions are used to represent dynamic fields of objects, which changes w.r.t another static field
#     domain changes with email
#     @property
#     def domain(self):
#         return self.email.split("@")[-1]
#
#
# if __name__ == "__main__":
#     user: User = User(email="elson@hdb.com")
#     print(user.domain)

class StockInput(BaseModel):
    stock: str


class CallOptionOutput(BaseModel):
    stock: str
    price: float


@app.route("/predict_call_option", methods=["GET"]) #to attach a function to the app
def predict_stock_price() -> Dict[str, Dict[str, Any]]: #optional type hints, Any represent anything, float, str etc
    # Concept introduced: how to get the input stock from the client / user
    # and how to change the stock name in the output response w.r.t to input

    # use flask.request.data to get the raw bytes data from our client
    data: bytes = request.data
    # deserialize the raw bytes into a dictionary, so its easier to handle
    data_dict: Dict[str, str] = json.loads(data)
    stock_input: StockInput = StockInput.parse_obj(data_dict)
    # get the stock by key from the dictionary
    stock: str = stock_input.stock

    """Predict stock price"""
    return CallOptionOutput(
        stock=stock,
        price=100.0
    ).dict()


if __name__ == "__main__":
    app.run(port=5000)
