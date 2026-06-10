# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import time
import sys
import algorithms as alg
import loader as ld

graph_name = sys.argv[1]
algo_name = sys.argv[2]

matrix = ld.get_matrix(graph_name)
if algo_name == "burkhard":
    algorithm = alg.burkhard_alg
elif algo_name == "sandia":
    algorithm = alg.sandia_alg
else:
    algorithm = alg.naive_alg

results = []
for i in range(45):
    t_start = time.perf_counter()
    algorithm(matrix)
    t_end = time.perf_counter()
    if i >= 15:
        results.append(t_end - t_start)

for r in results:
    print(r)
