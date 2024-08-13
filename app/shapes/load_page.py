from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/shapes')
def shapes():
    return render_template("shapes/base.html")

@app.route('/score_shapes', methods=['POST'])
def score_shapes():
    score = request.json['score']
    
    path = os.path.join(app.static_folder, 'score\shapes.json')

    s = {}
    if os.path.isfile(path):
        with open(path, "r") as f:
            s = json.load(f)
    print(s)
    if score > 6:
        s['fail'] += 1
    else:
        s[str(score)] += 1
    
    
    with open(path, "w+") as f:
        json.dump(s, f)

    return jsonify({ 'done': 'yes' })