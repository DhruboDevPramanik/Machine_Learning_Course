from flask import Flask
app=Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/name')
def name():
    return "Hello, Dhrubo! i am boy, i am bigboy"


if __name__=='__main__':
    app.run(debug=True)



