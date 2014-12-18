package main

import (
	"fmt"
)

// When we define a function, we define the types that we expect for the
// inputs and the return type that we expect.
func plus(a, b int) int {
	return a + b
}

func main() {
	// We can assign the function result to a variable and then use it in an
	// expression.
	res := plus(1, 2)
	fmt.Println("1 + 2 =", res)
}
