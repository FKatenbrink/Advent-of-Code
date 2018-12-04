package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"reflect"
	"runtime"
	"strings"
)

func main() {
	if len(os.Args) == 2 {
		dat, err := ioutil.ReadFile(os.Args[1])
		if err != nil {
			panic(err)
		}
		fmt.Printf("Result for file input: %d\n", day2_1(strings.TrimSpace(string(dat))))
	} else {
		testDay2_1()
	}
}

func assertEquals(input string, expected int, dayFunction func(input string) int) {
	result := dayFunction(input)
	if result != expected {
		panic(fmt.Sprintf("Failed function %s(...) for input\n### Begin\n%s\n### End\nExpected=%d != Result=%d", nameOf(dayFunction), input, expected, result))
	} else {
		fmt.Println(fmt.Sprintf("Test passed for function %s(...) for input\n### Begin\n%s\n### End\nExpected=%d == Result=%d", nameOf(dayFunction), input, expected, result))
	}
}

func nameOf(f interface{}) string {
	v := reflect.ValueOf(f)
	if v.Kind() == reflect.Func {
		if rf := runtime.FuncForPC(v.Pointer()); rf != nil {
			return rf.Name()
		}
	}
	return v.String()
}
