package main

import "fmt"
import "time"

func getMessageChannel(msg string, delay time.Duration) <-chan string {
	c := make(chan string)
	go func() {
		for i := 1; i <= 3; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Millisecond * delay)
		}
	}()

	return c
}

func main() {
	c1 := getMessageChannel("first", 300)
	c2 := getMessageChannel("second", 150)
	c3 := getMessageChannel("third", 10)

	for i := 1; i <= 9; i++ {
		select {
		case msg := <-c1:
			fmt.Println(msg)
		case msg := <-c2:
			fmt.Println(msg)
		case msg := <-c3:
			fmt.Println(msg)
		}
	}
}
