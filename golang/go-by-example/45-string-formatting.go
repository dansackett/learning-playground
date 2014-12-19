package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
	p := point{1, 2}

	// This will print the struct instance
	fmt.Printf("%v\n", p)

	// This will print the struct instance plus the field names
	fmt.Printf("%+v\n", p)

	// This prints the go source code statement
	fmt.Printf("%#v\n", p)

	// Print the type
	fmt.Printf("%T\n", p)

	// Print a boolean
	fmt.Printf("%t\n", true)

	// Print the number repr
	fmt.Printf("%d\n", 123)

	// Print the binary repr
	fmt.Printf("%b\n", 14)

	// Print the char repr
	fmt.Printf("%c\n", 33)

	// Print the hex repr
	fmt.Printf("%x\n", 456)

	// Print the float repr
	fmt.Printf("%f\n", 78.9)

	// Print the sci notation 1 repr
	fmt.Printf("%e\n", 123400000.0)

	// Print the sci notation 2 repr
	fmt.Printf("%E\n", 123400000.0)

	// Print the string repr
	fmt.Printf("%s\n", "\"string\"")

	// Print the string double quoted repr
	fmt.Printf("%q\n", "\"string\"")

	// Print the string hex repr
	fmt.Printf("%x\n", "hex this")

	// Print the pointer memory address
	fmt.Printf("%p\n", &p)

	// Format the output
	fmt.Printf("|%6d|%6d|\n", 12, 345)

	// Format the float output
	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)

	// Format the float output left justified
	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// Format the output right justified
	fmt.Printf("|%6s|%6s|\n", "foo", "b")

	// Format the output left justified
	fmt.Printf("|%-6s|%-6s|\n", "foo", "b")

	// Format a sentence
	s := fmt.Sprintf("a %s", "string")
	fmt.Println(s)

	// Print to stderr
	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}
