from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/argentina.geojson')
def argentina_geojson():
    file = 'static/subdivisions/sa/argentina.geojson'
    return send_file(file)

@app.route('/bolivia.geojson')
def bolivia_geojson():
    file = 'static/subdivisions/sa/bolivia.geojson'
    return send_file(file)

@app.route('/brazil.geojson')
def brazil_geojson():
    file = 'static/subdivisions/sa/brazil.geojson'
    return send_file(file)

@app.route('/chile.geojson')
def chile_geojson():
    file = 'static/subdivisions/sa/chile.geojson'
    return send_file(file)

@app.route('/colombia.geojson')
def colombia_geojson():
    file = 'static/subdivisions/sa/colombia.geojson'
    return send_file(file)

@app.route('/ecuador.geojson')
def ecuador_geojson():
    file = 'static/subdivisions/sa/ecuador.geojson'
    return send_file(file)

@app.route('/guyana.geojson')
def guyana_geojson():
    file = 'static/subdivisions/sa/guyana.geojson'
    return send_file(file)

@app.route('/paraguay.geojson')
def paraguay_geojson():
    file = 'static/subdivisions/sa/paraguay.geojson'
    return send_file(file)

@app.route('/peru.geojson')
def peru_geojson():
    file = 'static/subdivisions/sa/peru.geojson'
    return send_file(file)

@app.route('/suriname.geojson')
def suriname_geojson():
    file = 'static/subdivisions/sa/suriname.geojson'
    return send_file(file)

@app.route('/uruguay.geojson')
def uruguay_geojson():
    file = 'static/subdivisions/sa/uruguay.geojson'
    return send_file(file)

@app.route('/venezuela.geojson')
def venezuela_geojson():
    file = 'static/subdivisions/sa/venezuela.geojson'
    return send_file(file)

@app.route('/subdivision_sa.geojson')
def subdivision_sa():
    folder = os.path.join(app.static_folder, 'subdivisions')
    folder = os.path.join(folder, 'sa')
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