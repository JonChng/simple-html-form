from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    data = request.form
    password = data['password']
    username = data['username']
    return render_template("login.html", password=password, username=username)

if __name__ == "__main__":
    app.run(debug=True)