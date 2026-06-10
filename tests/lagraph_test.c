// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Dmitry Sergeev
#include "../lagraph_bench/lagraph_utils.h"
#include <assert.h>

void createTestMatrix(const char* filename, const char* content)
{
    FILE* f = fopen(filename, "w");
    assert(f != NULL);
    fputs(content, f);
    fclose(f);
}

void testEmptyMatrixFile()
{
    char msg[LAGRAPH_MSG_LEN];
    LAGraph_Graph g = createMatrixForBench("non_exist_file.mtx", msg);
    assert(g == 0);
    printf("PASSED\n");
}

void testPreprocessMatrix()
{
    char msg[LAGRAPH_MSG_LEN];
    const char* filename = "test_matrix.mtx";
    const char* content = "%%MatrixMarket matrix coordinate pattern general\n"
                          "3 3 3\n"
                          "1 1\n"
                          "1 2\n"
                          "2 3\n";

    createTestMatrix(filename, content);
    LAGraph_Graph g = createMatrixForBench(filename, msg);
    assert(g != NULL);
    assert(g->nself_edges == 0);
    assert(g->kind == LAGraph_ADJACENCY_UNDIRECTED);

    uint64_t count = 0;
    LAGr_TriangleCount_Method method = LAGr_TriangleCount_Sandia_LL;
    LAGr_TriangleCount_Presort presort = LAGr_TriangleCount_AutoSort;
    int status = LAGr_TriangleCount(&count, g, &method, &presort, msg);
    assert(status == 0);
    assert(count == 0);

    LAGraph_Delete(&g, msg);
    remove(filename);
    printf("PASSED\n");
}

int main()
{
    char msg[LAGRAPH_MSG_LEN];
    LAGraph_Init(msg);
    printf("Tests:\n\n");
    testEmptyMatrixFile();
    testPreprocessMatrix();
    printf("\nTests finished\n");
    LAGraph_Finalize(msg);
    return 0;
}
