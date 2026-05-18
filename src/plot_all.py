# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

graph = "web-NotreDame"
algorithms = ["burkhard", "sandia"]
algorithms2 = ["burkhard-py", "sandia-py","burkhard-lagr", "sandia-lagr"]
data_py = []
data_lagr = []
for algo in algorithms:
    with open(f"../results/bench-{graph}-{algo}.csv", "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        data_py.append(values)
for algo in algorithms:
    with open(f"../results/lagr-{graph}-{algo}.csv", "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        data_lagr.append(values)

#for i in range(0,2):
#     print(f"{algorithms[i]} normal test:",(stats.normaltest(data_py[i])))

#for i in range(0,2):
#     print(f"{algorithms[i]} normal test:",(stats.normaltest(data_lagr[i])))

print("burkhard py normal test:",(stats.normaltest(sorted(data_py[0])[:-1])))
#print("sandia py normal test:",(stats.normaltest(sorted(data_py[1][:-2]))))
print("sandia lagr normal test:",(stats.normaltest(sorted(data_lagr[0])[:-1])))
#all_data = [sorted(data_py[0])[:-1], sorted(data_py[1])[:-1], data_lagr[0], sorted(data_lagr[1])[:-1]]

all_data = [sorted(data_py[0])[:-1], sorted(data_py[1]), sorted(data_lagr[0])[:-1], sorted(data_lagr[1])]
bp = plt.boxplot(all_data, patch_artist=True)
colors = ['b', 'g','r','y']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.xticks([1, 2, 3, 4], algorithms2)
plt.ylabel('seconds')
plt.title(graph)
plt.show()
