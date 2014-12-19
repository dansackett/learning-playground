package main

import (
	"fmt"
	"strings"
)

// Returns the first index of given string t in slice vs
func Index(vs []string, t string) int {
	for i, v := range vs {
		if v == t {
			return i
		}
	}

	return -1
}

// Returns whether a string t is in a slice vs
func Include(vs []string, t string) bool {
	return Index(vs, t) >= 0
}

// Applies a function to each string in vs and returns if any items match
func Any(vs []string, f func(string) bool) bool {
	for _, v := range vs {
		if f(v) {
			return true
		}
	}

	return false
}

// Applies a function to each string in vs and returns false if any items don't match
func All(vs []string, f func(string) bool) bool {
	for _, v := range vs {
		if !f(v) {
			return false
		}
	}

	return true
}

// Applies a function to each string in vs and if it applies, we append it to
// a new slice to return
func Filter(vs []string, f func(string) bool) []string {
	vsf := make([]string, 0)
	for _, v := range vs {
		if f(v) {
			vsf = append(vsf, v)
		}
	}

	return vsf
}

// Applies a function to each string in vs and returns a new slice with
// updated values.
func Map(vs []string, f func(string) string) []string {
	vsm := make([]string, len(vs))
	for i, v := range vs {
		vsm[i] = f(v)
	}

	return vsm
}

func main() {
	// When we want to perform operations like map or selecting data in Go, we
	// do this will collection functions rather than generics. Below are
	// collection functions for slices of strings.

	var strs = []string{"peach", "apple", "pear", "plum"}

	// Find index of "pear" in strs
	fmt.Println(Index(strs, "pear"))

	// Check if "grape" in strs
	fmt.Println(Include(strs, "grape"))

	// Check if any strings in strs start with "p"
	fmt.Println(Any(strs, func(v string) bool {
		return strings.HasPrefix(v, "p")
	}))

	// Check if all strings in sts start with p
	fmt.Println(All(strs, func(v string) bool {
		return strings.HasPrefix(v, "p")
	}))

	// Return a new slice with items that contain the letter "e"
	fmt.Println(Filter(strs, func(v string) bool {
		return strings.Contains(v, "e")
	}))

	// Return a new list of strs transformed to uppercase
	fmt.Println(Map(strs, strings.ToUpper))
}
