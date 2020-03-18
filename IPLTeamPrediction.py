from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Initial Data
X = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
Y = [10, 7, 4, 7, 8, 8, 11, 3, 4, 7, 6, 6]

# Linear Regression : 1 Line of Code :)
data = stats.linregress(X, Y)
print(">> SLope is:", data[0])
print(">> Interceptor is:", data[1])
print(">> Equation of Line: y = {} + {} * x".format(data[1], data[0]))
# maxX = np.max(X) + 10
# minY = np.min(Y) - 10
#
# print("maxX:", maxX)
# print("minY:", minY)
#
# # Data Points for Linear Regression. Instead of 5, we got 100
# x = np.linspace(minY, maxX, 0)
# y = data[1] + data[0] * x
#
# print(x)
# print("----------")
# print(y)
#
plt.xlabel("Year")
plt.ylabel("Matches Won")
plt.grid(True)
plt.plot(X, Y, color="red", label="KINGS XI PUNJAB")
# plt.scatter(X, Y, color="blue", label="Data Points")
plt.legend()
plt.show()


# Model Creation
model = LinearRegressionModel()

# Model Training
model.fit(X, Y)

predictedOutput = model.predict(6)
print(">> Predicted Output for 6 is:", predictedOutput)
