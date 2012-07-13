package main

func f(n int) int {
	if n > 1 {
		return f(n - 1) + f(n - 2)
	}
	return 1
}

func main() {
	println(f(40))
}
