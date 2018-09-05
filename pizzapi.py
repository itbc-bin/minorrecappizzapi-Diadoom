from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name':'tonno'},
    {'name':'salami'},
    {'name':'magarita'}
]


@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for tempDic in pizzaDB:
        if name == tempDic['name']:
            resultPizza.append(tempDic)

    return jsonify({'pizzaDB':resultPizza})

if __name__ == "__main__":
    app.run(debug=True, port=8080)