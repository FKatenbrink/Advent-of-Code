package main

import (
	"fmt"
	"strconv"
	"strings"
)

func assertEquals(input string, result int, expected int) {
	if result != expected {
		panic(fmt.Sprintf("Fail %s: %d", input, result))
	}
}

func testDay1_1() {
	testCase := "+1\n-2\n+3\n+1"
	result := day1_1(testCase)
	assertEquals(testCase, result, 3)

	testCase = "+1\n+1\n+1"
	result = day1_1(testCase)
	assertEquals(testCase, result, 3)

	testCase = "+1\n+1\n-2"
	result = day1_1(testCase)
	assertEquals(testCase, result, 0)

	testCase = "-1\n-2\n-3"
	result = day1_1(testCase)
	assertEquals(testCase, result, -6)
}

func evaluateLine(line string) int {
	sign := 1
	if string(line[0]) == "-" {
		sign = -1
	}
	value, _ := strconv.Atoi(line[1:])
	return sign * value
}

func day1_1(input string) int {
	fmt.Println(input)
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		total += evaluateLine(line)
	}

	return total
}
