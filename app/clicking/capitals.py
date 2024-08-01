from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

# https://cartographyvectors.com/geo/fiji

@app.route('/capitals_na_clicker')
def capitals_na_clicker():
    return render_template("clicking/capitals/capitals_na_click.html")

@app.route('/capitals_eu_clicker')
def capitals_eu_clicker():
    return render_template("clicking/capitals/capitals_eu_click.html")

@app.route('/capitals_sa_clicker')
def capitals_sa_clicker():
    return render_template("clicking/capitals/capitals_sa_click.html")

@app.route('/capitals_as_clicker')
def capitals_as_clicker():
    return render_template("clicking/capitals/capitals_as_click.html")

@app.route('/capitals_af_clicker')
def capitals_af_clicker():
    return render_template("clicking/capitals/capitals_af_click.html")

@app.route('/capitals_oc_clicker')
def capitals_oc_clicker():
    return render_template("clicking/capitals/capitals_oc_click.html")

@app.route('/capitals_clicker')
def capitals_clicker():
    return render_template("clicking/capitals/capitals_click.html")