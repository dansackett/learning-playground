package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// A line filter reads input from stdin, processes it, and prints it to
	// stdout much like sed and grep.

	// We establish a scanner which turns unbuffered Stdin into a buffered
	// stream. This allows us to advance to the next line easily.
	scanner := bufio.NewScanner(os.Stdin)

	// We read from the buffer, and scanner.Text() gets the current token.
	for scanner.Scan() {
		ucl := strings.ToUpper(scanner.Text())
		fmt.Println(ucl)
	}

	// If we get an error in the scan, we exit. End of file is not reported as
	// an error.
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}
