import matplotlib.pyplot as plt

"""
    Y = f(X)
    X: 1, Y: 1
    X: 2, Y: 2
    X: 3, Y: 3
"""

"""
# X axis will be indexes :)
Y = [0, 1, 2, 3, 4, 5]
plt.plot(Y)
plt.show()
"""

X = list(range(1, 11))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

# Labels will be shown on Legend
plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")

plt.grid(True)

# Put X and Y Limits
plt.xlim(0, 100)
plt.ylim(0, 100)

# Save the Graph
# plt.savefig("MyGraph")

plt.show()
