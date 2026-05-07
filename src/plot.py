# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

graph = "web-Google"
algorithms = ["burkhard", "sandia", "naive"]

data = []
for algo in algorithms:
    with open(f"results/lagr-bench-{graph}-{algo}.csv", "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        data.append(values)
    print(f"{algo} normal test:",(stats.normaltest(data[algo])))

bp = plt.boxplot(data, patch_artist=True)
colors = ['blue', 'green', 'red']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.xticks([1, 2, 3], algorithms)
plt.ylabel('seconds')
plt.title(graph)
plt.show()