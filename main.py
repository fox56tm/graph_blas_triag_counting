# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev


import time


from src import algorithms as alg


from src import loader as ld

tests = ["karate"]


def benchmarks() -> None:

    for name in tests:

        matrix = ld.get_matrix(name)

        t1Start = time.perf_counter()

        trCount1 = alg.naive_alg(matrix)

        t1Res = time.perf_counter() - t1Start

        t2Start = time.perf_counter()

        trCount2 = alg.burkhard_alg(matrix)

        t2Res = time.perf_counter() - t2Start

        t3Start = time.perf_counter()

        trCount3 = alg.sandia_alg(matrix)

        t3Res = time.perf_counter() - t3Start

        print(trCount1, trCount2, trCount3, "\n")

        print(f"Naive {t1Res:.6f}", f"Burkhard {t2Res:.6f}", f"Sandia {t3Res:.6f}")


benchmarks()
