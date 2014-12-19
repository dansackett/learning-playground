package main

import (
	"fmt"
	"os"
)

func main() {
	defer fmt.Println("!")

	// Exit with status 3.
	os.Exit(3)
}
