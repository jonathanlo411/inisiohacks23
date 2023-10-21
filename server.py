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
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')

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
            user_db.insert_one({'username': username,'display_name': display_name, 'password': hashed_pass, 'working_on': [], 'planned': [], 'mastered': []})

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

@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('dashboard.html', user=obtain_user_from_session(session))
    
@app.route('/scores', methods=['GET'])
def scores_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('scores.html', user=obtain_user_from_session(session))
    
@app.route('/explore', methods=['GET'])
def explore_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('explore.html', user=obtain_user_from_session(session))
    
@app.route('/profile', methods=['GET'])
def profile_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('profile.html', user=obtain_user_from_session(session))
    
@app.route('/settings', methods=['GET'])
def settings_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('settings.html', user=obtain_user_from_session(session))

@app.route('/play', methods=['GET'])
def play_page():
    session = obtain_session(request)
    if (not validate_session(session)):
        return redirect('login')
    else:
        return render_template('play.html', user=obtain_user_from_session(session))

# --- APIs ---

@app.route('/api/logout', methods=['POST']) # THIS IS A POST REQUEST
def logout_api():
    # Get cookie for authorization
    privilege = request.cookies.get('auth')

    # Change to ObjectID typing
    oid2 = ObjectId(privilege)

    # Check if there is active session
    check = list(mongo.db.sessions.find({'_id': oid2}))

    # If we find a logged in session
    if (len(check) == 1):
        # Logout
        mongo.db.sessions.delete_one({'_id': oid2})
    return redirect('/login')



@app.route('/api/scores', methods=['POST'])
def add_scores():
    # Get the score to add or remove
    score = request.get_json()
    score_id = score['musicID']
    score_type = score['status']

    session = obtain_session(request)


    # If we find an expired or nonexisting session
    if (not validate_session(session)):
        return {
            "success": 0,
            "message": "session invalid"
        }, 401
    else:
        if score_type == null:
            return {
                "success": 0,
                "message": "score type was null"
            }, 401
        
        # retrieve the list to update
        user = obtain_user_from_session(session)
        score_list = user[score_type]

        # Remove the score from the all
        if score_id in user["working_on"]:
            user["working_on"].remove(score_id)
        if score_id in user["planned"]:
            user["planned"].remove(score_id)
        if score_id in user["mastered"]:
            user["mastered"].remove(score_id)

        # Append the score to the appropriate list
        score_list.append(score_id)

        return {
            "success": 1,
            "message": "score added"
        }, 200


@app.route('/api/music', methods=['GET'])
def music_api():
    # Get the score 
    music_id = request.args.get('id')
    object_music = ObjectId(music_id)
    
    session = obtain_session(request)

    if (not validate_session(session)):
        return {
            "success": 0,
            "message": "session invalid"
        }, 401
    else:
        music = list(mongo.db.musicScores.find({'_id': object_music}))[0]
        return {
            "success": 1,
            "music-data": music['music'],
            "score-name": music['name']
        }, 200

# --- Helper Function ---

def obtain_session(request):
    """ Gets the session given the user's request
    """
    privilege = request.cookies.get('auth')
    oid2 = ObjectId(privilege)
    return list(mongo.db.sessions.find({'_id': oid2}))

def validate_session(session):
    """ Returns true if valid session 
    """
    return not (
        len(session) != 1
        or 
        int(datetime.now().timestamp()) >= session[0]['active_time']
    )

def obtain_user_from_session(session):
    """ Obtains the user given the session
    """
    object_id = ObjectId(session[0]['user'])
    return list(mongo.db.users.find({'_id': object_id}))[0]
