cmake_minimum_required(VERSION 3.25)
project(example C)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_definitions(-D_POSIX_C_SOURCE=199309L)
set(GRAPHBLAS_PATH "/usr/local/lib/libgraphblas.so")
set(LAGRAPH_PATH "/usr/local/lib/liblagraph.so")
include_directories(/usr/local/include/suitesparse)

add_executable(main lagraph_bench/lagraph_bench.c)
target_link_libraries(main PRIVATE ${GRAPHBLAS_PATH} ${LAGRAPH_PATH})