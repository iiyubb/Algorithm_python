import Foundation

let input = readLine()!.split(separator:" ").map{Double(String($0))!}

print(input[0] / input[1])