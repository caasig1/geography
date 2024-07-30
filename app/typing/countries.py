from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://github.com/georgique/world-geojson
# https://cartographyvectors.com/geo/fiji

@app.route('/countries_na_typer')
def countries_na_typer():
    return render_template("typing/countries/countries_na_type.html")

@app.route('/countries_eu_typer')
def countries_eu_typer():
    return render_template("typing/countries/countries_eu_type.html")

@app.route('/countries_sa_typer')
def countries_sa_typer():
    return render_template("typing/countries/countries_sa_type.html")

@app.route('/countries_as_typer')
def countries_as_typer():
    return render_template("typing/countries/countries_as_type.html")

@app.route('/countries_af_typer')
def countries_af_typer():
    return render_template("typing/countries/countries_af_type.html")