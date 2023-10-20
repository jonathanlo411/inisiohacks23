
from flask import Flask, request, render_template
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
    temp = mongo.db.sample
    awa= temp.find()
    #print(len(awa), flush=True)
    #for i in awa:
    #print(awa[0]['user'], flush=True)
    
    return render_template('index.html', context={"MONGO_URI": list(awa)})