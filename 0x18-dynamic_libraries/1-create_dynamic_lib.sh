#!/bin/bash
gcc -Wall -Wextra -Werror -pedantic -c -fPIC *.c
gcc -shared -c -o liball.so *.o
export LD__LIBRARY_PATH=. :$LD_LIBRARY_PATH
