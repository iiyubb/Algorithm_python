let input = Int(readLine()!)!

if (input % 4 == 0) && (input % 100 != 0) {
    print(1)
} else if (input % 4 == 0) && (input % 400 == 0) {
    print(1)
} else {
    print(0)
}
