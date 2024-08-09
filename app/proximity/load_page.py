from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/proximity')
def proximity():
    return render_template("proximity/base.html")

@app.route('/score_proximity', methods=['POST'])
def score_proximity():
    time = request.json['t']
    date = request.json['d']
    found = request.json['f']
    guesses = request.json['g']
    
    path = os.path.join(app.static_folder, 'score\proximity\countries')
    print(path)
    print(app.static_folder)

    s = []
    if os.path.isfile(path):
        with open(path, "r") as f:
            temp = f.readlines()
            s = []
            for entry in temp:
                add = entry[:-1].split(',')
                s.append([add[0], add[0], float(add[2]), add[3]])
    s.append([found, guesses, float(time), date])
    s = sorted(s, key= lambda x:(-x[0], x[1], x[2], x[3]))
    
    
    with open(path, "w+") as f:
        for entry in s:
            temp = str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "," + str(entry[3]) + "\n"
            f.write(temp)

    return jsonify({
                        'done': 'yes'
                    })