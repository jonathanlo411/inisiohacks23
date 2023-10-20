
from flask import Flask, request, render_template


# Setup
app = Flask(__name__)

# Page Render
@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')