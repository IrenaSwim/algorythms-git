import matplotlib.pyplot as plt

data_sizes = [100, 1000, 10000]
time_sec1 = [0.0001, 0.7, 6] #время пузырьковой сортировки
time_sec2 = [0.0004, 0.2, 2пше] #время сортировки выбором

plt.plot(data_sizes, time_sec1)
plt.plot(data_sizes, time_sec2)
plt.show()