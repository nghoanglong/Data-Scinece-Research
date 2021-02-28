import numpy as np
from sklearn import neighbors
from keras.datasets import mnist
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    # load file
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    # run model
    X_train_convert = X_train.reshape((X_train.shape[0], 
                                       X_train.shape[1]*X_train.shape[2]))
    X_test_convert = X_test.reshape((X_test.shape[0], 
                                     X_test.shape[1]*X_test.shape[2]))

    clf = neighbors.KNeighborsClassifier(n_neighbors=1, p=2)
    clf.fit(X_train_convert, Y_train)
    Y_pred = clf.predict(X_test_convert)

    # calculate accuracy
    print(f'accuracy = {accuracy_score(Y_test, Y_pred)}')
