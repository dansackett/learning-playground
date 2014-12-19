package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"sync/atomic"
	"time"
)

func main() {
	// State will be a map and the mutex will allow synchronous updating
	var state = make(map[int]int)
	var mutex = &sync.Mutex{}
	var ops int64 = 0

	// Launch 100 goroutines execute repeared reads against state
	for r := 0; r < 100; r++ {
		go func() {
			total := 0
			for {
				// Randomly select a key, lock it down, update total
				key := rand.Intn(5)
				mutex.Lock()
				total += state[key]
				mutex.Unlock()
				atomic.AddInt64(&ops, 1)

				runtime.Gosched()
			}
		}()
	}

	// Create 10 goroutines for writes to the state
	for w := 0; w < 10; w++ {
		go func() {
			for {
				key := rand.Intn(5)
				val := rand.Intn(100)
				mutex.Lock()
				state[key] = val
				mutex.Unlock()
				atomic.AddInt64(&ops, 1)

				runtime.Gosched()
			}
		}()
	}

	time.Sleep(time.Second)

	var opsFinal = atomic.LoadInt64(&ops)
	fmt.Println("ops:", opsFinal)

	mutex.Lock()
	fmt.Println("state:", state)
	mutex.Unlock()
}
