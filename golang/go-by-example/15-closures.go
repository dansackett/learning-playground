package main

import (
	"fmt"
)

// To create a closure, we state that we're returning a function and that
// function is returning an int
func intSeq() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}

func main() {
	// We can assign our returned function to a new variable
	nextInt := intSeq()

	// Caling our function keeps track of state
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// As we see, this is a different state since we define a new variable
	newInts := intSeq()
	fmt.Println(newInts())
}
