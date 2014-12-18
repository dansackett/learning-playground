package main

import (
	"fmt"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {
	// This is a typical synchronous function call
	f("direct")

	// Placing "go" before the function call will run it as a goroutine and
	// will have it act asynchronously
	go f("goroutine")

	// We can also run anonymous goroutines
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// By now, the gorountines are running in the background
	// fmt.Scanln() requires pressing a key to finish
	var input string
	fmt.Scanln(&input)
	fmt.Println("done")
}
