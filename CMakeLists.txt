cmake_minimum_required(VERSION 3.25)
project(example C)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_definitions(-D_POSIX_C_SOURCE=199309L)

find_package(GraphBLAS REQUIRED)
find_package(LAGraph REQUIRED)

enable_testing()
add_executable(tests tests/lagraph_test.c lagraph_bench/lagraph_utils.c)
add_executable(main lagraph_bench/lagraph_bench.c lagraph_bench/lagraph_utils.c)

target_link_libraries(tests PRIVATE SuiteSparse::LAGraph GraphBLAS::GraphBLAS)
target_link_libraries(main PRIVATE SuiteSparse::LAGraph GraphBLAS::GraphBLAS)
add_test(NAME run_tests COMMAND tests)
