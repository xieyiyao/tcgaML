import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from pre_processing import pre_process, delete_low_variance

def run_model():
    p_val = [1, 2, 3]
    n_val = [3, 5]
    for n in n_val:
        for dist in p_val:
            x_train, x_test, y_train, y_test = pre_process()
            x_train, x_test = delete_low_variance(x_train, x_test)
            clf = KNeighborsClassifier(p = dist, n_neighbors = n)
            clf.fit(x_train, y_train.values.ravel())
            print "kNN: p =", dist, "neighbors =", n
            print "Score:", clf.score(x_test, y_test)

if __name__ == "__main__":
    run_model()
