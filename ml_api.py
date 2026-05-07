# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
#format that our api needs the data in
class model_input(BaseModel):
    age', 'sex', 'bmi', 'children', 'smoker', 'region']
    age : int
    sex : object
    bmi : float
    children : int
    smoker : object
    region : object
    
# loading the saved model 
insurance_model = pickle.load(open('insurance_model.sav', 'rb'))

@app.post('/insurance_prediction') 
def insurance_pred(input_parameters : model_input): # the values that the user will give
    input_data = input_parameters.json() # data will be posted in the form of json
    input_dictionary = json.loads(input_data) # then we have to convert that json to a dictionary 
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    bmi = input_dictionary['bmi']
    children = input_dictionary['children']
    smoker = input_dictionary['smoker']
    region = input_dictionary['region']

    
    input_list = [age, sex, bmi, children, smoker, region]
    
    prediction = insurance_model.predict([input_list])
    
    print('The insurance cost is USD ', prediction[0])"""
    
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class ModelInput(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region: int

insurance_model = pickle.load(open("insurance_model.sav", "rb"))

@app.get("/")
def home():
    return {"message": "Insurance API is running"}

@app.post("/insurance_prediction")
def insurance_pred(input_parameters: ModelInput):
    input_list = [
        input_parameters.age,
        input_parameters.sex,
        input_parameters.bmi,
        input_parameters.children,
        input_parameters.smoker,
        input_parameters.region
    ]

    prediction = insurance_model.predict([input_list])

    return {"predicted_insurance_cost": float(prediction[0])}