local name = io.read()
local salario = io.read("n")
local vendas = io.read("n")

local comissao = (vendas/100) * 15

salario = string.format("%.2f",comissao + salario)

print("TOTAL = R$ " .. salario)
