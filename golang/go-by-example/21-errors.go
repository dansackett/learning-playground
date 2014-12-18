package main

import (
	"errors"
	"fmt"
)

// Errors by convention are the last return value of a function
// error is a built-in type
// errors.New() creates an error instance with message
// returning nil in place of an error means no error occurred
func f1(arg int) (int, error) {
	if arg == 42 {
		return -1, errors.New("can't work with 42")
	}

	return arg + 3, nil
}

// If we want to make our own error class rather than use the built-in error,
// we just have to build a structure and implement the Error() method on it.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

// We use the &struct{} syntax to build a new struct in place
func f2(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't work with it"}
	}

	return arg + 3, nil
}

func main() {
	for _, i := range []int{7, 42} {
		// This common idiom in Go has you do an inline assignment within an
		// if statement checking for an error from the assignment
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// If we want to use a custom error, we have to get the error in an
	// instance and then act on it
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
