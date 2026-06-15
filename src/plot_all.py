# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import scipy.stats as stats
import numpy as np

graphs = [
    "amazon0302",
    "amazon-2008",
    "cit-Patents",
    "roadNet-CA",
    "web-NotreDame",
    "web-Stanford",
]
algorithms = ["burkhard", "sandia"]

for graph in graphs:
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

    print(f"graph: {graph}\n")
    for i in range(0, 2):
        print(f"{algorithms[i]}-py normal test:  ", (stats.normaltest(data_py[i])))
    for i in range(0, 2):
        print(f"{algorithms[i]}-lagr normal test:", (stats.normaltest(data_lagr[i])))

    print("\n---Stats---")
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
        std_dev = np.std(d, ddof=1)
        relative_std = (std_dev / mean) * 100

        print(f"{label}:")
        print(f"  mean     = {mean:.6f}")
        print(f"  std dev  = {std_dev:.6f} ({relative_std:.2f}%)")
        print(f"  sem      = {sem:.6f}")
        print(f"  interval = {mean:.6f} ± {ci:.6f}")
        print("-" * 30)

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
