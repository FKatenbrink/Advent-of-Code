package main

import (
	"fmt"
	"sort"
	"strings"
)

func assertEquals(input string, result int, expected int) {
	if result != expected {
		panic(fmt.Sprintf("Fail %s: %d", input, result))
	}
}

func testDay4_2() {
	result := day4_2("abcde fghij")
	assertEquals("abcde fghij", result, 1)
	result = day4_2("abcde xyz ecdab")
	assertEquals("abcde xyz ecdab", result, 0)
	result = day4_2("a ab abc abd abf abj")
	assertEquals("a ab abc abd abf abj", result, 1)
	result = day4_2("iiii oiii ooii oooi oooo")
	assertEquals("iiii oiii ooii oooi oooo", result, 1)
	result = day4_2("oiii ioii iioi iiio")
	assertEquals("oiii ioii iioi iiio", result, 0)
}

// SortString sorts a string
func SortString(input string) string {
	s := strings.Split(input, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func isValidAnagramLine(line string) int {
	uniqueWords := make(map[string]bool)
	for _, word := range strings.Split(line, " ") {
		sortedWord := SortString(word)
		_, exists := uniqueWords[sortedWord]
		if exists {
			return 0
		}
		uniqueWords[sortedWord] = true
	}

	return 1
}

func day4_2(input string) int {
	fmt.Println(input)
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		total += isValidAnagramLine(line)
	}

	return total
}
