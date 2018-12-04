package main

import (
	"fmt"
	"strconv"
	"strings"
)

func testDay1_1() {
	assertEquals("+1\n-2\n+3\n+1", 3, day1_1)
	assertEquals("+1\n+1\n+1", 3, day1_1)
	assertEquals("+1\n+1\n-2", 0, day1_1)
	assertEquals("-1\n-2\n-3", -6, day1_1)
	fmt.Println("All tests OK.")
}

func lineToInt(line string) int {
	sign := 1
	if string(line[0]) == "-" {
		sign = -1
	}
	value, _ := strconv.Atoi(line[1:])
	return sign * value
}

func day1_1(input string) int {
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		total += lineToInt(line)
	}

	return total
}
