package main

import (
	b64 "encoding/base64"
	"fmt"
)

func main() {
	data := "abc123!?$*&()'-=@~"

	// We can encode and this, like hashing, expects bytes
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// When decoding, we can catch an error
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// We can also URLEncode and Decode
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}
