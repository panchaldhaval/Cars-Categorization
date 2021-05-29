import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error

from datetime import datetime, timedelta,date
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_predict
%matplotlib inline
from sklearn.metrics import classification_report,confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from __future__ import division
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.svm import SVC
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score, train_test_split
import pickle
import joblib

filename = r'C:\Users\dhaval.panchal\Pictures\cars_categorization\Specifications_Cars.csv'

dff = pd.read_csv(filename, encoding= 'unicode_escape')
dff.rename(columns={"": "cng"})
dff['class']='0'

for inde,i in enumerate(dff['car_model']):
    if int(dff['length'][inde]) < 4000  or (int(dff['total_seats'][inde]) < 5) :
        dff['class'][inde] = '1'
    if int(dff['length'][inde]) > 4000 or (int(dff['total_seats'][inde]) > 5):
        dff['class'][inde] = '2'

s  = dff['functionality'].str.replace("'",'').str.split(',').explode().to_frame()

cols = s['functionality'].drop_duplicates(keep='first').tolist()

df = pd.concat([dff, pd.crosstab(s.index, s["functionality"])[cols]], axis=1).replace(
    {1: True, 0: False}
)
print(df)
df2 = df.rename(columns={"": "cng"})
   
df2.to_csv(r"C:\Users\dhaval.panchal\Pictures\car-classification-main\car-classification-main\cars_classification\Training_CSV_File/Training_Data.csv")

conditions = [
    (dff['length'] < 4) & (dff['total_seats'] < 5),
    (dff['length'] > 4) and (dff['total_seats'] > 5),
    ]

values = ['1', '2']
dff['class']='0'
dff['class'] = np.select(conditions, values)

dff.head()

df2=pd.read_csv(r"C:\Users\dhaval.panchal\Pictures\cars_categorization\Training_CSV_File/Training_Data.csv",encoding= 'unicode_escape')

y= df2['class']
X=df2[df2.columns[3:]]
X=X.astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44)

models = []

models.append(("RF",RandomForestClassifier()))
models.append(("SVC",SVC()))
models.append(("KNN",KNeighborsClassifier()))

for name,model in models:
    kfold = KFold(n_splits=4, random_state=2)
    cv_result = cross_val_score(model,X_train,y_train, cv = kfold,scoring = "accuracy")
    print(name, cv_result)
    y_pred = cross_val_predict(model, X, y, cv=5)

    print(confusion_matrix(y, y_pred))
    print(accuracy_score(y, y_pred))
    
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred)


