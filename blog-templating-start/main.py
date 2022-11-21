from flask import Flask, render_template
import requests
app = Flask(__name__)

post_url = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
