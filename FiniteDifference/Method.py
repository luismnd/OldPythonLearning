# -*- coding: utf-8 -*-
import diferencias as dif
#parametros del modelo
dz=0.2
sigma=0.3
E=2 *   10**10
q=40    *   10**3
D=(E*   dz**3) /   (12  *   (1  - sigma**2))

#ejecucion de las solicitudes
print "Resultados variables 1"
r1=dif.difin(31,31,15.,15.,1,q,D,1)
print dif.difin(31,31,15.,15.,2,q,D,r1)

print "Resultados variables 2"
r2=dif.difin(31,41,15.,20.,1,q,D,1)
print dif.difin(31,41,15.,20.,2,q,D,r2)

print "Resultados variables 3"
r3=dif.difin(81,81,40.,60.,1,q,D,1)
print dif.difin(81,81,40.,60.,2,q,D,r1)
