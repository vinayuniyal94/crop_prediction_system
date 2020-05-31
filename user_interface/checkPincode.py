import pandas as pd
import numpy as np

from ML.final_crop import getData

df = pd.read_csv("static/data_set/pin.csv").drop(
    ['Unnamed: 0'], axis=1
)


#for getting the district
def getdistrict(p):
    dist = df.Districtname.loc[df['Pincode'] == p]
    return str(dist)



#taking th values in a array for further processing
pin = pd.array(df['Pincode'])

#fucntion to check the user entered pincode is valid or not
def check(p, context):
    if p in pin:
        x = getData(context)
        return {"boo":True, "re":x}
    return False
