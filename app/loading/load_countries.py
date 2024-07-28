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
            
            if data['type'] == 'FeatureCollection':
                geodata.extend(data['features'])
            elif data['type'] == 'Feature':
                geodata.append(data)

    geodata = geojson.FeatureCollection(geodata)
    return geodata

@app.route('/countries_na.geojson')
def countries_na():
    return helper('na')

@app.route('/countries_eu.geojson')
def countries_eu():
    return helper('eu')

@app.route('/countries_sa.geojson')
def countries_sa():
    return helper('sa')