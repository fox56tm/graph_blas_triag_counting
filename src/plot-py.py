# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

graph = "web-Stanford"
algorithms = ["naive", "burkhard", "sandia"]

data = []
for algo in algorithms:
    with open(f"../results/bench-{graph}-{algo}.csv", "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        data.append(values)

for i in range(0,3):
     print(f"{algorithms[i]} normal test:",(stats.normaltest(data[i])))

# print("naive normal test:",(stats.normaltest(sorted(data[2])[:-1])))
# print("bur normal test:",(stats.normaltest(sorted(data[1])[:-1])))
bp = plt.boxplot(data, patch_artist=True)
colors = ['b', 'g','r']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.xticks([1, 2,3], algorithms)
plt.ylabel('seconds')
plt.title(graph)
plt.show()