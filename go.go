package main

import (
	"time"
	"fmt"
	)

func f(n int) int {
	if n > 1 {
		return f(n - 1) + f(n - 2)
	}
	return 1
}

func main() {
	start := time.Now()
	fmt.Printf("%d\n", f(40));
	d := time.Since(start)
  fmt.Printf("%d\n", d.Nanoseconds() / time.Millisecond.Nanoseconds())

	// println(start)
}
