from flask import Flask, jsonify, request
app=Flask(__name__)
tasks = [
    {
        'id': 1,
        'Name': u'Merl',
        'Contact': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Bob',
        'Contact': u'0987654321', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return ("Hello World")

@app.route("/add_data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get_data")
def get_task():
    return jsonify({
        "data":tasks
    })
if(__name__ == "__main__"):
    app.run(debug=True)