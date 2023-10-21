
from flask import Flask, request, render_template
import hashlib as hash
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv


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
    #print(mongo.db)

    # Hashing for password
    #m =hash.sha256()
    #m.update(b"qwefjha")
    #a = m.hexdigest()

    # Register new user
    #temp = mongo.db.users
    #temp.insert_one({'username':'jolo','display_name':'jolo', 'password':a})
    
    # Find user based on username
    #awa= temp.find({"username": "jolo"})
    #print(len(awa), flush=True)
    #for i in awa:
    #print(awa[0]['user'], flush=True)
    
    return render_template('index.html')