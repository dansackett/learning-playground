package main

import (
	"fmt"
)

func main() {
	// Channels are the "pipes" that connect concurrent goroutines. You can
	// send values into channels from one goroutine and receive them in
	// another.

	// We use make() with a type to define a channel
	messages := make(chan string)

	// We create a goroutine that sends "ping" into our channel. We do this
	// with the channel syntax (channel <- message)
	go func() { messages <- "ping" }()

	// The channel syntax receives a value from the channel. Here we receive
	// the "ping" message from the channel and print it out.
	msg := <-messages
	fmt.Println(msg)
}
