from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://github.com/georgique/world-geojson
# https://cartographyvectors.com/geo/fiji

@app.route('/countries_na_learner')
def countries_na_learner():
    return render_template("learning/countries/countries_na.html")

@app.route('/countries_eu_learner')
def countries_eu_learner():
    return render_template("learning/countries/countries_eu.html")