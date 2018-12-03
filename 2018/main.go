package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	if len(os.Args) == 2 {
		dat, err := ioutil.ReadFile(os.Args[1])
		if err != nil {
			panic(err)
		}
		fmt.Printf("Result for input: %d\n", day1_1(strings.TrimSpace(string(dat))))
	} else {
		testDay1_1()
	}
}
