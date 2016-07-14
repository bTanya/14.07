from flask import Flask,request,render_template

app = Flask(__name__)
"""
@app.route('/', methods = ['GET','POST'])
def index():
    name = request.args.get('name')
    return render_template('index.html',name=name)
"""
@app.route('/<id>')
def index(id):
    return render_template('index.html')

#app.run()