cmake_minimum_required(VERSION 3.25)
project(example C)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

list(APPEND CMAKE_MODULE_PATH "/usr/local/lib/cmake/LAGraph")
list(APPEND CMAKE_MODULE_PATH "/usr/local/lib/cmake/GraphBLAS")

find_package(GraphBLAS REQUIRED)
find_package(LAGraph REQUIRED)

add_executable(main lagraph_bench/lagraph_bench.c)
target_link_libraries(main PRIVATE SuiteSparse::LAGraph SuiteSparse::GraphBLAS)