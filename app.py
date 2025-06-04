from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
import joblib
import pandas as pd
from features import extract_features

# Flask app setup
app = Flask(__name__)
app.secret_key = 'secret123'  # Change this in production

# Login Manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin123":
            user = User(id=1)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
@login_required
def check():
    input_text = request.form['text']
    features = extract_features(input_text)
    df = pd.DataFrame([features])
    model = joblib.load('text_detector_model.pkl')  # Load model
    score = model.predict_proba(df)[0][1]
    result = "AI-Generated" if score > 1.0 else "Human-Written"
    return render_template('result.html', result=result, score=round(score * 100, 2))

if __name__ == '__main__':
    app.run(debug=True)
