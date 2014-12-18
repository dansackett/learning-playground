package main

import (
	"fmt"
	"math"
)

// We can declare constants
const s string = "constant"

func main() {
	// And print them
	fmt.Println(s)

	// Constants can be declared anywhere a var statement can occur
	const n = 50000000

	// We can do arithmetic with arbitrary precision
	const d = 3e20 / n
	fmt.Println(d)

	// Numeric constants have no type until assigned type
	fmt.Println(int64(d))

	// Functions can automatically assign type to a constant for instance this
	// gets int64()
	fmt.Println(math.Sin(n))
}
