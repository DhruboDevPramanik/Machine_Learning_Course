from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Dynamic Flask App!"      

@app.route('/pass/<int:mark>')
def passes (mark):
     return "Hello, your mark is " + str(mark)

@app.route('/fail/<int:mark>')  
def fail (mark):
    return "Hello, your mark is " + str(mark)


@app.route('/result/<int:mark>')
def result(mark):
    if mark<40:
        return "You have failed with a mark of " + str(mark)
    else:
        return "You have passed with a mark of " + str(mark)


if __name__ == '__main__':
    app.run(debug=True)
    