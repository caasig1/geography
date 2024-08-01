from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://github.com/georgique/world-geojson
# https://cartographyvectors.com/geo/fiji

@app.route('/capitals_na_typer')
def capitals_na_typer():
    return render_template("typing/capitals/capitals_na_type.html")

@app.route('/capitals_eu_typer')
def capitals_eu_typer():
    return render_template("typing/capitals/capitals_eu_type.html")

@app.route('/capitals_sa_typer')
def capitals_sa_typer():
    return render_template("typing/capitals/capitals_sa_type.html")

@app.route('/capitals_as_typer')
def capitals_as_typer():
    return render_template("typing/capitals/capitals_as_type.html")

@app.route('/capitals_af_typer')
def capitals_af_typer():
    return render_template("typing/capitals/capitals_af_type.html")

@app.route('/capitals_oc_typer')
def capitals_oc_typer():
    return render_template("typing/capitals/capitals_oc_type.html")

@app.route('/capitals_typer')
def capitals_typer():
    return render_template("typing/capitals/capitals_type.html")