package main

import (
	"fmt"
	"time"
)

func main() {
	// Create our first channel
	c1 := make(chan string, 1)

	// Simulate a blocking goroutine for 2 seconds
	go func() {
		time.Sleep(time.Second * 2)
		c1 <- "result 1"
	}()

	// For this select, we wait for the channel 1 response but if after 1
	// second and we don't have a response then we'll timeout
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(time.Second * 1):
		fmt.Println("timeout 1")
	}

	// Create another channel
	c2 := make(chan string, 1)

	// Wait 2 seconds to output a response
	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "result 2"
	}()

	// Out timeout here is 3 seconds so our response should be sent by then
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(time.Second * 3):
		fmt.Println("timeout 2")
	}
}
