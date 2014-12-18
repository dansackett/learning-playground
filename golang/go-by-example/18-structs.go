package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
}

func main() {
	// structs allow us to build a class-like object with defined attrs

	// We can create a new struct with regular ordered args
	fmt.Println(person{"Bob", 20})

	// We can create a new struct with keyword args
	fmt.Println(person{name: "Alice", age: 30})

	// Any args not defined are set to 0
	fmt.Println(person{name: "Fred"})

	// Using &struct yields a pointer to the struct
	fmt.Println(&person{name: "Anne", age: 40})

	// We can access struct attrs with dot notation
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// We can also use dot notation with struct pointers and the pointers are
	// automatically dereferenced
	sp := &s
	fmt.Println(sp.age)

	// Structs are mutable
	sp.age = 51
	fmt.Println(sp.age)
}
