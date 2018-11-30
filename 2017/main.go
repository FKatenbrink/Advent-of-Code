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
		fmt.Printf("Result for input: %d\n", day4_2(strings.TrimSpace(string(dat))))
	} else {
		testDay4_2()
	}
}
