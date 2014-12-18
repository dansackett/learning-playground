package main

import "fmt"

func main() {
	fmt.Println("go" + "lang")        // Strings can be concatenated with a "+"
	fmt.Println("1+1 =", 1+1)         // Can combine output with a comma
	fmt.Println("7.0/3.0 =", 7.0/3.0) // Floats are described as you would expect
	fmt.Println(true && false)        // And
	fmt.Println(true || false)        // Or
	fmt.Println(!true)                // Negation
}
