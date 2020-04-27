D0w = 66.31
nuDw = 11.64
D0n = 26.55
nuDn = 27.74
Dw = D0w * gamma(0.5) / beta(nuDw,0.5)
sigmaDw = math.sqrt(nuDw*D0w*D0w - Dw*Dw)
Dn = D0n * gamma(0.5) / beta(nuDn,0.5)
sigmaDn = math.sqrt(nuDn*D0n*D0n - Dn*Dn)

print(Dw)
print(Dn)