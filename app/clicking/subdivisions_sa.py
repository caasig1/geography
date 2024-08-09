from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

#argentina
@app.route('/argentina_clicker')
def argentina_clicker():
    return render_template("clicking/subdivisions/sa/argentina_click.html")

#bolivia
@app.route('/bolivia_clicker')
def bolivia_clicker():
    return render_template("clicking/subdivisions/sa/bolivia_click.html")

#brazil
@app.route('/brazil_clicker')
def brazil_clicker():
    return render_template("clicking/subdivisions/sa/brazil_click.html")

#colombia
@app.route('/colombia_clicker')
def colombia_clicker():
    return render_template("clicking/subdivisions/sa/colombia_click.html")

#chile
@app.route('/chile_clicker')
def chile_clicker():
    return render_template("clicking/subdivisions/sa/chile_click.html")

#ecuador
@app.route('/ecuador_clicker')
def ecuador_clicker():
    return render_template("clicking/subdivisions/sa/ecuador_click.html")

#guyana
@app.route('/guyana_clicker')
def guyana_clicker():
    return render_template("clicking/subdivisions/sa/guyana_click.html")

#paraguay
@app.route('/paraguay_clicker')
def paraguay_clicker():
    return render_template("clicking/subdivisions/sa/paraguay_click.html")

#peru
@app.route('/peru_clicker')
def peru_clicker():
    return render_template("clicking/subdivisions/sa/peru_click.html")

#suriname
@app.route('/suriname_clicker')
def suriname_clicker():
    return render_template("clicking/subdivisions/sa/suriname_click.html")

#uruguay
@app.route('/uruguay_clicker')
def uruguay_clicker():
    return render_template("clicking/subdivisions/sa/uruguay_click.html")

#venezuela
@app.route('/venezuela_clicker')
def venezuela_clicker():
    return render_template("clicking/subdivisions/sa/venezuela_click.html")

# combined south america
@app.route('/combined_sa_clicker')
def combined_sa_clicker():
    return render_template("clicking/subdivisions/sa.html")