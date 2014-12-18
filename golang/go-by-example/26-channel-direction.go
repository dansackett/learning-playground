package main

import (
	"fmt"
)

// This function only accepts a channel for sending values. A compile time
// error will occur if you try to receive on this channel.
func ping(pings chan<- string, msg string) {
	// We get a message and send the message to the pings channel
	pings <- msg
}

// This function accepts a channel to receive and a channel to send.
func pong(pings <-chan string, pongs chan<- string) {
	// We receive the message from the pings channel
	msg := <-pings
	// We send the message to the pongs channel
	pongs <- msg
}

func main() {
	// When using channels as function params, you can specify if the channel
	// should only send or receive values. This can increase type safety.

	pings := make(chan string, 1)
	pongs := make(chan string, 1)

	ping(pings, "passed message")
	pong(pings, pongs)

	// We receive from the pongs channel and print the message.
	fmt.Println(<-pongs)
}
