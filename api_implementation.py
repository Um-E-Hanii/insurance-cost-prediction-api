# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:17:30 2026

@author: sahal
"""

import json 
import requests 

url = 'http://127.0.0.1:8000/insurance_prediction'


input_data_for_model = { 
    'age' : 18,
    'sex' : 0,
    'bmi' : 33.77,
    'children' : 1,
    'smoker' : 1,
    'region' : 0
    }

input_json = json.dumps(input_data_for_model)
response = requests.post(url, json=input_data_for_model)
print(response.text) 