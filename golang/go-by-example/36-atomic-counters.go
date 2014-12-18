package main

import (
	"fmt"
	"runtime"
	"sync/atomic"
	"time"
)

func main() {
	// We create an unsigned integer counter
	var ops uint64 = 0

	// We start 50 goroutines that increment the counter once a millisecond
	for i := 0; i < 50; i++ {
		go func() {
			for {
				// We atomically increment using the memory address of our counter
				atomic.AddUint64(&ops, 1)

				// We then allow other goroutines to run
				runtime.Gosched()
			}
		}()
	}

	// We wait a second to allow some operations to accumulate
	time.Sleep(time.Second)

	// To safely use the counter, we have to make a copy of the operations and
	// print it afterwards.
	opsFinal := atomic.LoadUint64(&ops)
	fmt.Println("ops:", opsFinal)
}
