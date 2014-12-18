package main

import "fmt"

func main() {
	// When defining a variable, we name it and assign type
	var a string = "initial"
	fmt.Println(a)

	// We can assign multiple variables at once
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go infers type if you don't supply it
	var d = true
	fmt.Println(d)

	// We can initialize variables without assigning to them. Their value is 0.
	var e int
	fmt.Println(e)

	// We have short syntax for initializing which infers type
	f := "short"
	fmt.Println(f)
}
