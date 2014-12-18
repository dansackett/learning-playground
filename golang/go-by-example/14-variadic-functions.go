package main

import (
	"fmt"
)

// We can define a function that takes any number of variables and name them.
// We use the ellipsis and the expected type.
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {
	// Since our function can take any number of arguments, both of these work
	sum(1, 2)
	sum(1, 2, 3)

	// We can create a slice and then pass all values of our slice to the
	// function also using the ellipsis
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
