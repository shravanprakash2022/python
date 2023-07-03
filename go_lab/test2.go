package main

import (
	"fmt"
)

func main() {

	arr := [5]int{10, 20, 90, 70, 60}
	slice := arr[:3]
	fmt.Println("old slice", (slice))
	fmt.Println("old slice", cap(slice))
	new_slice := append(slice, 100, 200)
	fmt.Println("new slice Cap", cap(new_slice))
	fmt.Println("new slice", (new_slice))

}
