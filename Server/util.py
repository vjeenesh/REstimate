# -*- coding: utf-8 -*-
import json
import pickle
import numpy as np

__model = None
__locations = None
__data_columns = None

def get_location_names():
    return __locations

def load_artifacts():
    global __model
    global __data_columns
    global __locations
    
    print('Loading artifacts...')
    
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['column_names']
        __locations = __data_columns[3:]
        
    with open('./artifacts/Bengaluru_re_pred_model.pickle', 'rb') as f:
        __model = pickle.load(f)
        
    print('Artifacts loaded Successfully!')

def predict_price(sqft, bath, bhk, location):
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    try:
        loc_idx = __data_columns.index(location.lower())
    except:
        loc_idx = -1
    
    if loc_idx >= 0:
        x[loc_idx] = 1
        
    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    load_artifacts()
    print(get_location_names())
    print(predict_price(3000, location='abbigere', bath=3, bhk=4))

