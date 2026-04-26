# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import graphblas as gb
import time
from typing import Callable
import algorithms as alg
import loader as ld

tests = "web-Google"
algorithm = Callable[[gb.Matrix], int]


def bench(algorithm: algorithm, matrix: gb.Matrix, name: str) -> None:
    results = [0.0] * 30
    triangles = 0
    for i in range(40):
        t3Start = time.perf_counter()
        trCount3 = algorithm(matrix)
        t3end = time.perf_counter()
        if i >= 10:
            results[i - 10] = t3end - t3Start
        triangles = trCount3
        # print(trCount3)
        # print("\n")
    with open(f"py-bench-{name}.csv", "w") as res:
        for i in results:
            res.write(f"{i}\n")
    print(f"ready: {name}! triangles:{triangles}")


matrix = ld.get_matrix(tests)
# bench(alg.naive_alg, matrix, "naive")
bench(alg.burkhard_alg, matrix, "burkhard")
# bench(alg.sandia_alg, matrix, "sandia")
