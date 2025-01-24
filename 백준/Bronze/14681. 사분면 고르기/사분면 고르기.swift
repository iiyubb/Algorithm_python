let input1 = Int(readLine()!)!
let input2 = Int(readLine()!)!

if input1 > 0 && input2 > 0 {
    print(1)
} else if input1 > 0 && input2 < 0 {
    print(4)
} else if input1 < 0 && input2 < 0 {
    print(3)
} else if input1 < 0 && input2 > 0 {
    print(2)
}
