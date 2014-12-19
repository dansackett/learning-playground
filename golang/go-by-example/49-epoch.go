package main

import (
	"fmt"
	"time"
)

func main() {
	// We can get the elapsed time since the UNIX Epoch with Unix() and UnixNano()
	now := time.Now()
	secs := now.Unix()
	nanos := now.UnixNano()
	fmt.Println(now)

	millis := nanos / 1000000
	fmt.Println(secs)
	fmt.Println(millis)
	fmt.Println(nanos)

	// We can convert an integer into an UNIX Epoch
	fmt.Println(time.Unix(secs, 0))
	fmt.Println(time.Unix(0, nanos))
}
