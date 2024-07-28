from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://github.com/georgique/world-geojson
# https://cartographyvectors.com/geo/fiji

@app.route('/countries_eu_clicker')
def countries_eu_clicker():
    return render_template("clicking/countries/countries_eu_click.html")