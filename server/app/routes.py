from flask import Flask, render_template, request, url_for, jsonify
from app import app
from io import BytesIO
from kittengroomer_email import KittenGroomerMail
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World  !"

@app.route('/sanitize/', methods=['POST'])
def sanitize():
    data = request.data
    t = KittenGroomerMail(data)
    m = t.process_mail()
    logs = []
    for att in t.final_attach:
        logs.append(att.log_details)
    return str(logs)