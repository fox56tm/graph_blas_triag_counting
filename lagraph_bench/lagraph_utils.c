#include "lagraph_utils.h"

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg)
{
    FILE* f = fopen(fileName, "r");
    if (!f)
        return NULL;

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
    for (int i = 0; i < 30; i++) {
        LAGr_TriangleCount_Method m = method;
        LAGr_TriangleCount_Presort presort = LAGr_TriangleCount_AutoSort;
        struct timespec start, end;
        clock_gettime(CLOCK_MONOTONIC, &start);
        LAGr_TriangleCount(&count, g, &m, &presort, msg);
        clock_gettime(CLOCK_MONOTONIC, &end);
        double el = (double)(end.tv_sec - start.tv_sec) + (double)(end.tv_nsec - start.tv_nsec) / 1e9;
        fprintf(out, "%.16f\n", el);
    }
    printf("triles: %lu\n", count);
}
