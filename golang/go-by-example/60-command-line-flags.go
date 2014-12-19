package main

import (
	"flag"
	"fmt"
)

func main() {
	// Using the flag package, we define a new flag "word" with a default of
	// "foo" and a description of "a string".
	wordPtr := flag.String("word", "foo", "a string")

	// We can also make flags for numbers and booleans
	numbPtr := flag.Int("numb", 42, "an int")
	boolPtr := flag.Bool("fork", false, "a bool")

	// @NOTE: All flags return pointers and not values

	// We can use an existing var in the program to create a flag as well
	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	// After we have our flags declared, we can parse them
	flag.Parse()

	// We dereference the pointers here to get the actual values
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("bool:", *boolPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}
