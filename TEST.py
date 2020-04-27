from scipy.special import beta
from scipy.special import gamma
import math
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

val = pd.read_excel("C:/Users/Lenovo/Desktop/大四下/毕设/CODE/dp_crystmorph/regionI_double_peak/region_II_excel/0.6-R2-246_04260808.xlsx")
value = val.values
Dw_array = np.zeros((1183))
Dn_array = np.zeros((1183))
k = np.zeros((1183))
for i in range(0,value.shape[0]):
    D0w = value[i,3]
    nuDw = value[i,4]
    D0n = value[i,6]
    nuDn = value[i,7]

    Dw = D0w * gamma(0.5) / beta(nuDw,0.5)
    sigmaDw = math.sqrt(nuDw*D0w*D0w - Dw*Dw)
    Dn = D0n * gamma(0.5) / beta(nuDn,0.5)
    sigmaDn = math.sqrt(nuDn*D0n*D0n - Dn*Dn)
    Dw_array[i] = Dw
    Dn_array[i] =Dn
    k[i] = value[i,2]/value[i,5]

# plt.title("Evolution of Diameter")
# plt.plot(np.arange(0,1183),Dw_array.squeeze(0),'o',label="Dw")
# plt.plot(np.arange(0,1183),Dn_array.squeeze(0),'o',label="Dn")
# plt.xlabel("number of optimized")
# plt.ylabel("D/nm")
# plt.legend()
# plt.show()
# plt.title("Evolution of Kw/Kn")
# plt.xlabel("number of optimized")
# plt.ylabel("Kw/Kn")
# plt.plot(np.arange(0,1183),k,'*')
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(Dw_array,'o',label='Dw')
ax1.plot(Dn_array, 'o', label='Dn')
plt.xlabel("number of optimized")
plt.ylabel("D/nm")
ax1.legend(loc='center right')
ax2 = ax1.twinx()
ax2.plot(k, 'k-',label='Kw/Kn')
ax2.legend(loc="center")
plt.ylabel("Kw/Kn")
fig.savefig('fig.png', dpi=1000)
plt.show()

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

# strain = [0.5,0.6,0.9,1.4]
# Kw = [60.39,45,42.8,36.9]
# Kn = [6.9,7.4,9.42,23.3]
# Dw = [170.75,170,195,124.6]
# Dn = [108.51,137,84.5,77.1]
# k = []
# for i in range(0,4):
#     k.append(Kw[i]/Kn[i])
# plt.subplot(2,1,1)
# plt.xlabel("strian")
# plt.ylabel("D/nm")
# plt.plot(strain,Dw,color="blue", linewidth=2.5, linestyle="-",label="Dw")
# plt.plot(strain,Dn,color="red", linewidth=2.5, linestyle="-",label="Dn")
# plt.vlines([0.6,0.9,1.4],0,200)
# plt.legend()
# plt.subplot(2,1,2)
# plt.plot(strain,k)
# plt.show()