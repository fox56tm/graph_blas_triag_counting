//SPDX-License-Identifier: MIT
//Copyright (c) 2026 Dmitry Sergeev
#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <suitesparse/GraphBLAS.h>
#include <suitesparse/LAGraph.h>
#include <time.h>
LAGraph_Graph createMatrixForBench(const char * fileName, char* msg)
{   
     FILE* newMatrix = fopen(fileName, "r");

    if (!newMatrix) return NULL;

    GrB_Matrix matrix = NULL; 

    GrB_Matrix matrixT = NULL; 

    GrB_Index n;

    LAGraph_MMRead(&matrix, newMatrix, msg);

    GrB_Matrix_nrows(&n, matrix);

    GrB_Matrix_new(&matrixT, GrB_BOOL, n, n);

    GrB_transpose(matrixT, NULL, NULL, matrix, NULL);

    GrB_eWiseAdd(matrix, NULL, NULL, GxB_PAIR_BOOL, matrix, matrixT, NULL);

    GrB_free(&matrixT);

    LAGraph_Graph G = NULL;

    LAGraph_New(&G, &matrix, LAGraph_ADJACENCY_UNDIRECTED, msg); 

    LAGraph_DeleteSelfEdges(G, msg);
    LAGraph_Cached_NSelfEdges(G, msg);
    LAGraph_Cached_OutDegree(G, msg);
    LAGraph_Cached_AT(G, msg);

    return G;

}
double lagraphBench(LAGraph_Graph G, LAGr_TriangleCount_Method method, int iter, int warmup, char* msg)
{ 
    uint64_t count = 0;

    double total = 0.0;

    for (int i = 0; i < warmup + iter; i++)
    {   
        LAGr_TriangleCount_Method method1 = method;

        LAGr_TriangleCount_Presort presort = LAGr_TriangleCount_AutoSort;

        struct timespec start, end;

        clock_gettime(CLOCK_MONOTONIC, &start);

        int res = LAGr_TriangleCount(&count, G, &method1, &presort, msg);

        clock_gettime(CLOCK_MONOTONIC, &end);

        total += (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
        
    }
    
    printf(" count: %lu, msg: %s\n", count, msg);

    return total;
}


int main()
{       
    char msg[LAGRAPH_MSG_LEN];

    LAGraph_Init (msg);

    LAGraph_Graph google = createMatrixForBench("data/web-Google.mtx", msg);
    

    double sandia = lagraphBench(google,  LAGr_TriangleCount_Sandia_LL, 30, 10, msg);

    printf("%.8f\n", sandia);

    LAGraph_Delete(&google, msg);
    LAGraph_Finalize(msg);

    

}