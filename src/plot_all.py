# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

graph = "amazon0302"
algorithms = ["burkhard", "sandia"]
algorithms2 = ["burkhard-py", "sandia-py", "burkhard-lagr", "sandia-lagr"]
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

for i in range(0, 2):
    print(f"{algorithms[i]} normal test:", (stats.normaltest(data_py[i])))

for i in range(0, 2):
    print(f"{algorithms[i]} normal test:", (stats.normaltest(data_lagr[i])))

print("\n--- SEM ---")
all_labels = ["burkhard-py", "sandia-py", "burkhard-lagr", "sandia-lagr"]
all_datasets = [
    sorted(data_py[0]),
    sorted(data_py[1]),
    sorted(data_lagr[0]),
    sorted(data_lagr[1]),
]
for label, d in zip(all_labels, all_datasets):
    mean = np.mean(d)
    sem = stats.sem(d)
    ci = stats.t.ppf(0.975, df=len(d) - 1) * sem
    print(f"{label}: mean={mean:.6f}, sem={sem:.6f}, interval={mean:.6f} ± {ci:.6f}")

all_data = [
    sorted(data_py[0]),
    sorted(data_py[1]),
    sorted(data_lagr[0]),
    sorted(data_lagr[1]),
]
bp = plt.boxplot(all_data, patch_artist=True)
colors = ["b", "g", "r", "y"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
plt.xticks([1, 2, 3, 4], algorithms2)
plt.ylabel("seconds")
plt.title(graph)
plt.show()


# ======below code for 2 boxplots=======
# all_data_2 = [
#     sorted(data_py[1]),
#     sorted(data_lagr[1]),
# ]
# bp = plt.boxplot(all_data_2, patch_artist=True)
# colors = ["b", "g"]
# for patch, color in zip(bp["boxes"], colors):
#     patch.set_facecolor(color)
# selected_labels = [algorithms2[1], algorithms2[3]]
# plt.xticks([1, 2], selected_labels)
# plt.ylabel("seconds")
# plt.title(graph)
# plt.show()
