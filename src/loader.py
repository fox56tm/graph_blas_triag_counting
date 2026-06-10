# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import graphblas as gb
import os
import algorithms as alg

DATA_DIR = "../data"
def get_matrix(matrix_name: str) -> gb.Matrix:
    matrix_path = os.path.join(DATA_DIR, f"{matrix_name}.mtx")
    if not os.path.exists(matrix_path):
        print("Matrix not found")
        return None
    try:
        matrix = gb.io.mmread(matrix_path)
        matrix = alg.preprocess_matrix(matrix)
        return matrix
    except Exception as ex:
        print(f"error read {ex}")
        return None
