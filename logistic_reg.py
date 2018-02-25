import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from pre_processing import pre_process


def main():
    #import data

    
    #df.dropna(axis=1, how='any')
    #df = normalize(df)
    
    #print(df.iloc[:,2:3])
    #print(np.isfinite((df.iloc[:,2:3])).all())

    #low_var = VarianceThreshold(threshold = 0.1)
    #low_var.transform(x_train)
    #low_var.transform(x_test)
    
    #print(x_train)
    #print(np.isnan(x).all())
    #print(np.isfinite(x.any()))
    
    x_train, x_test, y_train, y_test = pre_process()
    
    print x_train
    
                                                                 

if __name__== "__main__":
    main()
