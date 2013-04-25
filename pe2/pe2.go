package main

func main() {
	f0, f1, sum := 0, 1, 0
	for f := 0; f <= 4e6; f0, f1 = f1, f {
		f = f0 + f1
		if (f0+f1)%2 == 0 {
			sum += f
		}
	}
	println(sum)
}
