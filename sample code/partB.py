from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import pandas as pd 
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    data_path = "E:\\dataminingMATH5836-master\\abalone\\abalone.data"
    abalone = pd.read_csv(data_path)
    abalone.columns = ['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
    abalone['Age'] = abalone['Rings']+1.5
    feature_vars = ['Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight']
    X_train, X_test, Y_train, Y_test = train_test_split(abalone[feature_vars], abalone['Age'], test_size = 0.4, random_state=5)
    scaler = StandardScaler()
    # # Fit only to the training data
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    clf_sgd = MLPRegressor(solver='sgd', alpha=1e-5,hidden_layer_sizes=(4,200,200,4), max_iter=500,random_state=1)
    clf_adam = MLPRegressor(solver='adam', alpha=1e-5,hidden_layer_sizes=(4,200,200,4), max_iter=500,random_state=1)
    clf_sgd.fit(X_train,Y_train)
    clf_adam.fit(X_train,Y_train)

    plt.plot(clf_sgd.loss_curve_,label='SGD')
    plt.plot(clf_adam.loss_curve_,label='Adam')
    plt.show()
    train_pred = clf_sgd.predict(X_train)
    test_pred = clf_sgd.predict(X_test)
    MSE = np.square(np.subtract(Y_train,train_pred))
    
    RMSE = np.sqrt(MSE)
    plt.plot(range(0,len(RMSE)),RMSE)
    plt.show()
    print(RMSE)


