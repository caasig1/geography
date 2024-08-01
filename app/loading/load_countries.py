from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

def helper(continent):
    folder = os.path.join(app.static_folder, 'country_outlines')
    folder = os.path.join(folder, continent)
    countries = []
    capitals = []

    for filename in os.listdir(folder):
        fp = os.path.join(folder, filename)
        if os.path.isfile(fp):
            with open(fp, 'r') as f:
                data = geojson.load(f)
            
            for feature in data['features']:
                if feature['geometry']['type'] in ['MultiPolygon','Polygon']:
                    countries.append(feature)
                elif feature['geometry']['type'] == 'Point':
                    capitals.append(feature)

    return [countries, capitals]

@app.route('/countries.geojson')
def countries():
    countries = []
    capitals = []

    temp = helper('na')
    countries.extend(temp[0])
    capitals.extend(temp[1])

    temp = helper('sa')
    countries.extend(temp[0])
    capitals.extend(temp[1])

    temp = helper('europe') # remove turkey cyprus and russia dupes
    temp[0].pop(43)
    temp[0].pop(35)
    temp[0].pop(8)
    temp[1].pop(43)
    temp[1].pop(35)
    temp[1].pop(8)
    countries.extend(temp[0])
    capitals.extend(temp[1])

    temp = helper('africa')
    countries.extend(temp[0])
    capitals.extend(temp[1])

    temp = helper('asia')
    countries.extend(temp[0])
    capitals.extend(temp[1])

    temp = helper('oc')
    countries.extend(temp[0])
    capitals.extend(temp[1])

    countries = geojson.FeatureCollection(countries)
    capitals = geojson.FeatureCollection(capitals)
    return [countries, capitals]