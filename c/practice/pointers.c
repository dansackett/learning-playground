/**
 * Pointers, syntax, and how they work.
 */
#include <stdio.h>

int main()
{
    // Pointers simply reference a place in memory. In this instance, the
    // pointer ip references the memory location of var.
    int var = 20;
    int *ip = &var;

    printf("Address of my variable 'var': %p\n", &var);
    printf("Address of my pointer to 'var': %p\n", ip);
    printf("Value of 'var': %d\n", var);
    printf("Value of my pointer to 'var': %d\n", *ip);

    // Strings in C work by pointers.
    char *name = "Dan";
    // This allocates a local variable called "name" which is a pointer to
    // single character. It also pointsto the "D" character or the start of
    // the string which is where it resides at.
    printf("\nThis should print 'D': %c\n", name[0]);

    // Pointers can be dereferenced which is showing where the pointer points
    // to. We do that with an asterix like we do for referencing it.
    int a = 1;
    int *pointer_to_a = &a;

    printf("The value of a is: %d\n", a);
    printf("The value of pointer_to_a is: %d\n", *pointer_to_a);

    return 0;
}
