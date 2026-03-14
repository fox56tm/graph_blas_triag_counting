import graphblas as gb

rows = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
cols = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0, 1]
val = [1] * len(rows)

A = gb.Matrix.from_coo(rows, cols, val)


def bukhartAlg(matrix):  # function is correct

    B = matrix.ewise_add(matrix.T, gb.binary.plus).apply(gb.unary.one).new()

    triag = B.select('tril').new()

    l =  triag.mxm(triag, gb.semiring.plus_times).new(mask = triag.S)

    summa = l.reduce_scalar(gb.monoid.plus).value

    if summa is None:
        return 0

    return summa


def sandiaAlg(matrix):

    B = matrix.ewise_add(matrix.T, gb.binary.plus).apply(gb.unary.one).new()

    L = B.select('tril').new()

    C = L.mxm(matrix, gb.semiring.plus_times).new(mask = L.S)

    summa = C.reduce_scalar(gb.monoid.plus).value

    if summa is None:
        return 0

    return summa

def nativeAlg(matrix):

    B = matrix.ewise_add(matrix.T, gb.binary.plus).apply(gb.unary.one).select('offdiag').new()

    newMatrix = B.mxm(B, gb.semiring.plus_times).new()

    newMatrix2 = newMatrix.mxm(B, gb.semiring.plus_times).select('diag').new()

    summa = newMatrix2.reduce_scalar(gb.monoid.plus).new().value

    if summa is None:
        return 0

    return int(summa) // 6


