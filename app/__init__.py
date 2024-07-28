from flask import Flask, render_template, send_file, request, jsonify

app = Flask(__name__)
app.secret_key = 'caasig#1'

from app import handler, main_routes
from app.loading import load_na_subdivisions, load_countries
from app.clicking import countries, subdivisions_na
from app.learning import countries, subdivisions_na
from app.typing import countries, subdivisions_na