import pyodbc
import pandas as pd
import numpy as np
from flask import Flask,jsonify
from flask_cors import CORS
import connect
import Filters.headerfilters as hdr 
import Details.bodydetails as bdy
c = connect.connect()
Store_Name_df = hdr.storeName()
Store_Code_df = hdr.storeCode()
group_df = hdr.groupTable()
body_df = bdy.bodyView()

print(group_df)

# print(group_df['Name'].unique)

# print(body_df[body_df['Name']=='Centerpoint Nakheel Mall'])

app = Flask(__name__)
CORS(app)
@app.route('/get_names')
def get_names():
    names = group_df['Name'].unique().tolist()
    return jsonify(names)

@app.route('/get_code')
def get_codes():
    codes = [code for code in group_df['siteid'].unique().tolist() if not np.isnan(code)]
    float_codes = [code for code in codes if isinstance(code, float)]
    return jsonify(float_codes)

@app.route('/get_ip')
def get_ip():
    ip = group_df['description'].unique().tolist()
    return jsonify(ip)

@app.route('/get_mac')
def get_mac():
    mac = group_df['MAC Address'].unique().tolist()
    return jsonify(mac)

@app.route('/get_filtered_table')
def get_filtered():
    filtered = body_df.to_json(orient='records')
    return filtered
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
