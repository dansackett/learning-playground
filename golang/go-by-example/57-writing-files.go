package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// We can dump a string or bytes into a file with the ioutil.WriteFile()
	d1 := []byte("hello\ngo\n")
	err := ioutil.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// To create a file, we can use os.Create() to open a file for writing
	f, err := os.Create("/tmp/dat2")
	check(err)

	// Close the file at the end of the write cycle
	defer f.Close()

	// We can write byte slices as we want
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// We can write a full string to a file
	n3, err := f.WriteString("writes\n")
	fmt.Printf("wrote %d bytes\n", n3)

	// We issue Sync to flush writes to stable storage
	f.Sync()

	// With the bufio module, we can create a new writer object
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	fmt.Printf("wrote %d bytes\n", n4)

	// We have to flush the writer to ensure all buffered operations have cleared
	w.Flush()
}
