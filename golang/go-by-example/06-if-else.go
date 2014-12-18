package main

import (
	"fmt"
)

func main() {
	// We can do standard if/else statements
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// Bare if statement
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// If, else, else if statement where we assign the variable in the check
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}
