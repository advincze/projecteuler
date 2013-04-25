package main

import (
	"time"
	"strconv"
)

func main() {
	t := time.Now()

	k := 10000
	squares := make([]int64, k)
	for i := 1; i < k; i++ {
		squares[i] = int64(i*i)
		//println(squares[i])
	}
	sumsquares := make([][]int64, k)
	sum :=int64(0)
	for i := 1; i < k; i++ {
		sumsquares[i] = make([]int64, k)
		sumsquares[i][i] = squares[i]
		for j := i+1; j < k; j++ {
			sumsquares[i][j] = sumsquares[i][j-1]+squares[j]
			
			if isPalindrome(sumsquares[i][j]) {
				
				if sumsquares[i][j] < 1e8 {
					//println(i,j, sumsquares[i][j])
					sum += sumsquares[i][j]
				}
			}
		}
		
	}	
	println("sum", sum)
	println("time", time.Since(t).Nanoseconds()/1e6, "ms")
}

func isPalindrome(i int64) bool {
	s := strconv.FormatInt(i, 10)
	for; len(s)>1; {
		//println("s",s)
		if s[0] != s[len(s)-1] {
			return false
		}
		s = s[1:len(s)-1]
		//println("s2",s)
	}
	return true
}

