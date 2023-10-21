from flask import Flask, request, render_template
import hashlib as hash
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

# Setup
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
MONGO_URI = os.getenv('MONGO_URI')

# Setup MongoDB
mongo = PyMongo(app)

# Page Render
@app.route('/', methods=['GET'])
def landing_page():
    # Make sure to remove this. Temp for testing
    # Hashing for password
    m =hash.sha256()
    m.update(b"qwefjha")
    a = m.hexdigest()
    temp = mongo.db.users

    # Makes sure no duplicate usernames
    temp.create_index('username', unique=True)
    temp_user = temp.find({'username':'jolo'})
    if (temp_user[0]['username'] == 'jolo'):
        print("wow", flush=True)
    else:
        temp.insert_one({'username':'jolo','display_name':'jolo', 'password':a})
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_input = request.get_json()
        temp = mongo.db.users
        user_input = request.form
        username = user_input['username']
        password = user_input['password']
        print(username, password, flush=True)

        # Check user exists in DB
        temp_user = list(temp.find({'username': username}))
        if (len(temp_user) != 1):
            print("failed nerd", flush=True)
        else:
            # Check if user pass matches password
            m =hash.sha256()
            m.update(password.encode('ascii'))
            a = m.hexdigest()
            if (temp_user[0]['password'] == a):
                # Redirect if good else error if wrong
                print("real", flush=True)
            else:
                print("failed p2", flush=True)
        return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    return render_template("signup.html")