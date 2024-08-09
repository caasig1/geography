from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

#argentina
@app.route('/argentina_typer')
def argentina_typer():
    return render_template("typing/subdivisions/sa/argentina_typ.html")

#bolivia
@app.route('/bolivia_typer')
def bolivia_typer():
    return render_template("typing/subdivisions/sa/bolivia_typ.html")

#brazil
@app.route('/brazil_typer')
def brazil_typer():
    return render_template("typing/subdivisions/sa/brazil_typ.html")

#colombia
@app.route('/colombia_typer')
def colombia_typer():
    return render_template("typing/subdivisions/sa/colombia_typ.html")

#chile
@app.route('/chile_typer')
def chile_typer():
    return render_template("typing/subdivisions/sa/chile_typ.html")

#ecuador
@app.route('/ecuador_typer')
def ecuador_typer():
    return render_template("typing/subdivisions/sa/ecuador_typ.html")

#guyana
@app.route('/guyana_typer')
def guyana_typer():
    return render_template("typing/subdivisions/sa/guyana_typ.html")

#paraguay
@app.route('/paraguay_typer')
def paraguay_typer():
    return render_template("typing/subdivisions/sa/paraguay_typ.html")

#peru
@app.route('/peru_typer')
def peru_typer():
    return render_template("typing/subdivisions/sa/peru_typ.html")

#suriname
@app.route('/suriname_typer')
def suriname_typer():
    return render_template("typing/subdivisions/sa/suriname_typ.html")

#uruguay
@app.route('/uruguay_typer')
def uruguay_typer():
    return render_template("typing/subdivisions/sa/uruguay_typ.html")

#venezuela
@app.route('/venezuela_typer')
def venezuela_typer():
    return render_template("typing/subdivisions/sa/venezuela_typ.html")

# combined south america
@app.route('/combined_sa_typer')
def combined_sa_typer():
    return render_template("typing/subdivisions/sa.html")