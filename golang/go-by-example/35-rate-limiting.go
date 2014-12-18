package main

import (
	"fmt"
	"time"
)

func main() {
	// Create 5 requests and close the channel
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// Setup a limiter which receives a value every 200 milliseconds. This
	// regulates things for us.
	limiter := time.Tick(time.Millisecond * 200)

	// Here is the limiter magic. We block on the limiter allowing us to only
	// make on request every 200 milliseconds.
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// If we want to allow a short burst of items in our rate limiting scheme,
	// we can create a buffered channel.
	burstyLimiter := make(chan time.Time, 3)

	// We can pass three messages onto this channel to fill it
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// Every 200 milliseconds we will attempt to add a new message onto our
	// channel.
	go func() {
		for t := range time.Tick(time.Millisecond * 200) {
			burstyLimiter <- t
		}
	}()

	// Now we create 5 requests and then close this channel
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)

	// We simulate 5 more requests here and block on the limiter. This will
	// blast three messages at once.
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}
