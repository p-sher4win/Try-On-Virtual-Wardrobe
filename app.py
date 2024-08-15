# app.py

from flask import Flask, render_template
import subprocess

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    # Render the about.html template
    return render_template('about.html')

@app.route('/watchs')
def cloths():
    return render_template('watchs.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tshirt')
def tshirt():
    return render_template('shirts.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/jwellery')
def jwellery():
    return render_template('jwellery.html')

@app.route('/runtScript')
def runScript():
    subprocess.Popen(['python', 'main.py'])
    return 'Script is running!'

@app.route('/runtScript2')
def runScript2():
    subprocess.Popen(['python', 'tops.py'])
    return 'Script is running!'

@app.route('/runtScript3')
def runScript3():
    subprocess.Popen(['python', 'arj/main.py'])
    return 'Script is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

