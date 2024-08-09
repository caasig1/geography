from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

#argentina
@app.route('/argentina_typer')
def argentina_typer():
    return render_template("typing/subdivisions/sa/argentina_type.html")

#bolivia
@app.route('/bolivia_typer')
def bolivia_typer():
    return render_template("typing/subdivisions/sa/bolivia_type.html")

#brazil
@app.route('/brazil_typer')
def brazil_typer():
    return render_template("typing/subdivisions/sa/brazil_type.html")

#colombia
@app.route('/colombia_typer')
def colombia_typer():
    return render_template("typing/subdivisions/sa/colombia_type.html")

#chile
@app.route('/chile_typer')
def chile_typer():
    return render_template("typing/subdivisions/sa/chile_type.html")

#ecuador
@app.route('/ecuador_typer')
def ecuador_typer():
    return render_template("typing/subdivisions/sa/ecuador_type.html")

#guyana
@app.route('/guyana_typer')
def guyana_typer():
    return render_template("typing/subdivisions/sa/guyana_type.html")

#paraguay
@app.route('/paraguay_typer')
def paraguay_typer():
    return render_template("typing/subdivisions/sa/paraguay_type.html")

#peru
@app.route('/peru_typer')
def peru_typer():
    return render_template("typing/subdivisions/sa/peru_type.html")

#suriname
@app.route('/suriname_typer')
def suriname_typer():
    return render_template("typing/subdivisions/sa/suriname_type.html")

#uruguay
@app.route('/uruguay_typer')
def uruguay_typer():
    return render_template("typing/subdivisions/sa/uruguay_type.html")

#venezuela
@app.route('/venezuela_typer')
def venezuela_typer():
    return render_template("typing/subdivisions/sa/venezuela_type.html")

# combined south america
@app.route('/combined_sa_typer')
def combined_sa_typer():
    return render_template("typing/subdivisions/sa.html")