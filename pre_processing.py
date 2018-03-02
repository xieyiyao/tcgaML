import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler

def pre_process():
    df = pd.read_csv('tcga_data.csv',sep = ',')

    y = df.iloc[:,1:2] #since first column contains indices
    x = df.iloc[:,2:]

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train, x_test = scaler.transform(x_train), scaler.transform(x_test)

    return (x_train,x_test,y_train,y_test)

def delete_low_variance(x_train, x_test):
    low_var = VarianceThreshold(threshold = 0.1)
    low_var.fit(x_train)
    x_train, x_test = low_var.transform(x_train), low_var.transform(x_test)
    return (x_train, x_test)

if __name__ == "__main__":
    pre_process()
