from flask import Flask, render_template,session

app = Flask(__name__, template_folder='templates')
app.secret_key = '123'

@app.route('/')
def index():
    username = None
    if 'username' in session:
        username = session['username']
    return render_template('index.html', username=username)
    
@app.route('login', methods=['GET', 'POST'])
def login():
    if request
    
if __name__ == '__main__':
    app.run(debug=True)