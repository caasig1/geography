from flask import Flask, render_template, send_file, request, jsonify, session
from app import app 
import json
import random

@app.route('/collect', methods=['POST'])
def collect():
    session['vals'] = request.json['locations']
    random.shuffle(session['vals'])
    session['to_find'] = session['vals'].pop()
    session['total_clicks'] = 0
    session['correct_clicks'] = 0
    return jsonify({'first': "Please click on " + str(session['to_find'])})

@app.route('/click', methods=['POST'])
def click():
    input_value = request.json['input_value']

    # This will be printed in the Flask server's console
    # print(f"Received input value from client: {input_value}")

    # Process the input_value as needed (e.g., perform calculations, database operations, etc.)
    if session['to_find'] == input_value:
        color = 'green'
        if session['vals']:
            next = session['vals'].pop()
        else:
            color = 'black'
            next = '1'
        session['to_find'] = next
        session['correct_clicks'] += 1
    else:
        color = 'red'
        next = session['to_find']
    session['total_clicks'] += 1
    p = "Accuracy: " + str(round(session['correct_clicks'] / session['total_clicks'] * 100, 2)) + "%"

    return jsonify({
                        'color' : color,
                        'next' : "Please click on " + next,
                        'percent' : p,
                        'total' : session['correct_clicks']
                    })