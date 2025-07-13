from flask import Flask, redirect, url_for,render_template, request, flash
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')

###Result checking by html page
@app.route('/submit', methods=['POST'])
def submit():
    total=0;
    if request.method =='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths']) 
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total=science+maths+c+datascience
        final=total/4
        if final >= 60:
            res='pass'
            
        else:
            res='fail'
        return render_template('final_result.html', result=res)

if __name__=='__main__':
    app.run(debug=True)

