from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

#Canada
@app.route('/canada_typer')
def canada_typer():
    return render_template("typing/subdivisions/na/canada_type.html")

#USA
@app.route('/usa_typer')
def usa_typer():
    return render_template("typing/subdivisions/na/usa_type.html")

#Mexico
@app.route('/mexico_typer')
def mexico_typer():
    return render_template("typing/subdivisions/na/mexico_type.html")

#Belize
@app.route('/belize_typer')
def belize_typer():
    return render_template("typing/subdivisions/na/belize_type.html")

#Guatemala
@app.route('/guatemala_typer')
def guatemala_typer():
    return render_template("typing/subdivisions/na/guatemala_type.html")

#El Salvador
@app.route('/el_salvador_typer')
def el_salvador_typer():
    return render_template("typing/subdivisions/na/el_salvador_type.html")

#Honduras
@app.route('/honduras_typer')
def honduras_typer():
    return render_template("typing/subdivisions/na/honduras_type.html")

#Nicaragua
@app.route('/nicaragua_typer')
def nicaragua_typer():
    return render_template("typing/subdivisions/na/nicaragua_type.html")

#Costa Rica
@app.route('/costa_rica_typer')
def costa_rica_typer():
    return render_template("typing/subdivisions/na/costa_rica_type.html")

#Panama
@app.route('/panama_typer')
def panama_typer():
    return render_template("typing/subdivisions/na/panama_type.html")

#Cuba
@app.route('/cuba_typer')
def cuba_typer():
    return render_template("typing/subdivisions/na/cuba_type.html")

#Bahamas
@app.route('/bahamas_typer')
def bahamas_typer():
    return render_template("typing/subdivisions/na/bahamas_type.html")

#Jamaica
@app.route('/jamaica_typer')
def jamaica_typer():
    return render_template("typing/subdivisions/na/jamaica_type.html")

#Haiti
@app.route('/haiti_typer')
def haiti_typer():
    return render_template("typing/subdivisions/na/haiti_type.html")

#Dominican Republic
@app.route('/dominican_republic_typer')
def dominican_republic_typer():
    return render_template("typing/subdivisions/na/dominican_republic_type.html")

#Saint Kitts and Nevis
@app.route('/saint_kitts_and_nevis_typer')
def saint_kitts_and_nevis_typer():
    return render_template("typing/subdivisions/na/saint_kitts_and_nevis_type.html")

#antigua_and_barbuda
@app.route('/antigua_and_barbuda_typer')
def antigua_and_barbuda_typer():
    return render_template("typing/subdivisions/na/antigua_and_barbuda_type.html")

#dominica
@app.route('/dominica_typer')
def dominica_typer():
    return render_template("typing/subdivisions/na/dominica_type.html")

#saint_lucia
@app.route('/saint_lucia_typer')
def saint_lucia_typer():
    return render_template("typing/subdivisions/na/saint_lucia_type.html")

#saint_vincent_and_the_grenadines
@app.route('/saint_vincent_and_the_grenadines_typer')
def saint_vincent_and_the_grenadines_typer():
    return render_template("typing/subdivisions/na/saint_vincent_and_the_grenadines_type.html")

#grenada
@app.route('/grenada_typer')
def grenada_typer():
    return render_template("typing/subdivisions/na/grenada_type.html")

#barbados
@app.route('/barbados_typer')
def barbados_typer():
    return render_template("typing/subdivisions/na/barbados_type.html")

#trinidad_and_tobago
@app.route('/trinidad_and_tobago_typer')
def trinidad_and_tobago_typer():
    return render_template("typing/subdivisions/na/trinidad_and_tobago_type.html")

# combined north america
@app.route('/combined_na_typer')
def combined_na_typer():
    return render_template("typing/subdivisions/na.html")