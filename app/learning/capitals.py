from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

# https://cartographyvectors.com/geo/fiji

@app.route('/capitals_learner')
def capitals_learner():
    return render_template("learning/capitals/capitals.html")