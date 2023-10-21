from flask import Flask, request, render_template, redirect
import hashlib as hash
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from bson import ObjectId


# Setup
load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
MONGO_URI = os.getenv('MONGO_URI')

# Setup MongoDB
mongo = PyMongo(app)

# Page Render
@app.route('/', methods=['GET'])
def landing_page():
    context = {
        "user": "jolo"
    }
    return render_template('index.html', context=context)



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_input = request.get_json()
        user_db = mongo.db.users

        # Get inputed information
        username = user_input['username']
        password = user_input['password']

        # Check user exists in DB
        user_check = list(user_db.find({'username': username}))
        if (len(user_check) != 1):                          # Check user is actually real
            return {
                "success": 0,
                "message": "Wrong Username"
            }, 401
        else:                               
            # Hash inputted password
            pass_hash =hash.sha256()
            pass_hash.update(password.encode('ascii'))
            hashed_pass = pass_hash.hexdigest()

            if (user_check[0]['password'] == hashed_pass):  # Check if user pass matches password
                # Create user session
                # Store user _id, active time (for 7 days)
                # Store session id into cookie
                active_time = int((datetime.now() + timedelta(days=7)).timestamp())

                # Insert new session
                mongo.db.sessions.insert_one({'user': str(user_check[0]['_id']), 'active_time': active_time})

                # Get session id (already hashed)
                curr_user = list(mongo.db.sessions.find({'user': str(user_check[0]['_id']), 'active_time': active_time}))

                # Return cookie to frontend
                return {
                    "success": 1,
                    "cookie": str(curr_user[0]['_id'])
                }, 200
            else:
                return {
                    "success": 0,
                    "message": "Wrong Password"
                }, 401
    else:
        # Get cookie for authorization
        privilege = request.cookies.get('auth')

        # Change to ObjectID typing
        oid2 = ObjectId(privilege)

        # Check if there is active session
        check = list(mongo.db.sessions.find({'_id': oid2}))
        
        #print(check[0]['active_time'], flush=True)
        if (len(check) != 1 or int(datetime.now().timestamp()) >= check[0]['active_time']):
            return render_template('login.html')
        else: 
            return redirect('dashboard')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        user_input = request.get_json()
        user_db = mongo.db.users

        # Get inputed information
        username = user_input['username']
        password = user_input['password']
        display_name = user_input['displayName']

        # Make sure every username is unique
        user_db.create_index('username', unique=True)
        temp_user = list(user_db.find({'username':username}))

        
        if (len(temp_user) != 0):       # Username already exists
            return {
                "success": 0,
                "message": "Username taken!"
            }, 401
        elif (len(password) < 5):       # Password length < 5
            print("bruh", flush=True)
            return {
                "success": 0,
                "message": "Password is less than 5 characters long!"
            }, 401
        else:                           # Create new account
            # Hashing for password
            pass_hash =hash.sha256()
            pass_hash.update(password.encode('ascii'))
            hashed_pass = pass_hash.hexdigest()

            # Insert new account
            user_db.insert_one({'username': username,'display_name': display_name, 'password': hashed_pass})

            # Return that account made was success
            return {
                "success": 1,
                "message": "Account Made :)"
            }, 200
    else:
        # Get cookie for authorization
        privilege = request.cookies.get('auth')

        # Change to ObjectID typing
        oid2 = ObjectId(privilege)

        # Check if there is active session
        check = list(mongo.db.sessions.find({'_id': oid2}))
        
        #print(check[0]['active_time'], flush=True)
        if (len(check) != 1 or int(datetime.now().timestamp()) >= check[0]['active_time']):
            return render_template('signup.html')
        else: 
            return redirect('dashboard')


@app.route('/dashboard', methods=['GET','POST'])
def dashboard_page():
    # Get cookie for authorization
    privilege = request.cookies.get('auth')

    # Change to ObjectID typing
    oid2 = ObjectId(privilege)

    # Check if there is active session
    check = list(mongo.db.sessions.find({'_id': oid2}))

    #print(check[0]['active_time'], flush=True)
    if (len(check) != 1 or int(datetime.now().timestamp()) >= check[0]['active_time']):
        return redirect('login')
    else: 
        return render_template('dashboard.html')