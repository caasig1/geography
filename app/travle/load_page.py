from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/travle')
def travle():
    return render_template("travle/base.html")

@app.route('/score_travle', methods=['POST'])
def score_travle():
    
    path = os.path.join(app.static_folder, 'score\proximity\\travle')
    print(path)
    print(app.static_folder)

    s = 0
    if os.path.isfile(path):
        with open(path, "r") as f:
            temp = f.readlines()
            s = int(temp[0])
    s += 1
    
    
    with open(path, "w+") as f:
        f.write(str(s))

    return jsonify({ 'done': 'yes' })