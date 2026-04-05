# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev


import time


import algorithms as alg


import loader as ld

tests = ["web-Google"]


def benchmarks() -> None:

    for name in tests:
        matrix = ld.get_matrix(name)

        # t1Start = time.perf_counter()

        # trCount1 = alg.naive_alg(matrix)

        # t1Res = time.perf_counter() - t1Start

        # t2Start = time.perf_counter()

        # trCount2 = alg.burkhard_alg(matrix)

        # t2Res = time.perf_counter() - t2Start
        total = 0.0
        for i in range (40):
        
            t3Start = time.perf_counter()

            trCount3 = alg.sandia_alg(matrix)

            t3end = time.perf_counter()
            
            if i >= 10:
                total += (t3end - t3Start)

        print(trCount3)
        print("\n")
        print(f"total: {total:.8}\n")
        # print(f"matrix {name}:\n")

        # print(trCount1, trCount2, trCount3, "\n")

        # print(f"Naive {t1Res:.6f}", f"Burkhard {t2Res:.6f}", f"Sandia {t3Res:.6f}")
        # print("\n")
        


benchmarks()
