from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/score', methods=['POST'])
def score():
    time = request.json['t']
    date = request.json['d']
    score = request.json['s']
    type = request.json['type']
    region = request.json['r'][2:-9].split('_')
    if len(region) == 1:
        if region[0] == 'countries':
            folder = region[0]
            file = region[0]
        else:
            folder = 'subdivision'
            file = region[0]
    else:
        if region[0] not in ["countries", "capitals", "subdivision"]:
            folder = 'subdivision'
            file = "_".join(region)
        else:
            folder = region[0]
            file = region[1]
    
    path = os.path.join(app.static_folder, 'score')
    path = os.path.join(path, folder)
    path = os.path.join(path, type)
    path = os.path.join(path, file)

    s = []
    if os.path.isfile(path):
        with open(path, "r") as f:
            temp = f.readlines()
            s = []
            for entry in temp:
                add = entry[:-1].split(',')
                s.append([float(add[0]), float(add[1]), add[2]])
    s.append([float(score), float(time), date])
    s = sorted(s, key= lambda x:(-x[0], x[1]))
    
    
    with open(path, "w+") as f:
        for entry in s:
            temp = str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "\n"
            f.write(temp)

    return jsonify({
                        'done': 'yes'
                    })