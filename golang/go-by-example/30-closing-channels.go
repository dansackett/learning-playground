package main

import (
	"fmt"
)

func main() {
	// When we have no more expected communication on a channel, we can close
	// it to signal completion to receivers.

	// We create a jobs channel to store our jobs that we need done and a done
	// channel to signal when the jobs are all done.
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Our goroutine will infinitely loop through the jobs messages and if
	// there are more of them then we'll continue looping until their all
	// finished. When they're finished, we pass true to the done channel and
	// return from the loop.
	go func() {
		for {
			// more will be false if the jobs channel is closed, otherwise true
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// We create jobs here and send them into the jobs channel
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}

	// When the jobs are all sent, we close the jobs channel
	close(jobs)
	fmt.Println("sent all jobs")

	// We wait for all jobs to complete in a synchronized manner
	<-done
}
