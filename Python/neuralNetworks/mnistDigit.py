from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
digits = load_digits()

print(digits.data[0,:])
#Scaling the data
X_Scale = StandardScaler()
X = X_Scale.fit_transform(digits.data)
print(X[0,:])

print(digits.data.shape)
import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[1])
plt.show()