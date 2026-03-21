import graphblas as gb


def preprocessMatrix(matrix):

    B = matrix.ewise_add(matrix.T, gb.binary.plus).select('offdiag').new()

    return B.apply(gb.unary.one).new()

def  burkhardAlg(matrix):  

   C = matrix.mxm(matrix, gb.semiring.plus_times).new(mask=matrix.S)

   return C.reduce_scalar().value // 6


def sandiaAlg(matrix):

    L = matrix.select('tril').new()

    C = L.mxm(L, gb.semiring.plus_times).new(mask = L.S)

    return C.reduce_scalar(gb.monoid.plus).value

    
    

def naiveAlg(matrix):

    C = matrix.mxm(matrix, gb.semiring.plus_times).new()
    
    C << C.mxm(matrix, gb.semiring.plus_times).select("diag")

    return C.reduce_scalar().value // 6


