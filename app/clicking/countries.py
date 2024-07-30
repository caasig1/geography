from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

# https://cartographyvectors.com/geo/fiji

@app.route('/countries_na_clicker')
def countries_na_clicker():
    return render_template("clicking/countries/countries_na_click.html")

@app.route('/countries_eu_clicker')
def countries_eu_clicker():
    return render_template("clicking/countries/countries_eu_click.html")

@app.route('/countries_sa_clicker')
def countries_sa_clicker():
    return render_template("clicking/countries/countries_sa_click.html")

@app.route('/countries_as_clicker')
def countries_as_clicker():
    return render_template("clicking/countries/countries_as_click.html")

@app.route('/countries_af_clicker')
def countries_af_clicker():
    return render_template("clicking/countries/countries_af_click.html")

@app.route('/countries_oc_clicker')
def countries_oc_clicker():
    return render_template("clicking/countries/countries_oc_click.html")

@app.route('/countries_clicker')
def countries_clicker():
    return render_template("clicking/countries/countries_click.html")