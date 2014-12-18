package main

import (
	"fmt"
)

func main() {
	// Our channel holds two messages
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// We can loop through the channel with range
	for elem := range queue {
		fmt.Println(elem)
	}

	// @NOTE: A closed channel can not send messages, but can receive them.
}
