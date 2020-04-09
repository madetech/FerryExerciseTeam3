from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def main():
    app.run()


RULES = [
    lambda hunted, hunter: hunted > 0 and hunter == 0,
    lambda hunted, hunter: hunted <= 2 and hunter == 1,
    lambda hunted, hunter: hunted < 2 and hunter == 2,
    lambda hunted, hunter: hunted == 0 and hunter > 2,
]

@app.route('/')
def hello():
    return render_template('index.html', title='Home')

def construct_itinerary(corn, geese):
    return [
        {
            'farm_side': {'corn': (corn - 1) - c, 'geese': 0},
            'in_transit': {'corn': 1, 'geese': 0},
            'market_side': {'corn': c, 'geese': 0},
        }
        for c in range(corn)
    ]


@app.route('/_add_numbers')
def add_numbers():
    corn = request.args.get('corn', 0, type=int)
    geese = request.args.get('geese', 0, type=int)
    price = request.args.get('price', 0, type=float)

    total_price = (((corn + geese)*2)-1) * price
    if corn < 0 or geese < 0:
        return jsonify(error=1, error_message="Only positive geese and corn pls")
    if is_valid(corn, geese):
        itinerary = construct_itinerary(corn, geese)
        return jsonify(error=0, price=total_price, itinerary=itinerary)
    return jsonify(error=1, error_message="Trip not possible")


def is_valid(corn,geese):
     for rule in RULES:
        if rule(corn,geese):
            return True

if __name__ == '__main__':
    main()

'''
works:
c > 0 and g = 0
c <= 2 and g = 1
c < 2 and g = 2
c = 0 and g > 2


c = 1  and g = 1 and fox = 1
c = 2  and g = 1 and fox = 1

'''
