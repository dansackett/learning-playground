package main

import (
	"fmt"
	"net/url"
	"strings"
)

func main() {
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// We can parse a url and have all sections of the URL available to access
	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	// We can get these things such as scheme, user, and password
	fmt.Println(u.Scheme)
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// The host is the host and port
	fmt.Println(u.Host)
	h := strings.Split(u.Host, "")
	fmt.Println(h[0])
	fmt.Println(h[1])

	// The path is after the slash
	// The fragment is the final piece
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// The raw query set is k=v
	// We can parse a query and turn it into a map
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}
