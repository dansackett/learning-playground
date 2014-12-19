package main

import (
	"fmt"
	"os"
)

func main() {
	// Defer says to the system, run the function at the end of the main
	// function's execution. So in this case, we create the file, defer the
	// closing of the file, write to the file, and then close the file.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}

	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")
}

func closeFile(f *os.File) {
	fmt.Println("closing")
	f.Close()
}
