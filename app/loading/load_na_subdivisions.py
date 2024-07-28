from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/canada.geojson')
def canada_geojson():
    file = 'static/subdivisions/na/canada.geojson'
    return send_file(file)

@app.route('/usa.geojson')
def usa_geojson():
    file = 'static/subdivisions/na/usa.geojson'
    return send_file(file)

@app.route('/mexico.geojson')
def mexico_geojson():
    file = 'static/subdivisions/na/mexico.geojson'
    return send_file(file)

@app.route('/belize.geojson')
def belize_geojson():
    file = 'static/subdivisions/na/belize.geojson'
    return send_file(file)

@app.route('/guatemala.geojson')
def guatemala_geojson():
    file = 'static/subdivisions/na/guatemala.geojson'
    return send_file(file)

@app.route('/el_salvador.geojson')
def el_salvador_geojson():
    file = 'static/subdivisions/na/el_salvador.geojson'
    return send_file(file)

@app.route('/honduras.geojson')
def honduras_geojson():
    file = 'static/subdivisions/na/honduras.geojson'
    return send_file(file)

@app.route('/nicaragua.geojson')
def nicaragua_geojson():
    file = 'static/subdivisions/na/nicaragua.geojson'
    return send_file(file)

@app.route('/costa_rica.geojson')
def costa_rica_geojson():
    file = 'static/subdivisions/na/costa_rica.geojson'
    return send_file(file)

@app.route('/panama.geojson')
def panama_geojson():
    file = 'static/subdivisions/na/panama.geojson'
    return send_file(file)

@app.route('/cuba.geojson')
def cuba_geojson():
    file = 'static/subdivisions/na/cuba.geojson'
    return send_file(file)

@app.route('/bahamas.geojson')
def bahamas_geojson():
    file = 'static/subdivisions/na/bahamas.geojson'
    return send_file(file)

@app.route('/jamaica.geojson')
def jamaica_geojson():
    file = 'static/subdivisions/na/jamaica.geojson'
    return send_file(file)

@app.route('/haiti.geojson')
def haiti_geojson():
    file = 'static/subdivisions/na/haiti.geojson'
    return send_file(file)

@app.route('/dominican_republic.geojson')
def dominican_republic_geojson():
    file = 'static/subdivisions/na/dominican_republic.geojson'
    return send_file(file)

@app.route('/saint_kitts_and_nevis.geojson')
def saint_kitts_and_nevis_geojson():
    file = 'static/subdivisions/na/saint_kitts_and_nevis.geojson'
    return send_file(file)

@app.route('/antigua_and_barbuda.geojson')
def antigua_and_barbuda_geojson():
    file = 'static/subdivisions/na/antigua_and_barbuda.geojson'
    return send_file(file)

@app.route('/dominica.geojson')
def dominica_geojson():
    file = 'static/subdivisions/na/dominica.geojson'
    return send_file(file)

@app.route('/saint_lucia.geojson')
def saint_lucia_geojson():
    file = 'static/subdivisions/na/saint_lucia.geojson'
    return send_file(file)

@app.route('/saint_vincent_and_the_grenadines.geojson')
def saint_vincent_and_the_grenadines_geojson():
    file = 'static/subdivisions/na/saint_vincent_and_the_grenadines.geojson'
    return send_file(file)

@app.route('/grenada.geojson')
def grenada_geojson():
    file = 'static/subdivisions/na/grenada.geojson'
    return send_file(file)

@app.route('/barbados.geojson')
def barbados_geojson():
    file = 'static/subdivisions/na/barbados.geojson'
    return send_file(file)

@app.route('/trinidad_and_tobago.geojson')
def trinidad_and_tobago_geojson():
    file = 'static/subdivisions/na/trinidad_and_tobago.geojson'
    return send_file(file)

@app.route('/combined_na.geojson')
def combined_na():
    folder = os.path.join(app.static_folder, 'subdivisions')
    folder = os.path.join(folder, 'na')
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