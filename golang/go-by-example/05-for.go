package main

import (
	"fmt"
)

func main() {
	// We can define for loops with simply a comparison
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// We can define for loops traditionally
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// We can define for loops that act like while loops
	for {
		fmt.Println("loop")
		break
	}
}
