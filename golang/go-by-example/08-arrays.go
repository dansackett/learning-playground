package main

import (
	"fmt"
)

func main() {
	// We initialize an array of size 5 with all values 0 like so
	var a [5]int
	fmt.Println("emp:", a)

	// We can set values in this array by index
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// As well, we can get the length of the array
	fmt.Println("len:", len(a))

	// We can define the values of an array like so
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// We can define a multiple dimension array like so
	var twoD [2][3]int

	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}

	fmt.Println("2d:", twoD)
}
