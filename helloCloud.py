from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello Ruk-com </h1>'
@app.route('/home',methods=['GET','POST'])
def home():
    links = ['http://ruk-com.in.th','https://www.bing.com',
            'https://www.python.org','http://www.kmutnb.ac.th']
    return render_template('example.html',links=links)
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0',port=80)