from flask import Flask, render_template

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

if __name__ == '__main__':
    main()
