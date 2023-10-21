from flask import Flask, request, render_template
import hashlib as hash
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

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
    #pass_hash =hash.sha256()
    #pass_hash.update(b"qwefjha")
    #hashed_pass = pass_hash.hexdigest()
    #user_db = mongo.db.users

    # Makes sure no duplicate usernames
    #user_db.create_index('username', unique=True)
    #temp_user = user_db.find({'username':'jolo'})
    #if (temp_user[0]['username'] == 'jolo'):
    #    print("Need to put error here", flush=True)
    #else:
    #    temp.insert_one({'username':'jolo','display_name':'jolo', 'password':hashed_pass})


    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_input = request.get_json()
        #print(user_input, flush=True)
        user_db = mongo.db.users
        username = user_input['username']
        password = user_input['password']
        #print(username, password, flush=True)

        # Check user exists in DB
        user_check = list(user_db.find({'username': username}))
        #print(user_check, flush=True)
        if (len(user_check) != 1):
            return {
                "success": 0,
                "message": "Wrong Username"
            }, 401
        else:
            # Check if user pass matches password
            pass_hash =hash.sha256()
            pass_hash.update(password.encode('ascii'))
            hashed_pass = pass_hash.hexdigest()
            if (user_check[0]['password'] == hashed_pass):
                # Create user session
                # Store user _id, expire time (need library)
                # Send _id of session
                active_time = int((datetime.now() + timedelta(days=7)).timestamp())
                mongo.db.sessions.insert_one({'user': str(user_check[0]['_id']), 'active_time': active_time})
                curr_user = list(mongo.db.sessions.find({'user': str(user_check[0]['_id']), 'active_time': active_time}))
                print(str(curr_user[0]['_id']), flush=True)
                return {
                    "success": 1,
                    "cookie": str(curr_user[0]['_id'])
                }, 200

                # Redirect if good else error if wrong
            else:
                return {
                    "success": 0,
                    "message": "Wrong Password"
                }, 401
    else:
        return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    return render_template("signup.html")