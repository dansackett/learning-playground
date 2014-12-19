package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {
	// We can do a regex match to see if a string matches
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// We can precompile a regex pattern to use later
	r, _ := regexp.Compile("p([a-z]+)ch")

	// We can use that regex pattern to run MatchString again
	fmt.Println(r.MatchString("peach"))

	// This returns the matched portion
	fmt.Println(r.FindString("peach punch"))

	// This finds the first match and returns the start and end indices
	fmt.Println(r.FindStringIndex("peach punch"))

	// This gets the full pattern match and the subpattern match
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// This gets the indices for start and end for both pattern and subpattern
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// This gets all matching strings
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// This gets the indices for all matches, submatches, etc
	fmt.Println(r.FindAllStringSubmatchIndex("peach punch pinch", -1))

	// This finds first two matches
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// This checks byte args
	fmt.Println(r.Match([]byte("peach")))

	// This forces the compilation to happen and has one return
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println(r)

	// This replaces all instances of strings with another
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// This transforms matched text into a given function
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}
