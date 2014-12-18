package main

import (
	"fmt"
)

// We can specify multiple return values from a function with parens
func vals() (int, int) {
	return 3, 7
}

func main() {
	// We can assign multiple variables from the function return
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// If we don't care about a variable, we can use the underbar
	_, c := vals()
	fmt.Println(c)
}
