#final code

from flask import Flask, render_template, request 
import requests
import os
import json
# from IPython.display import Image,display
# import datetime

app = Flask(__name__)
# run_with_ngrok(app)

@app.route("/")
def home():
  return render_template('live.html')
# @app.route("/")
# def live_fix():
#   return render_template('live.html')

if __name__ == "__main__":
  app.run()