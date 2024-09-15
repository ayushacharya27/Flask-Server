from flask import Flask ,redirect , render_template , request
import firebase_admin

from firebase_admin import  credentials , firestore

app = Flask(__name__)
app.secret_key ="ayush3112"

cred = credentials.Certificate(r"/home/ayush3112/flask_signup/ayushtakuli-2d4ac-firebase-adminsdk-isb1a-87b5c5274b.json")
firebase_admin.initialize_app(cred)

sendData = firestore.client()

@app.route('/')
def homePage():
    return "Welcome"

@app.route('/login')
def homePage1():
    return "Welcome1"

@app.route('/register',methods = ["GET" , "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user_data = {"username":username,"email":email , "password":password}
        sendData.collection("takuli").add(user_data)

        return redirect("/login")

    return render_template("register.html")

if __name__ =="__main__":
    app.run(debug=True)




