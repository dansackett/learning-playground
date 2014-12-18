package main

import (
	"fmt"
)

func main() {
	// Slices are one of the most common data types in Go and used more than
	// arrays in most cases.

	// Slices can grow in size and are typed. We use the built-in make()
	// function to initialize them.
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// We can update index values of a slice
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// We can get the length
	fmt.Println("len:", len(s))

	// We can add new values to a slice with the append() function. Notice how
	// we assign the function result to the former variable
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// We can create an empty slice and then copy an existing slice into it
	// with the copy() function.
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Like Python, we can take a slice of a slice
	l := s[2:5]
	fmt.Println("sl1:", l)

	m := s[:5]
	fmt.Println("sl2:", m)

	n := s[2:]
	fmt.Println("sl3:", n)

	// We can also define a slice in one line
	t := []string{"g", "h", "i"}
	fmt.Println("dcl", t)

	// To make a multidimensional slice, we first define the multi slice. Then
	// if we want inner slices within, we make a new slice and assign to it.
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}
