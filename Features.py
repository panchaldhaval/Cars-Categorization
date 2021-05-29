import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\dhaval.panchal\Pictures\cars_categorization\Training_CSV_File/Training_Data.csv",encoding= 'unicode_escape')

df.columns =[column.replace(" ", "_") for column in df.columns]

options =['climate_control','sunroof','petrol','cng','diesel']

for i in range(len(options)):
    print(str(i+1) + ":", options[i])

opt = int(input("Choose from the below options: "))
if opt in range(1, 7):
    opt = options[inp-1]
    if opt=='sunroof':
        df.query("roof == True", inplace = True)
        feature=df["car_model"]
        print(f'{feature}')
    if opt=='climate_control':
        df.query("climate_control == True", inplace = True)
        feature=df["car_model"]
        print(f'{feature}')
    if opt=='petrol':
        df.query("petrol == True", inplace = True)
        feature=df["car_model"]
        print(f'{feature}')
    if opt=='cng':
        df.query("cng == True", inplace = True)
        feature=df["car_model"]
        print(f'{feature}')
    if opt=='diesel':
        df.query("diesel == True", inplace = True)
        feature=df["car_model"]
        print(f'{feature}')

else:
    print("Choose from the above mentioned option")
