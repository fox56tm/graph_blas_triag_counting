# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev
import graphblas as gb
from src import algorithms as alg


def test_empty_graph():

    empty_matrix = gb.Matrix.from_coo([], [], [], nrows=10, ncols=10)
    expected = 0
    assert alg.naive_alg(empty_matrix) == expected
    assert alg.burkhard_alg(empty_matrix) == expected
    assert alg.sandia_alg(empty_matrix) == expected


def test_zero_triangle_graph():

    rows = [0, 1, 1, 2]
    cols = [1, 0, 2, 1]
    vals = [1, 1, 1, 1]
    A = gb.Matrix.from_coo(rows, cols, vals, nrows=3, ncols=3)
    expected = 0
    assert alg.sandia_alg(A) == expected
    assert alg.burkhard_alg(A) == expected
    assert alg.naive_alg(A) == expected


def test_graph_k3():

    rows = [0, 0, 1, 1, 2, 2]
    cols = [1, 2, 0, 2, 0, 1]
    vals = [1, 1, 1, 1, 1, 1]
    k3 = gb.Matrix.from_coo(rows, cols, vals, nrows=3, ncols=3)
    expected = 1
    assert alg.naive_alg(k3) == expected
    assert alg.burkhard_alg(k3) == expected
    assert alg.sandia_alg(k3) == expected
