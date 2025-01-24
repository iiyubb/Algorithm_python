let input = readLine()!.split(separator: " ").map { Int(String($0))!}
let time = Int(readLine()!)!

var h = input[0], m = input[1]

var now_time = h * 60 + m
var end_time = now_time + time

var end_time_h = end_time / 60
var end_time_m = end_time % 60

if end_time_h >= 24 {
    end_time_h -= 24
}

print(end_time_h, end_time_m)
