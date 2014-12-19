package main

import (
	"os"
)

func main() {
	// A panic() is used when something goes wrong and you need to fail fast.

	panic("a problem")

	// Common use of panic is to abort if a function returns a value that we
	// don't know how to handle.
	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
