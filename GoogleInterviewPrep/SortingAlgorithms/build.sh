#!/bin/bash
if [ "$1" = "all" ]; then
    gcc SelectionSort.cpp -lstdc++ -o SelectionSort.o
    gcc BubbleSort.cpp -lstdc++ -o BubbleSort.o
    gcc InsertionSort.cpp -lstdc++ -o InsertionSort.o
elif [ "$1" = "clean" ]; then
    rm *.o
else
    gcc $1.cpp -lstdc++ -o $1.o
fi
