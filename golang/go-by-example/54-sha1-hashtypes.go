package main

import (
	"crypto/sha1"
	"fmt"
)

func main() {
	s := "sha1 this string"

	// The pattern for sha1 is first we create a new hashing instance.
	// The we write the bytes of our string.
	// Then we sum the to get the final hashed result.
	h := sha1.New()
	h.Write([]byte(s))
	bs := h.Sum(nil)

	// We print this in hex for the final result
	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}
