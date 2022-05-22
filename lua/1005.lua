local n1 = io.read("n")
local n2 = io.read("n")

n1 = n1 * 3.5
n2 = n2 * 7.5

local media = string.format("%.5f",(n1 + n2) / 11)

print("MEDIA = " .. media)
