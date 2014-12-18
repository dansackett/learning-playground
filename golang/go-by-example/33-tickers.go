package main

import (
	"fmt"
	"time"
)

func main() {
	// Tickers do things at regular intervals

	// Our ticker will fire every 500 milliseconds
	ticker := time.NewTicker(time.Millisecond * 500)

	go func() {
		// We loop over a channel and every message that is received will
		// print the time.
		for t := range ticker.C {
			fmt.Println("Tick at", t)
		}
	}()

	// We set a sleep in the program for 1500 milliseconds and then stop the
	// ticker.
	time.Sleep(time.Millisecond * 1500)
	ticker.Stop()
	fmt.Println("ticker stopped")
}
