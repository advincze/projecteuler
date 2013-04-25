package main

func main() {
	n, max := int64(600851475143), int64(0)
	for i := int64(1); i <= n; i++ {
		if n%i == 0 {
			max, n = i, n/i
		}
	}
	println(max)
}
