from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Flask!"

# Define a route with a dynamic segment (e.g., user/<name>)

@app.route('/ayush')
def ayush():
    return "Ayush"

if __name__ == '__main__':
    app.run()
