from flask import Flask, flash, redirect, render_template, request, session, url_for
# configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')