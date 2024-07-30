from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

# https://cartographyvectors.com/geo/fiji

@app.route('/countries_na_learner')
def countries_na_learner():
    return render_template("learning/countries/countries_na.html")

@app.route('/countries_eu_learner')
def countries_eu_learner():
    return render_template("learning/countries/countries_eu.html")

@app.route('/countries_sa_learner')
def countries_sa_learner():
    return render_template("learning/countries/countries_sa.html")

@app.route('/countries_as_learner')
def countries_as_learner():
    return render_template("learning/countries/countries_as.html")

@app.route('/countries_af_learner')
def countries_af_learner():
    return render_template("learning/countries/countries_af.html")

@app.route('/countries_oc_learner')
def countries_oc_learner():
    return render_template("learning/countries/countries_oc.html")

@app.route('/countries_learner')
def countries_learner():
    return render_template("learning/countries/countries.html")