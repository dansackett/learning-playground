package main

import (
	"fmt"
	"sort"
)

func main() {
	// We can sort any type of built-ins. Sorts are done in place so they
	// don't return anything and instead update the slice.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:", ints)

	// We can check if a data type is sorted
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted:", s)
}
