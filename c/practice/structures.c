/**
 * Structures are large variables which contain variables within them. They
 * are what makes up objects and classes in other languages.
 *
 * The can serialize data
 * All multiple arguments to be passed through a function in one variable
 * Can be used for data structures such as linked lists and trees.
 */
#include <stdio.h>

int main()
{
    struct point {
        int x;
        int y;
    };

    // We can use dot syntax to access struct variables
    struct point p;
    p.x = 10;
    p.y = 5;

    // Typedef allows us to define a struct and call it without specifying struct
    typedef struct {
        int x;
        int y;
    } my_struct;

    my_struct q;

    // Structs can store pointers to other items and even to other structs
    // In this example, we can use a string for the brand since it has pointer
    // char notation.
    typedef struct {
        char * brand;
        int model;
    } vehicle;

    vehicle car;
    car.brand = "Ford";
    car.model = 2014;

    return 0;
}
