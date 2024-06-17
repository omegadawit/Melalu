from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure the session to use filesystem (instead of signed cookies)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "supersecretkey"
Session(app)

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
    return render_template('index.html', score=session['score'])

@app.route('/click')
def click():
    session['score'] += 1
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['score'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)