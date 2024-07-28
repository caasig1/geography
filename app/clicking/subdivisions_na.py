from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

#Canada
@app.route('/canada_clicker')
def canada_clicker():
    return render_template("clicking/subdivisions/na/canada_click.html")

#USA
@app.route('/usa_clicker')
def usa_clicker():
    return render_template("clicking/subdivisions/na/usa_click.html")

#Mexico
@app.route('/mexico_clicker')
def mexico_clicker():
    return render_template("clicking/subdivisions/na/mexico_click.html")

#Belize
@app.route('/belize_clicker')
def belize_clicker():
    return render_template("clicking/subdivisions/na/belize_click.html")

#Guatemala
@app.route('/guatemala_clicker')
def guatemala_clicker():
    return render_template("clicking/subdivisions/na/guatemala_click.html")

#El Salvador
@app.route('/el_salvador_clicker')
def el_salvador_clicker():
    return render_template("clicking/subdivisions/na/el_salvador_click.html")

#Honduras
@app.route('/honduras_clicker')
def honduras_clicker():
    return render_template("clicking/subdivisions/na/honduras_click.html")

#Nicaragua
@app.route('/nicaragua_clicker')
def nicaragua_clicker():
    return render_template("clicking/subdivisions/na/nicaragua_click.html")

#Costa Rica
@app.route('/costa_rica_clicker')
def costa_rica_clicker():
    return render_template("clicking/subdivisions/na/costa_rica_click.html")

#Panama
@app.route('/panama_clicker')
def panama_clicker():
    return render_template("clicking/subdivisions/na/panama_click.html")

#Cuba
@app.route('/cuba_clicker')
def cuba_clicker():
    return render_template("clicking/subdivisions/na/cuba_click.html")

#Bahamas
@app.route('/bahamas_clicker')
def bahamas_clicker():
    return render_template("clicking/subdivisions/na/bahamas_click.html")

#Jamaica
@app.route('/jamaica_clicker')
def jamaica_clicker():
    return render_template("clicking/subdivisions/na/jamaica_click.html")

#Haiti
@app.route('/haiti_clicker')
def haiti_clicker():
    return render_template("clicking/subdivisions/na/haiti_click.html")

#Dominican Republic
@app.route('/dominican_republic_clicker')
def dominican_republic_clicker():
    return render_template("clicking/subdivisions/na/dominican_republic_click.html")

#Saint Kitts and Nevis
@app.route('/saint_kitts_and_nevis_clicker')
def saint_kitts_and_nevis_clicker():
    return render_template("clicking/subdivisions/na/saint_kitts_and_nevis_click.html")

#antigua_and_barbuda
@app.route('/antigua_and_barbuda_clicker')
def antigua_and_barbuda_clicker():
    return render_template("clicking/subdivisions/na/antigua_and_barbuda_click.html")

#dominica
@app.route('/dominica_clicker')
def dominica_clicker():
    return render_template("clicking/subdivisions/na/dominica_click.html")

#saint_lucia
@app.route('/saint_lucia_clicker')
def saint_lucia_clicker():
    return render_template("clicking/subdivisions/na/saint_lucia_click.html")

#saint_vincent_and_the_grenadines
@app.route('/saint_vincent_and_the_grenadines_clicker')
def saint_vincent_and_the_grenadines_clicker():
    return render_template("clicking/subdivisions/na/saint_vincent_and_the_grenadines_click.html")

#grenada
@app.route('/grenada_clicker')
def grenada_clicker():
    return render_template("clicking/subdivisions/na/grenada_click.html")

#barbados
@app.route('/barbados_clicker')
def barbados_clicker():
    return render_template("clicking/subdivisions/na/barbados_click.html")

#trinidad_and_tobago
@app.route('/trinidad_and_tobago_clicker')
def trinidad_and_tobago_clicker():
    return render_template("clicking/subdivisions/na/trinidad_and_tobago_click.html")

# combined north america
@app.route('/combined_na_clicker')
def combined_na_clicker():
    return render_template("clicking/subdivisions/na.html")