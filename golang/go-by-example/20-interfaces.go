package main

import (
	"fmt"
	"math"
)

// We define our interface which requires structs to implement the methodset
type geometry interface {
	area() float64
	perim() float64
}

// We create out structs
type square struct {
	width, height float64
}

type circle struct {
	radius float64
}

// We assign the required methods to the square struct
func (s square) area() float64 {
	return s.width * s.height
}

func (s square) perim() float64 {
	return 2*s.width + 2*s.height
}

// We assign the required methods to the circle struct
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// We define a function which takes an interface. This allows us to pass in
// objects that implement the required interface methods.
func measure(g geometry) {
	fmt.Println("struct: ", g)
	fmt.Println("area: ", g.area())
	fmt.Println("perim: ", g.perim())
}

func main() {
	// Interfaces are a named collection of method signatures

	s := square{width: 3, height: 4}
	c := circle{radius: 5}

	measure(s)
	measure(c)
}
