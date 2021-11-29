from flask import Flask, render_template, jsonify
from generator import Password
import convert

app = Flask(__name__)

@app.route("/generate/<int:length>/<digits>/<alphabets>/<specialchars>", methods=["POST"])
def generate(length, digits, alphabets, specialchars):
    digits = convert.to_bool(digits)
    alphabets = convert.to_bool(alphabets)
    specialchars = convert.to_bool(specialchars)
    password = Password()
    password.set(length, digits=digits, alphabets=alphabets, specialchars=specialchars)
    return jsonify(password=password.get())

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5500)