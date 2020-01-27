from flask import Flask,render_template
import mysql_con as sql

app = Flask(__name__)
post = sql.getmoviedetails()
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/1')
def hello_world1():
    return render_template('page.html', p = post[1])

@app.route('/2')
def hello_world2():
    return render_template('page.html', p = post[2])

@app.route('/3')
def hello_world3():
    return render_template('page.html', p = post[3])

@app.route('/4')
def hello_world4():
    return render_template('page.html', p = post[4])

@app.route('/5')
def hello_world5():
    return render_template('page.html', p = post[5])

@app.route('/6')
def hello_world6():
    return render_template('page.html', p = post[6])

if __name__ == '__main__':
    app.run()
