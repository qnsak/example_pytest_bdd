from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/",methods=['POST'])
def index():
    return render_template("hello.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)