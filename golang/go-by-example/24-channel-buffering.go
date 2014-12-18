package main

import (
	"fmt"
)

func main() {
	// Channels are unbuffered by default, meaning it will only get sends if
	// there is a corresponding receive. Buffered channels accept a limited
	// number of values without a corresponding receiver

	// Our channel buffers up to two values
	messages := make(chan string, 2)

	// Because it's buffered, we can send messages into the channel without a
	// concurrent receive
	messages <- "buffered"
	messages <- "channel"

	// We can receive these later
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
