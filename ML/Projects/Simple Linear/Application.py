from flask import Flask , request , jsonify , render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

application=Flask(__name__)
app=application

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")
lasso_model_path=os.path.join(BASE_DIR, "model_ls.pkl")

Normal_Model = joblib.load(model_path)

@app.route("/")
def Home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")