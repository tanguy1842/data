from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index6.html')
@app.route('/sign')
def sign():
    return render_template('sign.html')
@app.route('/home', methods=['GET','POST'])
def home():
    links = ['https://www.youtube.com', 'https://www.bing.com',
            'https://www.python.org', 'https://www.enkato.com']
    return render_template('exmple.html', links=links)
    

if __name__ == "__main__":
    app.run(debug=True)
