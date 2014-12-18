package main

import (
	"fmt"
)

// We define our struct
type rect struct {
	width, height int
}

// We define a method on our struct by pointer
func (r *rect) area() int {
	return r.width * r.height
}

// We can also define a method on our struct normally
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	// Initialize our object
	r := rect{width: 10, height: 5}

	// Go will automatically handle the conversion between reference and value
	// for us which is AWESOME. It may be best to use pointer syntax though to
	// avoid copying on method calls or to allow it to mutate the receiving
	// struct directly.
	fmt.Println("area: ", r.area())
	fmt.Println("perim: ", r.perim())

	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim: ", rp.perim())
}
