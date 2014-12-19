package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// We can set and get environment variables in the os package
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	fmt.Println()

	// We can loop through all the environment variables and print them.
	for _, e := range os.Environ() {
		pair := strings.Split(e, "=")
		fmt.Println(pair[0])
	}
}
