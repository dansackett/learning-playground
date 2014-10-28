/**
 * Everything about C data types and variables.
 */
#include <stdio.h>

int main()
{
    // Integers: positvie or negative whole numbers
    char a = 1;
    int b = -2;
    short c = 3;
    long d = 4L;
    long long e = 5L;

    // Unsigned Integers: Positive whole numbers
    unsigned char f = 6;
    unsigned int g = 7;
    unsigned short h = 8;
    unsigned long i = 9L;
    unsigned long long j = 10L;

    // Floating Points: Real numbers (numbers with fractions)
    float k = 3.14;
    double l = 100.98;

    // Arrays: Used to store collections of same type data
    // We can set a max length on definition.
    int numbers[10];
    int more_numbers[] = {1, 2, 3, 4, 5};

    // Strings: Strings are essentially arrays of characters in C. We have two
    // ways of writing them. One with array syntax and one with pointer syntax.
    // All strings end with /0 as a null character.
    char my_string[] = "This is a string";
    char *my_other_string = "This is another string";
    // strncmp("Dan", "Dan", 3);

    // Structures:

    // C does not have a boolean type. We can define them though for ease.
    #define BOOL char
    #define FALSE 0
    #define TRUE 1

    // We can define variables without assigning them and they will hold a
    // place in memory to assign to later.
    int m;

    return 0;
}
