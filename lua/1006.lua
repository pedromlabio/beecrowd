local a = io.read("n")
local b = io.read("n")
local c = io.read("n")

a = a * 2
b = b * 3
c = c * 5

soma = a + b + c
media = string.format("%.1f",soma/10)

print("MEDIA = " .. media)