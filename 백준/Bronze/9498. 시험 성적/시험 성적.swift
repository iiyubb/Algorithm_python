let input = Int(readLine()!)!

if input >= 90 {
    print("A")
} else if input < 90 && input >= 80 {
    print("B")
} else if input < 80 && input >= 70 {
    print("C")
} else if input < 70 && input >= 60 {
    print("D")
} else {
    print("F")
}
