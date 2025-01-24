let input1 = Int(readLine()!)!
let input2 = Int(readLine()!)!

print(input1 * (input2%10))
print(input1 * ((input2%100)/10))
print(input1 * (input2/100))
print(input1 * input2)
