package main

import (
	"fmt"
)

func main() {
	// Maps are just like Python dictionaries and hashes

	// We can define a map with the make() function and it takes the form
	// map[KEY TYPE]VALUE TYPE
	m := make(map[string]int)

	// We can assign keys and values
	m["k1"] = 7
	m["k2"] = 13
	fmt.Println("map:", m)

	// We can get a value
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// We can see the length
	fmt.Println("len:", len(m))

	// We can remove an item based on the key
	delete(m, "k2")
	fmt.Println("map:", m)

	// A good pattern when getting a key is multiple assignment where the
	// second variable to be assigned is a boolean stating whether the key
	// exists
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// We can define a map in one line like other data types
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}
