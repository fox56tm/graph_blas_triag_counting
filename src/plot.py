# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import matplotlib.pyplot as plt
from scipy import stats

name = "burkhard"
data = [[], [], []]
lagr_data = []
with open(f"py-bench-{name}.csv", "r") as f1:
    data[0] = [float(line.strip()) for line in f1 if line.strip()]

with open(f"test-res-lagr-{name}.csv", "r") as f1:
    lagr_data = [float(line.strip()) for line in f1 if line.strip()]

plt.hist(data[0])
print(stats.normaltest(data[0]))
# vs_lagr_data = [lagr_data, data[0]] // boxplots
# colors = ['b', 'g','r']
# bp = plt.boxplot(vs_lagr_data, patch_artist=True)
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)
# plt.xticks([1, 2], [f"lagr_{name}", f"python_{name}"])
# plt.ylabel('seconds')

plt.show()
