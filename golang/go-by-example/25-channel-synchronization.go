package main

import (
	"fmt"
	"time"
)

// We create a worker function that will be run as a goroutine. We use the
// done channel to notify the other goroutine that this function is done.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Send value to notify we're done
	done <- true
}

func main() {
	// We can use channels to synchronize execution across goroutines. We can
	// use a blocking receive to wait for the goroutine to finish.

	// Start a worker passing a channel for it to signal through
	done := make(chan bool, 1)
	go worker(done)

	// Block the program until we get a notification from the channel
	<-done

	// @NOTE: removing the <-done would actually exit the program before the
	// goroutine finished.
}
