import matplotlib.pyplot as plt

data_sizes = [10, 1666, 10000]
time_sec1 = [4, 85, 289] #время линейного поиска
time_sec2 = [12, 13, 8] #время бинарного поиска

plt.plot(data_sizes, time_sec1)
plt.plot(data_sizes, time_sec2)
plt.show()