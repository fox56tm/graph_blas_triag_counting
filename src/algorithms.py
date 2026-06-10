# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import graphblas as gb

def preprocess_matrix(matrix: gb.Matrix) -> gb.Matrix:
    B = matrix.ewise_add(matrix.T, gb.binary.plus).select("offdiag").new()
    return B.apply(gb.unary.one).new()

def burkhard_alg(matrix: gb.Matrix) -> int:
    C = matrix.mxm(matrix, gb.semiring.plus_pair).new(mask=matrix.S)
    return (C.reduce_scalar(gb.monoid.plus).value or 0) // 6

def sandia_alg(matrix: gb.Matrix) -> int:
    L = matrix.select("tril").new()
    C = L.mxm(L, gb.semiring.plus_pair).new(mask=L.S)
    return C.reduce_scalar(gb.monoid.plus).value or 0

def naive_alg(matrix: gb.Matrix) -> int:
    C = matrix.mxm(matrix, gb.semiring.plus_times).new()
    C << C.mxm(matrix, gb.semiring.plus_times).select("diag")
    return (C.reduce_scalar(gb.monoid.plus).value or 0) // 6
