
from flask import Flask, request, render_template


# Setup
app = Flask(__name__)

# Page Render
@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_input = request.get_json()
        username = user_input['username']
        password = user_input['password']
        print(username, password, flush=True)

        # Check user exists in DB
        ...

        # Check if user pass matches password
        ...

        # Redirect if good else error if wrong
        ...
    else:
        return render_template('login.html')