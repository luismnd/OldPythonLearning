# -*- coding: utf-8 -*-
#importa las librerias a usar
import numpy as np
import pylab as plt
#importa los datos
datos=np.loadtxt('Datos.txt')
#distribuye los datos en x y y
x,y=(datos[:,0],datos[:,1])
#Crea la funcion de calcular con polinomio
def polinomial(orden):
    #variables para matriz nxm
    m,n=(orden+1,len(x)) 
    #inicia los vectores para respuesta       
    #Resuelve de la forma zT*z*A=zT*Y 
    z=np.zeros((n,m))
    calculado=np.zeros((n)) 
    #calcula la atriz z       
    for i in range(0,n):   
        for j in range(0,m): 
            z[i,j]=x[i]**j    
    zt=z.T           #calcula z transpuesta
    mult=np.dot(zt,z)      
    c=np.dot(zt,y)          
    #resuelve linealmente para coeficientes       
    coef=np.linalg.solve(mult,c)   
    print coef            
    #se calcula el r^2
    sc,sp=(0,0)                      
    for i in range(0,n,1):          
        s=0
        for j in range(0,m,1):          
            s=s+coef[j]*x[i]**j        
        calculado[i]=s
        sc=sc+(y[i]-s)**2         
        sp=sp+(y[i]-y.mean())**2    
    print 'R', (sp-sc)/sp    
    plt.plot(x,calculado)
#Se generan todas las graficas
plt.plot(x,y,'o')               
print 'polinomio 1',polinomial(1)    
print 'polinomio 6',polinomial(6)   
print 'polinomio 9',polinomial(9)    
print 'polinomio 12',polinomial(12)    
print 'polinomio 13',polinomial(13)    
plt.show()                        
