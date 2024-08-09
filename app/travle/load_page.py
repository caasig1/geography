from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.route('/travle')
def travle():
    return render_template("travle/base.html")