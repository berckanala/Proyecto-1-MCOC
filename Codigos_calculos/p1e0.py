import numpy as np

a1=0.8
b1=3.8
c1=18.6
a2=10
b2=3
c2=10.2
d=13-a2-b2
gammaw=9810
gammasat=21000
i_crit=(gammasat-gammaw)/gammaw
k= 6.9e-5
dH=b1+c1-b2-c2

np=8
ns=3

puntosa=["A","B","C","D","E","F","G","H"]
A=round(b1+c1,1)
B=c1
C=b2+c2
H=b2+c2
D=c2
G=c2
E=c2-d
F=c2-d
puntos=[A,B,C,D,E,F,G,H]
zg =[]
for i in puntos:
    zg.append(i)
ni=[0,1,2,3,4,5,6,7]
hi=[]
for i in ni:
    hi.append((b1+c1)-i*dH/np)
hp=[]
for i in range(8):
    hp.append(hi[i]-zg[i])

uw=[]
for i in range(8):
    uw.append(gammaw*hp[i]/1000)

for i in range(8):
    print(f"La presión de poros del punto {puntosa[i]} es {round(uw[i],3)} kPa")

netos=[]
netos.append(uw[0])
netos.append(uw[1])
netos.append(uw[2]-uw[7])
netos.append(uw[3]-uw[6])
netos.append(uw[4]-uw[5])

print("")

for i in range(5):
    print(f"La presión neta del punto {puntosa[i]} es {round(netos[i],3)} kPa")

print("")
Q=k*dH*ns/np*86400
print(f"El caudal de agua que se filtra es {round(Q,3)} m^3/dia")

print("")

i_max=dH/((B-E)-(G-F))

print(f"El grandiente hidráulico máximo es {round(i_max,3)}")

if i_crit>i_max:
    print("El gradiente hidráulico máximo es menor que el crítico, por lo tanto no se producirá la licuación")
else:
    print("El gradiente hidráulico máximo es mayor que el crítico, por lo tanto se producirá la licuación")

print("")

print(f"El factor de seguridad es {round(i_crit/i_max,3)}")