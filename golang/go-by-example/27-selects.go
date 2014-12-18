package main

import (
	"fmt"
	"time"
)

func main() {
	// Go select lets you wait on multiple channel operations. Usually used in
	// conjunction with goroutines making a powerful component to Go.

	// Create two separate channel objects
	c1 := make(chan string)
	c2 := make(chan string)

	// Each channel receives a value after some amount of time to show blocking
	go func() {
		time.Sleep(time.Second * 1)
		c1 <- "one"
	}()

	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()

	// The select statement will wait for each channel simutaneously and will
	// print the result after it arrives.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}
