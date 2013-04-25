package main

func main() {
	n := 10000
	a := 2
	asq := a * a
	sumOdd := 0
	for i := 2; i <= n; i++ {
		if i == asq {
			a++
			asq = a * a
		} else if periodLength(a-1, i)%2 == 1 {
			sumOdd++
		}
	}
	println(sumOdd)
}

func periodLength(a, s int) int {
	//http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
	a0 := a
	b0 := 0
	c0 := 1

	type step struct {
		b, c, a int
	}

	m := make(map[step]int)
	var b1, c1, a1 int
	for i := 0; ; b0, c0, a0, i = b1, c1, a1, i+1 {
		b1 = (c0 * a0) - b0
		c1 = (s - (b1 * b1)) / c0
		a1 = (a + b1) / c1
		st := step{b1, c1, a1}
		if j, ok := m[st]; ok {
			return i - j
		} else {
			m[st] = i
		}
	}
	panic("should never reach this line")
}
