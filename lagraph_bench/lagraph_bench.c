// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Dmitry Sergeev
#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <suitesparse/GraphBLAS.h>
#include <suitesparse/LAGraph.h>
#include <time.h>

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg);
void lagraphBench(LAGraph_Graph g, LAGr_TriangleCount_Method method, int iter, int warmup, char* msg, double* testArr);

int main()
{
    double testSandia[30];
    char msg[LAGRAPH_MSG_LEN];
    LAGraph_Init(msg);
    LAGraph_Graph google = createMatrixForBench("data/web-Google.mtx", msg);
    lagraphBench(google, LAGr_TriangleCount_Burkhardt, 30, 10, msg, testSandia);
    for (int i = 0; i < 30; i++)
        printf("%.9f ", testSandia[i]);

    LAGraph_Delete(&google, msg);
    LAGraph_Finalize(msg);
    FILE* testOut = fopen("src/test-res-lagr-burkhard.csv", "w");

    if (!testOut) {
        printf("file error");
        return 1;
    }
    for (int i = 0; i < 30; i++) {
        fprintf(testOut, "%.16lf\n", testSandia[i]);
    }
    fclose(testOut);
}

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg)
{
    FILE* newMatrix = fopen(fileName, "r");
    if (!newMatrix)
        return NULL;

    GrB_Matrix matrix = NULL;
    GrB_Matrix matrixT = NULL;
    GrB_Index n;
    LAGraph_MMRead(&matrix, newMatrix, msg);
    GrB_Matrix_nrows(&n, matrix);
    GrB_Matrix_new(&matrixT, GrB_BOOL, n, n);
    GrB_transpose(matrixT, NULL, NULL, matrix, NULL);
    GrB_eWiseAdd(matrix, NULL, NULL, GxB_PAIR_BOOL, matrix, matrixT, NULL);
    GrB_free(&matrixT);
    LAGraph_Graph g = NULL;
    LAGraph_New(&g, &matrix, LAGraph_ADJACENCY_UNDIRECTED, msg);
    LAGraph_DeleteSelfEdges(g, msg);
    LAGraph_Cached_NSelfEdges(g, msg);
    LAGraph_Cached_OutDegree(g, msg);
    LAGraph_Cached_AT(g, msg);

    return g;
}

void lagraphBench(LAGraph_Graph g, LAGr_TriangleCount_Method method, int iter, int warmup, char* msg, double* testArr)
{
    uint64_t count = 0;
    double total = 0.0;
    for (int i = 0; i < warmup + iter; i++) {
        LAGr_TriangleCount_Method method1 = method;
        LAGr_TriangleCount_Presort presort = LAGr_TriangleCount_AutoSort;
        struct timespec start, end;
        clock_gettime(CLOCK_MONOTONIC, &start);
        int res = LAGr_TriangleCount(&count, g, &method1, &presort, msg);
        clock_gettime(CLOCK_MONOTONIC, &end);
        if (i >= warmup) {
            total = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
            testArr[i - warmup] = total;
        }
    }
    printf(" count: %lu, msg: %s\n", count, msg);

}