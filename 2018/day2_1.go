package main

import (
	"fmt"
	"strings"
)

func testDay2_1() {
	assertEquals("abcdef", 2, day2_1)
	assertEquals("+1\n-1", 0, day2_1)
	assertEquals("+3\n+3\n+4\n-2\n-4", 10, day2_1)
	assertEquals("-6\n+3\n+8\n+5\n-6", 5, day2_1)
	assertEquals("+7\n+7\n-2\n-7\n-4", 14, day2_1)
	fmt.Println("All tests OK.")
}

func day2_1(input string) int {
	lines := strings.Split(input, "\n")
	values := make(map[int]bool)
	values[0] = true
	total := 0
	for i := 0; ; i = (i + 1) % len(lines) {
		line := lines[i]
		total += lineToInt(line)
		if values[total] {
			break
		}
		values[total] = true
	}

	return total
}
