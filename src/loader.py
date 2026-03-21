
import graphblas as gb
import os
from src import algorithms as alg

DATA_DIR = 'data'

def getMatrix(matrixName):

    matrixPath = os.path.join(DATA_DIR, f"{matrixName}.mtx")
    

    if not os.path.exists(matrixPath):

        print("Matrix not found")

        return None


    try:
        matrix = gb.io.mmread(matrixPath)

        matrix = alg.preprocessMatrix(matrix)

        return matrix
        
    except Exception as ex:

        print(f"error read {ex}")
            
        return None




            
        
        

