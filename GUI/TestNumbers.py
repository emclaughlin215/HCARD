import numpy as np

points = 100
X = range(0, points)
Y = np.exp2(X)

# X2 = np.add(100, X)
X2 = range(0, 100)

Y2 = np.multiply(X2, 2)
Y3 = np.multiply(X2, 3)
YT = []
YT.append(Y3)
YT.append(Y2)
print YT