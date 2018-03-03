import pandas as pd
import numpy as np
from sklearn import tree
import subprocess

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import f1_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from pre_processing import pre_process, delete_low_variance

def visualize_tree(model, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        tree.export_graphviz(model, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

def main():

    # preprocess includes: spliting and using standard scaler to transform

    x_train, x_test, y_train, y_test = pre_process()


    ### feature selection with low variance

    #print(x_train.shape)

    x_train, x_test= delete_low_variance(x_train, x_test)

    #print(x_train.shape)
    #print(x_test.shape)  #this deleted 218 features
    criteria = 'entropy'
    model = DecisionTreeClassifier(criterion = criteria)
    model.fit(x_train,y_train)
    prediction = model.predict(x_test)

    #visualize_tree(model,features)

    #print('the criteria is: ' + criteria)
    #print('the mean accuracy is: %.10f' % model.score(x_test,y_test))
    #print("F-1 score(micro) for test is: %.10f " % f1_score(y_test,prediction,average= 'micro'))
    print("F-1 score(weighted) for test is: %.10f " % f1_score(y_test,prediction,average= 'weighted'))




if __name__== "__main__":
    main()
