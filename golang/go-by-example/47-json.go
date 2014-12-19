package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Build structs to hold fruits and a page
type Response1 struct {
	Page   int
	Fruits []string
}

type Response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {
	// We can encode basic data types to JSON strings.
	// We can do booleans
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	// We can do integers
	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	// We can do floats
	fltB, _ := json.Marshal(2.38)
	fmt.Println(string(fltB))

	// We can do strings
	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// We can do slices
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	// We can do maps
	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// We can do custom data types as well using exported fields
	res1D := &Response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// We can do custom data types as well using exported fields
	res2D := &Response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// We create variables to help decoding JSON
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)
	var dat map[string]interface{}

	// The actual decoding happens with Unmarshal() which checks for errors here.
	// This is an inline call as we can see.
	if err := json.Unmarshal(byt, &dat); err != nil {
		panic(err)
	}

	fmt.Println(dat)

	// To use the decoded items, we need to cast them to their proper types.
	num := dat["num"].(float64)
	fmt.Println(num)

	// We have to do multiple casts to get nested data
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// We can use custom data types to decode into as well which helps type
	// saftey.
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := &Response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// Instead of using strings or bytes as an intermediary, we can use Stdout
	// as well to handle this.
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}
