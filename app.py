from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route("/program1", methods=["GET"])
def program1():
    return jsonify({"result": "To jest pierwszy program!"})

@app.route("/program2", methods=["GET"])
def program2():
    value = 10
    squared = value ** 2
    return jsonify({"value": value, "squared": squared})

@app.route("/program3", methods=["POST"])
def program3():
    data = request.get_json()
    number = data.get("number", 0)
    cube = number ** 3
    return jsonify({"number": number, "cube": cube})

@app.route("/decision", methods=["POST"])
def decision():
    data = request.get_json()
    age = data.get("age", 0)
    income = data.get("income", 0)
    if age > 18 and income > 3000:
        decision = "Approved"
    else:
        decision = "Denied"
    return jsonify({"decision": decision})

if __name__ == "__main__":
    app.run(debug=True)
