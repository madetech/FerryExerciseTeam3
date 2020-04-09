from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

class Ferry(object):

    def __init__(self, load, price):
        self.load = load
        self.price = price

def main():
    app.run()

@app.route('/')
def hello():
    return render_template('index.html', title='Home')

@app.route('/_add_numbers')
def add_numbers():
    corn = request.args.get('corn', 0, type=int)
    geese = request.args.get('geese', 0, type=int)
    price = request.args.get('price', 0, type=float)

    if corn < 0 or geese <0 :
        return jsonify(error=1,error_message="Only positive geese and corn pls")
    if corn > 0 and geese > 2 :
        return jsonify(error=1,error_message="Too many geese to make this trip possible with the corn!")
    if corn > 2 and geese > 0 :
        return jsonify(error=1,error_message="Too much corn to make this trip possible with the goose!")

    return jsonify(error=0,price=(corn*price))

if __name__ == '__main__':
    main()
