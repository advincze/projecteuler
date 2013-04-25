package main

import (
	"math/big"
	//"fmt"
	"time"
)

func main() {
	t := time.Now()
	a := 2
	asq := a*a
	mx := big.NewInt(-1)
	mxi := -1
	for i := 2; i <= 100000; i++ {
		if i == asq {
			a++
			asq = a*a
		} else {
			minx := contFract(a,i)
			if minx.Cmp(mx) ==1 {
				mx = minx
				mxi = i
				//fmt.Println(i, minx)
			}

		}
	}
	println(mxi)
	println("time", time.Since(t))
}

func contFract(a, s int) *big.Int {
	//http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
	a0 := a
	b0 := 0
	c0 := 1

	hm1 := big.NewInt(1)
	km1 := big.NewInt(0)
	
	h0 := big.NewInt(int64(a0))  
	k0 := big.NewInt(1)

	var b1, c1, a1 int
	var h1, k1 *big.Int
	bigs := big.NewInt(int64(s))
	
	for i := 0;  ; b0, c0, a0, h0, k0, hm1, km1, i = b1, c1, a1, h1, k1, h0, k0, i+1 {
		b1 = (c0 * a0) - b0
		c1 = (s - (b1 * b1)) / c0
		a1 = (a + b1) / c1
		h1 = big.NewInt(0)
		k1 = big.NewInt(0)
		h1.Add( h1.Mul( big.NewInt(int64(a1)) , h0), hm1)
		k1.Add(k1.Mul(big.NewInt(int64(a1)), k0), km1)
		
		//println(h1, k1)

		temp1 := big.NewInt(0)
		temp2 := big.NewInt(0)
		temp1.Mul(h1,h1)
		temp2.Mul(bigs,temp2.Mul(k1,k1))
		if temp1.Sub(temp1,temp2).Cmp(big.NewInt(1)) == 0 {
			//println("cont fract", i,h1,k1 )
			return h1.Abs(h1)
		}
	}
	panic("should not reach this")
}