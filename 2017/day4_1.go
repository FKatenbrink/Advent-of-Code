package main

import (
	"fmt"
	"strings"
)

func testDay4_1() {
	result := day4_1("aa bb cc dd ee")
	if result != 1 {
		panic(fmt.Sprintf("Fail: %d", result))
	}
	result = day4_1("aa bb cc dd aa")
	if result != 0 {
		panic(fmt.Sprintf("Fail: %d", result))
	}
	result = day4_1("aa bb cc dd aaa")
	if result != 1 {
		panic(fmt.Sprintf("Fail: %d", result))
	}
}

func isValidLine(line string) int {
	uniqueWords := make(map[string]bool)
	for _, word := range strings.Split(line, " ") {
		_, exists := uniqueWords[word]
		if exists {
			return 0
		}
		uniqueWords[word] = true
	}

	return 1
}

func day4_1(input string) int {
	fmt.Println(input)
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		total += isValidLine(line)
	}

	return total
}
