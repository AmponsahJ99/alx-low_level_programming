#include <stdlib.h>

/**
 *random – any random integer for the main function
 *@int: an integer picked for the operation
 *result: the parameter used to determine the result
 *return: return a value of 0
 */
int random_operation(int *result)
{
    int a = rand() % 222 - 111;
    int b = rand() % 222 - 111;

    *result = a + b;

    return 0;
}
