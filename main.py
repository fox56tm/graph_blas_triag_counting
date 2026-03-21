import numpy as np

import time

import graphblas as gb

from src import algorithms as alg

import networkx as nx

from src import loader as ld

tests = ['karate']

def benchmarks():


    for name in tests:

        matrix = ld.getMatrix(name)

        t1Start = time.perf_counter()

        trCount1 = alg.naiveAlg(matrix)

        t1Res =  time.perf_counter() - t1Start




        t2Start = time.perf_counter()

        trCount2 = alg.burkhardAlg(matrix)

        t2Res =  time.perf_counter() - t2Start



        t3Start = time.perf_counter()

        trCount3 = alg.sandiaAlg(matrix)

        t3Res =  time.perf_counter() - t3Start


        print(trCount1, trCount2, trCount3,'\n')
        
        print(f"Naive {t1Res:.6f}", f"Burkhard {t2Res:.6f}",f"Sandia {t3Res:.6f}")

benchmarks()

