# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 20:16:42 2022

@author: Jinesh
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Estify</h1>'

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
     sqft = float(request.form['total_sqft'])
     bath = int(request.form['bath'])
     bhk = int(request.form['bhk'])
     location = request.form['location']
     
     response = jsonify({
         'est_price': util.predict_price(sqft, bath, bhk, location)
         })
     response.headers.add('Access-Control-Allow-Origin', '*')
     
     return response

if __name__ == "__main__":
    print("Connecting to Flask Server...")
    util.load_artifacts()
    app.run()