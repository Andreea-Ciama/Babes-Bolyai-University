cmake_minimum_required(VERSION 3.21)
project(dsa_lab1)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(dsa_lab1
        DynamicVector.cpp
        DynamicVector.h
        ExtendedTest.cpp
        ExtendedTest.h
        main.cpp
        Set.cpp
        Set.h
        SetIterator.cpp
        SetIterator.h
        ShortTest.cpp
        ShortTest.h)
