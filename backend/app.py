from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

# part 2, get a single show that has the id provided from the request
@app.route("/shows/<id>", methods=['GET'])   
def get_single_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")       # works :)
    return create_response(db.getById('shows', int(id)))        # getById(type, id) works :) 
                                                                # result is in a different order- episodes seen is above id, i don't think this will make a diffrence but we'll see

# part 3, create a new show
# https://www.poftut.com/python-try-catch-exceptions-tutorial/
# https://www.educba.com/flask-get-post-data/ !! super helpful
@app.route("/shows", methods=['POST'])
def new_show():
    request_data = request.get_json()
    try:
        name = request_data['name']
    except:
        return create_response(status=422, message = "PLease provide a show name")
    try:
        episodes_seen = request_data['episodes_seen']
    except:
        return create_response(status=422, message = "Please provide number of episodes seen")
    db.create('shows', request_data)
    return create_response(db.getById('shows', request_data['id']), status=201, message="show added") 
    
# part 4 update show
@app.route("/shows/<id>", methods=['PUT'])
def update_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists") #works 
    request_data = request.get_json()
    db.updateById('shows', int(id), request_data)      
    return create_response(db.getById('shows', int(id)))


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
