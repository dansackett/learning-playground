package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {
	// We need the binary to exec specifically so we use exec.LookPath() to
	// find the proper binary file.
	binary, lookErr := exec.LookPath("ls")
	if lookErr != nil {
		panic(lookErr)
	}

	// We build a slice with our args and grab the environment variables since
	// exec also requires these.
	args := []string{"ls", "-a", "-l", "-h"}
	env := os.Environ()

	// We execute the command here and if all goes well then we exit
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
