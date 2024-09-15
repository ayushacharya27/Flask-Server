from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {'user1' : 'password123', 'user2' : 'anypassword'}

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signin', methods = ['GET','POST'])
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request
        rd']
        if username in users and users[username] == password:
            return f'Welcome, {username}!'
        
        else:
            error = "Invalid Credentials. Please try again."
    return render_template('signin.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)

