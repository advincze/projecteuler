package main

import (
	"time"
	"math"
	"sort"
)

func main() {
	t := time.Now()

	var pows []float64
	m := make(map[float64]bool)
	for i := 2; i < 100; i++ {
		for j:= 2; j<100; j++ {
			pow := math.Pow(float64(i),float64(j))
			if !m[pow] && pow >9{
				if sumdigits(int64(pow), 0) == i {
					pows = append(pows, pow)
					m[pow] = true
				}
				
			}
		}
	}

	sort.Float64s(pows)
	
	println(int64(pows[29]))	
	println("time", time.Since(t).Nanoseconds()/1e6, "ms")
}

func sumdigits(i int64, sum int) int {
	if i < 10 { 
		return sum + int(i)
	}
	return sumdigits(i/10, sum+int(i%10))
}