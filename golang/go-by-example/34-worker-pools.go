package main

import (
	"fmt"
	"time"
)

// We define the main goroutine worker function which will have a unique id
// and two channels. The first channel receives jobs and the second channel
// sends results. We sleep to simulate an expensive task.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "processing job", j)
		time.Sleep(time.Second)
		results <- j * 2
	}
}

func main() {
	// Our channels will each except integers with a length of 100
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// We create 3 worker gorountine instances here
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// We then create 9 jobs, send them onto the jobs channel, and close the
	// channel so we can't send anymore.
	for j := 1; j <= 9; j++ {
		jobs <- j
	}
	close(jobs)

	// We then collect all the results from the jobs
	for a := 1; a <= 9; a++ {
		<-results
	}
}
