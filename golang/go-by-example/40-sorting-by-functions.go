package main

import (
	"fmt"
	"sort"
)

// In order to do a custom sorting function, we have to first define a type
type ByLength []string

// Our sort interface requires that we implement the following functions. Len,
// Less, and Swap. The Len() function is common across type.
func (s ByLength) Len() int {
	return len(s)
}

// The Swap() function provides a way to change value order.
func (s ByLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

// The Less() function is the custom function which allows us to make the
// comparison we want to make. In this case, length.
func (s ByLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

func main() {
	// When we want to do custom sorting in Go, we can write a sort function.

	fruits := []string{"peach", "banana", "kiwi"}

	// We state the sort function inside our Sort() call and the magic happens.
	sort.Sort(ByLength(fruits))
	fmt.Println(fruits)
}
