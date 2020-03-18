import matplotlib.pyplot as plt

Singers = ["Sidhu Moosewala", "Babbu Mann", "Karan Aujla", "Mankirat Aulakh", "Sharry Mann"]
Trending = [80, 70, 55, 50, 19]

plt.pie(Trending, labels=Singers)
plt.legend()
plt.show()