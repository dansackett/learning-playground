package main

import (
	"fmt"
)

func main() {
	// range is an iterator basically

	// We can iterate over a slice using range rather than a traditional for
	// loop. range simply has the length and values baked in.
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// We can get the index and value if we wish
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// When looping over a map, we can get keys and values with range
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// We can also loop over strings where this will give us Unicode code
	// points in Bytes.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
