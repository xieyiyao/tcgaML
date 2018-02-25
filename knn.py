import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from pre_processing import pre_process, delete_low_variance

def run_model():
    x_train, x_test, y_train, y_test = pre_process()
    x_train, x_test = delete_low_variance(x_train, x_test)

    p_val = 3
    n_val = 5
    clf = KNeighborsClassifier(p = p_val, n_neighbors = n_val)
    clf.fit(x_train, y_train.values.ravel())
    print "p =", p_val, "neighbors =", n_val
    print "Score:", clf.score(x_test, y_test)

if __name__ == "__main__":
    run_model()
