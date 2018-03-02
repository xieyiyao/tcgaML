from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from pre_processing import pre_process, delete_low_variance

def run_model():
    x_train, x_test, y_train, y_test = pre_process()
    #x_train, x_test = delete_low_variance(x_train, x_test)

    clf = RandomForestClassifier()
    clf.fit(x_train, y_train.values.ravel())
    y_pred = clf.predict(x_test)
    print "Weighted F-1 Score:", f1_score(y_test, y_pred, average="weighted")

if __name__ == "__main__":
    run_model()
