package main

import (
	"fmt"
)

// We define a recursive function that will multiply until we have 0 left
// which is the breakpoint
func fact(n int) int {
	if n == 0 {
		return 1
	}

	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))
}
