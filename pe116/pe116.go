package main

var m map[Cps]int64

func main() {
	m = make(map[Cps]int64)
	k := 50
	sum := cpsCached(k, 2, false)
	sum += cpsCached(k, 3, false)
	sum += cpsCached(k, 4, false)
	println(sum)
}

type Cps struct {
	Rem   int
	Using int
	Used  bool
}

func cpsCached(remaining int, using int, used bool) int64 {
	cps := Cps{Rem: remaining, Using: using, Used: used}
	if v, ok := m[cps]; ok {
		return v
	} else {
		v = countpos(remaining, using, used)
		m[cps] = v
		return v
	}
	println("no way")
	return 0

}

func countpos(remaining int, using int, used bool) int64 {
	if remaining < 0 {
		return 0
	}
	if remaining == 0 {
		if used {
			return 1
		} else {
			return 0
		}
	}
	return cpsCached(remaining-1, using, used) + cpsCached(remaining-using, using, true)
}
