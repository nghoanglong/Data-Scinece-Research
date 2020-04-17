import numpy as np
from matplotlib import pyplot as plt

#Bài toán sự đoán cân nặng với data có sẵn

# height (cm)
# giả lập dữ liệu chiều cao
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

# weight (kg)
# giả lập dữ liệu cân nặng
y = np.array([[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# Building Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

# Calculating weights of the fitting line
# Dựa theo đạo hàm của hàm mất mát L(w)
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)  # giả nghịch đảo
w_0 = w[0][0]
w_1 = w[1][0]
print('w = ', w)

def visual_data():
    #visualize data
    plt.plot(X, y, 'ro') #các điểm dữ liệu
    plt.axis([140, 190, 45, 75])
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')

    x0 = np.linspace(145, 185, 2) #thanh x0 nằm trong khoảng 145 <= x <= 185
    y0 = w_0 + w_1*x0

    # Drawing the fitting line
    plt.plot(X.T, y.T, 'ro') #data
    plt.plot(x0, y0)# the fitting line
    plt.axis([140, 190, 45, 75])
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.savefig('bieudo')
    plt.show()


def predict_weight(height):
    y1 = w_1*height + w_0
    print(f'Predict weight of person with {height} cm: %.2f (kg)' %(y1))


def main():
    height = int(input('Nhap chieu cao de du doan can nang: '))
    visual_data()
    predict_weight(height)

main()

