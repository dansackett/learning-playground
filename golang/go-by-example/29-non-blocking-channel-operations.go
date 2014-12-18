package main

import (
	"fmt"
)

func main() {
	// By default, channels are blocking. We can implement a default case in a
	// select to simulate a non-blocking call.

	messages := make(chan string)
	signals := make(chan bool)

	// We have a non-blocking receive where if there's a messages receive
	// waiting then it will take that case, otherwise take default.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// Here's a non-blocking send
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// We can try multiple non-blocking receives here
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}
