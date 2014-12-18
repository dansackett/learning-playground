package main

import (
	"fmt"
)

// Here we define a normal function to set a value to zero. It essentially
// does nothing..
func zeroval(ival int) {
	ival = 0
}

// Here define a function that takes a pointer and assigned that pointer value
// to 0. This will change things for us
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	// We define our variable
	i := 1
	fmt.Println("inital:", i)

	// Run it against the function that doesn't do anything
	zeroval(i)
	fmt.Println("zeroval:", i)

	// Run it against the pointer function. This works because we pass i by
	// reference and then our function acts on i in memory and alters it.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// We can see the memory location of i by reference
	fmt.Println("pointer:", &i)
}
