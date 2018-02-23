import pandas as pd

CANCER_TYPES = {"Breast Invasive Carcinoma": 1,
    "Kidney Renal Clear Cell Carcinoma": 2, "Lung Adenocarcinoma": 3,
    "Lung Squamous Cell Carcinoma": 4, "Pancreatic Adenocarcinoma": 5,
    "Uveal Melanoma": 6}

def check_data():
    features = []
    filename = "data/Breast Invasive Carcinoma/0a2a3cf2-8c9e-4d2a-9da3-7e04ffb1a032/d243560f-fec1-4803-b704-dde9f10f7aa2.mirbase21.mirnas.quantification.txt"
    with open(filename, 'r') as initial_file:
        line = initial_file.readline()
        line = initial_file.readline().split()
        while line:
            features.append(line[0])
            line = initial_file.readline().split()

    for cancer_type in CANCER_TYPES.keys():
        print cancer_type + ":",
        if has_same_features(cancer_type, features) == False:
            print "MISMATCH"
        else:
            print "GOOD"

def has_same_features(cancer_type, features):
    filename = "data/" + cancer_type + "/manifest.txt"
    patients = []

    with open(filename, 'r') as in_file:
        line = in_file.readline()
        line = in_file.readline().split()
        while line and line[0] != "\N":
            patients.append(line[1])
            line = in_file.readline().split()

    for patient in patients:
        p_features = []
        filename = "data/" + cancer_type + "/" + patient
        with open(filename, 'r') as patient_file:
            line = patient_file.readline()
            line = patient_file.readline().split()
            while line:
                p_features.append(line[0])
                line = patient_file.readline().split()
        if p_features != features:
            return False

    return True

def build_dataset():
    data_dict_list = []

    for cancer_type in CANCER_TYPES.keys():
        filename = "data/" + cancer_type + "/manifest.txt"
        patients = []

        with open(filename, 'r') as in_file:
            line = in_file.readline()
            line = in_file.readline().split()
            while line and line[0] != "\N":
                patients.append(line[1])
                line = in_file.readline().split()

        for patient in patients:
            filename = "data/" + cancer_type + "/" + patient
            feature_dict = {}

            with open(filename, 'r') as p_file:
                line = p_file.readline()
                line = p_file.readline().split()
                while line:
                    feature_dict[line[0]] = line[2]
                    line = p_file.readline().split()

            feature_dict["Cancer Type"] = CANCER_TYPES[cancer_type]
            data_dict_list.append(feature_dict)

    return pd.DataFrame(data_dict_list)

if __name__ == "__main__":
    #check_data()
    df = build_dataset()
    print df
