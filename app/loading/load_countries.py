from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

def helper(continent):
    folder = os.path.join(app.static_folder, 'country_outlines')
    folder = os.path.join(folder, continent)
    geodata = []

    for filename in os.listdir(folder):
        fp = os.path.join(folder, filename)
        if os.path.isfile(fp):
            with open(fp, 'r') as f:
                data = geojson.load(f)
            
            for feature in data['features']:
                if feature['geometry']['type'] in ['MultiPolygon','Polygon']:
                    geodata.append(feature)

    geodata = geojson.FeatureCollection(geodata)
    return geodata

@app.route('/countries.geojson')
def countries():
    geodata = []

    temp = helper('na')
    geodata.extend(temp['features'])

    temp = helper('sa')
    geodata.extend(temp['features'])

    temp = helper('europe') # remove turkey cyprus and russia dupes
    temp['features'].pop(43)
    temp['features'].pop(35)
    temp['features'].pop(8)
    geodata.extend(temp['features'])

    temp = helper('africa')
    geodata.extend(temp['features'])

    temp = helper('asia')
    geodata.extend(temp['features'])

    temp = helper('oc')
    geodata.extend(temp['features'])

    geodata = geojson.FeatureCollection(geodata)
    return geodata