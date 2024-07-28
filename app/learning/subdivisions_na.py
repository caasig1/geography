from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

#https://commons.wikimedia.org/wiki/Atlas_of_first-level_administrative_divisions

# combined north america
@app.route('/combined_na_learner')
def combined_na_learner():
    return render_template("learning/subdivisions/na.html")