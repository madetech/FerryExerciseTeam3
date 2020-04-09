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
    price = request.args.get('price', 0, type=float)
    return jsonify(result=corn*price,price=(corn*price))
if __name__ == '__main__':
    main()
