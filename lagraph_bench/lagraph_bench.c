// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Dmitry Sergeev
#include "lagraph_utils.h"

int main(int argc, char* argv[])
{
    if (argc != 4) {
        printf("args error\n");
        return 1;
    }

    const char* graphPath = argv[1];
    const char* algoName = argv[2];
    const char* outputPath = argv[3];

    LAGr_TriangleCount_Method method;
    if (strcmp(algoName, "burkhard") == 0) {
        method = LAGr_TriangleCount_Burkhardt;
    } else if (strcmp(algoName, "sandia") == 0) {
        method = LAGr_TriangleCount_Sandia_LL;
    } else {
        printf("algo error\n");
        return 1;
    }

    char msg[LAGRAPH_MSG_LEN];
    LAGraph_Init(msg);
    LAGraph_Graph g = createMatrixForBench(graphPath, msg);

    FILE* out = fopen(outputPath, "w");
    lagraphBench(g, method, out, msg);
    fclose(out);

    LAGraph_Delete(&g, msg);
    LAGraph_Finalize(msg);
    return 0;
}
