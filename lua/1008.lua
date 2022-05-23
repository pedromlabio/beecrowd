local numero = io.read("n")
local horas = io.read("n")
local salario = io.read("n")

local salario = string.format("%.2f", salario * horas)
print("NUMBER = " .. numero)
print("SALARY = U$" .. salario)