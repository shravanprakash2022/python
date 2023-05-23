package main

import (
	"fmt"
)

/*
func main() {

	var grades int = 42
	fmt.Printf("variable grades = %v is of type %v \n", grades, grades)
	fmt.Printf("variable grades = %v is of type %T \n", grades, grades)
	reflect.TypeOf()
}
*/

func main() {
	/*
									var a, b string = "foo", "bar"
									if a+b == "foo" {
										fmt.Println("foo")
									} else if a+b == "bar" {
										fmt.Println("bar")
									} else if a+b == "foobar" {
										fmt.Println("foobar")
									} else {
										fmt.Println("None matched")
									}
									fmt.Println("thank you!")
								}



							var a, b string = "kolkata", "Kolkata"
							if a == b {
								fmt.Println("strings are equal")
							} else {
								fmt.Println("strings are not equal")
							}
							fmt.Println("thank you!")

						}

						var a, b string = "kolkata", "kolkata"
						if a == b {
							fmt.Println("strings are equal")
						} else {
							fmt.Println("strings are not equal")
						}
						fmt.Println("thank you!")



					var a, b = 100, 5
					switch {
					case a/b == 10:
						fmt.Println("10")
					case a/b == 20:
						fmt.Println("20")
					case a/b == 10:
						fmt.Println("30")
					default:
						fmt.Println("default")
					}

				}


			day := "sunday"
			switch day {
			case "monday":
				fmt.Println("monday")
			case "tuesday":
				fmt.Println("tuesday")
			case "wednesday":
				fmt.Println("wednesday")
			case "thursday":
				fmt.Println("thursday")
			case "friday":
				fmt.Println("friday")
			case "saturday", "sundday":
				fmt.Println("weekwwwend")
			default:
				fmt.Println("default")
			}

		}
	*/

	day := "wednesday"
	switch day {
	case "monday":
		fmt.Println("monday")
	case "tuesday":
		fmt.Println("tuesday")
	case "wednesday":
		fmt.Println("wednesday")
		fallthrough
	case "thursday":
		fmt.Println("thursday")
		fallthrough
	case "friday":
		fmt.Println("friday")
	case "saturday", "sunday":
		fmt.Println("weekend")
	default:
		fmt.Println("default")
	}

}
