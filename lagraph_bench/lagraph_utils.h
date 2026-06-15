// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Dmitry Sergeev
#pragma once
#include <stdio.h>
#include <string.h>
#include <suitesparse/GraphBLAS.h>
#include <suitesparse/LAGraph.h>
#include <time.h>

LAGraph_Graph createMatrixForBench(const char* fileName, char* msg);
void lagraphBench(LAGraph_Graph g, LAGr_TriangleCount_Method method, FILE* out, char* msg);
