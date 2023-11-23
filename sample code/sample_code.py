import pandas as pd
import requests
from io import BytesIO
from zipfile import ZipFile
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler


def data_preprocess():
    pass

if __name__ == "__main__":
    url = "https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip"
    with ZipFile(BytesIO(requests.get(url).content), "r") as myzip:
        # print content of zip:
        # print(myzip.namelist())

        # print content of one of the file:
        with myzip.open("wdbc.data", "r") as f_in:
            data = pd.read_csv(f_in)
            # print(data.head())
    data.columns = ["ID","Diagnosis","radius1","texture1","perimeter1","area1","smoothness1","compactness1","concavity1","concave_points1","symmetry1","fractal_dimension1","radius2","texture2","perimeter2","area2","smoothness2","compactness2","concavity2","concave_points2","symmetry2","fractal_dimension2","radius3","texture3","perimeter3","area3","smoothness3","compactness3","concavity3","concave_points3","symmetry3","fractal_dimension3"]

    scaler = MinMaxScaler()
    feature_vars = ["radius1","texture1","perimeter1","area1","smoothness1","compactness1","concavity1","concave_points1","symmetry1","fractal_dimension1","radius2","texture2","perimeter2","area2","smoothness2","compactness2","concavity2","concave_points2","symmetry2","fractal_dimension2","radius3","texture3","perimeter3","area3","smoothness3","compactness3","concavity3","concave_points3","symmetry3","fractal_dimension3"]
    # # Fit only to the training data
    scaler.fit(data[feature_vars])
    data[feature_vars] = scaler.transform(data[feature_vars])

    print(data.head())
    # X_tr = scaler.transform(X_train)
    # X_test = scaler.transform(X_test)

    coder = preprocessing.OneHotEncoder()
    tranformered =  coder.fit_transform(data[['Diagnosis']])
    y = tranformered.toarray()
    print(y.shape)
    X = data[["radius1","texture1","perimeter1","area1","smoothness1","compactness1","concavity1","concave_points1","symmetry1","fractal_dimension1","radius2","texture2","perimeter2","area2","smoothness2","compactness2","concavity2","concave_points2","symmetry2","fractal_dimension2","radius3","texture3","perimeter3","area3","smoothness3","compactness3","concavity3","concave_points3","symmetry3","fractal_dimension3"]]
    # data['Diagnosis_M'] = y[[0]]
    # data['Diagnosis_M'] = y[[1]]
    data.to_csv("data.csv")
    sgd_classifier = MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(20, 100,100,40), learning_rate_init=0.0001,random_state=1)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.4, random_state=5)
    sgd_classifier.fit(X_train,Y_train)
    sgd_train_pred = sgd_classifier.predict(X_train)

    adam_classifier = MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(20, 100,100,40), learning_rate_init=0.0001,random_state=1)
    adam_classifier.fit(X_train,Y_train)

    

    # print(coder.categories_)
    # onehot = pd.get_dummies(data['Diagnosis'],prefix='Diagnosis')
    # data[onehot.columns] = onehot
    # print(data.columns)
    # print(data['Diagnosis_B'])

    # with ZipFile(BytesIO(requests.get(url).content), "r") as myzip:
    #     # print content of zip:
    #     # print(myzip.namelist())

    #     # print content of one of the file:
    #     with myzip.open("wdbc.names", "r") as f_in:
    #         names = f_in.read()
    #         print(names)
            # print(f_in.read())