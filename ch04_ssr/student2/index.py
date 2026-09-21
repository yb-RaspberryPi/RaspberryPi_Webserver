from flask import Flask, render_template, redirect, request
import pymysql
import db

app = Flask(__name__)

@app.route("/")
def index():
    counts = db.get_counts()
    return render_template("index.html", counts=counts)

@app.route("/save", methods=['POST'])
def save():
    data = request.get_json() if request.is_json else request.form
    num = data.get('num')
    if num is not None:
        db.add_count(int(num))
    return redirect("/")

@app.route("/<num>")
def save_num_get(num):
    db.add_count(int(num))
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
