package main

var m map[int]int64

func main() {
	m = make(map[int]int64)
	sum := cpsCached(50)
	println(sum)
}

func cpsCached(remaining int) int64 {
	if v, ok := m[remaining]; ok {
		return v
	} else {
		v = countpos(remaining)
		m[remaining] = v
		return v
	}
	panic("not reached")
}

func countpos(remaining int) int64 {
	if remaining < 0 {
		return 0
	}
	if remaining == 0 {
		return 1
	}
	res := cpsCached(remaining - 1)
	res += cpsCached(remaining - 2)
	res += cpsCached(remaining - 3)
	res += cpsCached(remaining - 4)
	return res
}
