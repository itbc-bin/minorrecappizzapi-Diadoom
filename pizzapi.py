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


@app.route("/name/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if name == pizza['name']:
            resultPizza.append(pizza)

    return jsonify({'pizzaDB':resultPizza})

@app.route("/vorm/<string:vorm>", methods=['GET'])
def getvormPizza(vorm):
    resultPizza = []
    for pizza in pizzaDB:
        if vorm == pizza['vorm']:
            resultPizza.append(pizza)

    return jsonify({'pizzaDB':resultPizza})

@app.route("/", methods=["POST"])
def addONePizza():
    postdata = request.json
    newPizza = {}
    for x in postdata:
        if x == "name":
            newPizza["name"] =  request.json['name']

        if x == "rating":
            newPizza["rating"]=  request.json['rating']

        if x == "vorm":
            newPizza["vorm"] =  request.json['vorm']

        if x == "prijs":
            newPizza["prijs"] =  request.json['prijs']

        if x == "ingredienten":
            newPizza["ingredienten"] =  request.json['ingredienten']


    pizzaDB.append(newPizza)
    return jsonify({'pizzaDB' : pizzaDB})


if __name__ == "__main__":
    app.run(debug=True, port=8080)