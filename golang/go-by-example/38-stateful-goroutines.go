package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// Create structs to handle messages being passed back and forth in the goroutine
type readOp struct {
	key  int
	resp chan int
}

type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {
	var ops int64 = 0

	// Create our channels based on the structs we made.
	reads := make(chan *readOp)
	writes := make(chan *writeOp)

	// We encapsulate the state in a single goroutine and use channels to
	// communicate updates within it.
	go func() {
		var state = make(map[int]int)

		// We infinitely loop with the select listening for reads and writes
		// and communicating responses on the appropriate response channels.
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// We create 100 goroutines for reads. We create a new readOp object,
	// write that to the reads channel, and block until there's a response and
	// then update the atomic counter.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := &readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddInt64(&ops, 1)
			}
		}()
	}

	// We create 10 goroutines for writes. We create a new writeOp object,
	// write that to the writes channel, and block until we get a response and
	// then update the atomic counter.
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := &writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddInt64(&ops, 1)
			}
		}()
	}

	// Allow the goroutines to run for a second
	time.Sleep(time.Second)

	// Capture the ops variable in a new instance to preserve safety.
	opsFinal := atomic.LoadInt64(&ops)
	fmt.Println("ops:", opsFinal)
}
