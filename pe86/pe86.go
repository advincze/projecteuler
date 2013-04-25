package main

import (
	"time"
)

var sq map[int64]int64

func main() {
	t := time.Now()
	m := int64(100)
	sq = make(map[int64]int64)
	sqm := make(map[int64]bool)

	for i := int64(0); i < int64(3)*m; i++ {
		v := i * i
		sq[i] = v
		sqm[v] = true
	}

	c := 0
	sumways := make(map[int64]int)
	for x := int64(1); x < m; x++ {
		for y := x; y < m; y++ {
			sumways[x+y] += 1
		}
	}

	for z := int64(1); z < m; z++ {
		for xy := z; xy < 2*m; xy++ {
			xysq := sq[xy]
			s := sumways[xy]
			if sqm[sq[z]+xysq] {
				c += s
			}

		}
	}
	println(c)
	println("time", time.Since(t).Nanoseconds())

}
