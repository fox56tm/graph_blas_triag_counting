// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Dmitry Sergeev
#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <string.h>
#include <suitesparse/GraphBLAS.h>
#include <suitesparse/LAGraph.h>
#include <time.h>

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg);
void lagraphBench(LAGraph_Graph g, LAGr_TriangleCount_Method method, FILE* out, char* msg);

int main(int argc, char* argv[])
{
    if (argc != 4) {
        printf("args error\n");
        return 1;
    }

    const char* graph_path  = argv[1];
    const char* algo_name   = argv[2];
    const char* output_path = argv[3];

    LAGr_TriangleCount_Method method;
    if (strcmp(algo_name, "burkhard") == 0) {
        method = LAGr_TriangleCount_Burkhardt;
    } else if (strcmp(algo_name, "sandia") == 0) {
        method = LAGr_TriangleCount_Sandia_LL;
    } else{
        printf("algo error\n");
        return 1;
    }

    char msg[LAGRAPH_MSG_LEN];
    LAGraph_Init(msg);
    LAGraph_Graph g = createMatrixForBench(graph_path, msg);

    FILE* out = fopen(output_path, "w");
    lagraphBench(g, method, out, msg);
    fclose(out);

    LAGraph_Delete(&g, msg);
    LAGraph_Finalize(msg);
    return 0;
}

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg)
{
    FILE* f = fopen(fileName, "r");
    if (!f) return NULL;

    GrB_Matrix matrix = NULL;
    GrB_Matrix matrixT = NULL;
    GrB_Index n;

    LAGraph_MMRead(&matrix, f, msg);
    fclose(f);

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

void lagraphBench(LAGraph_Graph g, LAGr_TriangleCount_Method method, FILE* out, char* msg)
{
    uint64_t count = 0;
    for(int i = 0; i < 30; i++){
        LAGr_TriangleCount_Method m = method;
        LAGr_TriangleCount_Presort presort = LAGr_TriangleCount_AutoSort;
        struct timespec start, end;
        clock_gettime(CLOCK_MONOTONIC, &start);
        LAGr_TriangleCount(&count, g, &m, &presort, msg);
        clock_gettime(CLOCK_MONOTONIC, &end);
        double el = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
        fprintf(out, "%.16f\n", el);
    }
    printf("triles: %lu\n", count);
}