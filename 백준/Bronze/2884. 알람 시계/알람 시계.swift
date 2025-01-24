let input = readLine()!.split(separator: " ").map{Int(String($0))!}

var (h, m) = (input[0], input[1])

if m < 45 {
    h -= 1
    m = 60+m-45
} else {
    m = m - 45
}

if h < 0 {
    h += 24
}

print(h, m)