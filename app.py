from flask import *  
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form  # Get form data from the POST request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    r = requests.post("https://vykmplbk62.execute-api.ap-south-1.amazonaws.com/beta/user/signup", data=json.dumps({"username":username, "password": password, "email": email, "name":"name"}))
    r.json()
    return redirect(url_for('verify'))
    
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        code = request.form.get('code')
        data = request.form  # Get form data from the POST request
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        r = requests.post("https://vykmplbk62.execute-api.ap-south-1.amazonaws.com/beta/user/confirm_sign_up", data=json.dumps({"username": username, "password":password, "email": email, "name":"harsh","code":code}))
        r.json()

        return redirect(url_for('login'))
    return render_template('verify.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        data = request.form  # Get form data from the POST request
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        r = requests.post("https://vykmplbk62.execute-api.ap-south-1.amazonaws.com/beta/user/login", data=json.dumps({"username": username, "password":password, "email": email, "name":"harsh"}))
        r.json()
        response_json_string = json.dumps(r.json())
        if 'id_token' in response_json_string:
            return f"Login successful. Welcome, {username}!"
        else:
            return f'wrong credentials'
    return render_template('login.html')


  
    
if __name__ == '__main__':
    app.run(debug=True)
