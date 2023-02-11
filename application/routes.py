import pandas as pd
from application import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/',methods=['POST','GET'])

def home():
    return render_template('home.html')