import numpy as np
from matplotlib import pyplot as plt

#khởi tạo
def init():
    X = np.random.rand(1000, 1) #trục x
    y = 4 + 3 * X + .2*np.random.randn(1000, 1) #trục y

    plt.scatter(X.T, y.T, s=5, c='#20A4F3')
    plt.xlabel('Data')
    plt.ylabel('Value')
    plt.show()

init()