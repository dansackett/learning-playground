package main

import (
	"fmt"
	"time"
)

func main() {
	// Timers represent a single event in the future. They provide a channel
	// that when the timer expires, will be notified.
	timer1 := time.NewTimer(time.Second * 2)

	// This is blocking and executes on the timer's channel C
	<-timer1.C
	fmt.Println("Timer 1 expired")

	timer2 := time.NewTimer(time.Second)

	// One nice thing you can do is stop a timer before it fires unlike
	// time.Sleep() which will happen.
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 expired")
	}()

	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}
}
