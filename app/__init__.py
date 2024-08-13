from flask import Flask, render_template, send_file, request, jsonify

app = Flask(__name__)
app.secret_key = 'caasig#1'

from app import handler, main_routes
from app.loading import load_na_subdivisions, load_countries, error_handling, load_sa_subdivisions
from app.clicking import countries, subdivisions_na, capitals, subdivisions_sa
from app.learning import countries, subdivisions_na, capitals, subdivisions_sa
from app.typing import countries, subdivisions_na, capitals, subdivisions_sa
from app.travle import load_page
from app.proximity import load_page
from app.shapes import load_page
from app.scorekeeping import score