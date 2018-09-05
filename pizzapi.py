from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name':'tonno', "rating" : "5 reten","prijs": 700,"vorm" : "rond", "ingredienten" : ['tomaat','kaas','tonijn','e-nummers','tarwe','smaakstoffen']},
    {'name':'salami', "rating" : "3 reten","prijs": 600,"vorm" : "vierkant", "ingredienten" : ['vlees','kaas','tomaat','e-nummers','tarwe','koen']},
    {'name':'magarita', "rating" : "4 reten","prijs": 500,"vorm" : "driehoek", "ingredienten" :['kaas','tomaat','e-nummers','tarwe','koen']}
]


@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if name == pizza['name']:
            resultPizza.append(pizza)

    return jsonify({'pizzaDB':resultPizza})

if __name__ == "__main__":
    app.run(debug=True, port=8080)