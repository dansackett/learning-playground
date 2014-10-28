/**
 * We can pass arguments to funtions by reference rather than copying them by
 * value. It gives control to functions and structures.
 */
#include <stdio.h>

int n;

typedef struct {
    int x;
    int y;
} point;

void addOne(int n)
{
    n++;
}

void addOneByReference(int *n)
{
    (*n)++;
}

// We can use pointers to structs and use special syntax to adit properties
void structFunc(point *p)
{
    p->x++;
    p->y++;
}

int main()
{
    printf("Before: %d\n", n);
    addOne(n);
    printf("After: %d\n", n);

    printf("Before: %d\n", n);
    addOneByReference(&n);
    printf("After: %d\n", n);

    point p;
    p.x = 9;
    p.y = 10;
    printf("My struct params x: %d, y: %d\n", p.x, p.y);
    structFunc(&p);
    printf("My struct params after passing by pointer x: %d, y: %d\n", p.x, p.y);

    return 0;
}
