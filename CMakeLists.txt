cmake_minimum_required(VERSION 3.25)
project(example C)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_definitions(-D_POSIX_C_SOURCE=199309L)

find_package(GraphBLAS REQUIRED)
find_package(LAGraph REQUIRED)

add_executable(main lagraph_bench/lagraph_bench.c)
target_link_libraries(main PRIVATE SuiteSparse::LAGraph GraphBLAS::GraphBLAS)
