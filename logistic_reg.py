import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from pre_processing import pre_process, delete_low_variance


def main():

    # preprocess includes: spliting and using standard scaler to transform

    x_train, x_test, y_train, y_test = pre_process()


    ### feature selection with low variance

    #print(x_train.shape)

    x_train, x_test = delete_low_variance(x_train, x_test) 

    #print(x_train.shape)
    #print(x_test.shape)  #this deleted 218 features
    strength = 1
    model = LogisticRegression(C=strength, penalty='l1', solver="saga", multi_class="multinomial")
    model.fit(x_train, y_train)
    print("Accuracy score for test is: %.6f" % model.score(x_test, y_test))




if __name__== "__main__":
    main()
