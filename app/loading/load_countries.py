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
    return helper('europe')

@app.route('/countries_sa.geojson')
def countries_sa():
    return helper('sa')

@app.route('/countries_as.geojson')
def countries_as():
    return helper('asia')

@app.route('/countries_af.geojson')
def countries_af():
    return helper('africa')

@app.route('/countries_oc.geojson')
def countries_oc():
    return helper('oc')

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