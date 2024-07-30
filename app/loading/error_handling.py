from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json, geojson, random, os

@app.errorhandler(404)
def page_not_found(e):
    # dont worry about it
    return ""