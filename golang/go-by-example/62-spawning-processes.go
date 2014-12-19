package main

import (
	"fmt"
	"io/ioutil"
	"os/exec"
)

func main() {
	// In the most basic way, we can use exec.Command() to execute
	dateCmd := exec.Command("date")

	// We catch any errors
	dateOut, err := dateCmd.Output()
	if err != nil {
		panic(err)
	}

	// Print the output. The Output result is in bytes
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// Begin a grep command
	grepCmd := exec.Command("grep", "hello")

	// We grab input and output pipes
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	// Start the command
	grepCmd.Start()
	// Write to Stdin
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	// Close Stdin
	grepIn.Close()
	// Read the bytes from Stdout
	grepBytes, _ := ioutil.ReadAll(grepOut)
	// Wait for the process to exit
	grepCmd.Wait()

	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// When we want to spawn processes directly, we can use bash -c
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err != nil {
		panic(err)
	}

	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}
