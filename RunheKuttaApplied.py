# -*- coding: utf-8 -*-
#librerias
import numpy as np
import pylab as plt

#funciones
def fa(ca,cb,cc):  
    return -0.1*ca*cc+0.3*ca
def fb(ca,cb,cc):
    return -0.01*ca*cc+0.2*cb
def fc(ca,cb,cc):
    return -0.1*ca*cc-0.3*cb+0.3*cc

#metodo runhe kutta
def metodo(h,t):         
    n=t/h
    res=np.zeros([n+1,4])   #matriz respuesta inicializada con 0
    res[0,0],res[0,1],res[0,2],res[0,3]=(0,50,10,30)    #valores iniciales de concentracion 
    t_=0
    for tmp in np.arange(h,t+h,h):
        #crea matriz de contantes del metodo de grado 4
        
        #Formulas para calcular las constantes k
        k1A=fa(res[t_,1],res[t_,2],res[t_,3])       
        k1B=fb(res[t_,1],res[t_,2],res[t_,3])
        k1C=fc(res[t_,1],res[t_,2],res[t_,3])
        k2A=fa(res[t_,1]+h*k1A/2,res[t_,2]+h*k1A/2,res[t_,3]+h*k1A/2)
        k2B=fb(res[t_,1]+h*k1B/2,res[t_,2]+h*k1B/2,res[t_,3]+h*k1B/2)
        k2C=fc(res[t_,1]+h*k1C/2,res[t_,2]+h*k1C/2,res[t_,3]+h*k1C/2)
        k3A=fa(res[t_,1]+h*k2A/2,res[t_,2]+h*k2A/2,res[t_,3]+h*k2A/2)
        k3B=fb(res[t_,1]+h*k2B/2,res[t_,2]+h*k2B/2,res[t_,3]+h*k2B/2)
        k3C=fc(res[t_,1]+h*k2C/2,res[t_,2]+h*k2C/2,res[t_,3]+h*k2C/2)
        k4A=fa(res[t_,1]+h*k3A,res[t_,2]+h*k3A,res[t_,3]+h*k3A)
        k4B=fb(res[t_,1]+h*k3B,res[t_,2]+h*k3B,res[t_,3]+h*k3B)
        k4C=fc(res[t_,1]+h*k3C,res[t_,2]+h*k3C,res[t_,3]+h*k3C)
        #llena la matriz de respuesta con cada concentracion calculada
        res[t_+1,0]= tmp        
        res[t_+1,1]= res[t_,1]+h/6*(k1A+2*k2A+2*k3A+k4A)
        res[t_+1,2]= res[t_,2]+h/6*(k1B+2*k2B+2*k3B+k4B)
        res[t_+1,3]= res[t_,3]+h/6*(k1C+2*k2C+2*k3C+k4C)

        t_+=1           #actualiza el tiempo
        #imprime los resultados requeridos        
        if tmp==0.2:    
            print '[t       ca      cb      cc]'
            print res[t_,:]
        if np.round(tmp,1)==1.0:    #se redondean los valores porque por algun motivo tienen un decimal de mas
            print res[t_,:]         #se imprimen los resultados
        if np.round(tmp,1)==2.0:
            print res[t_,:]
        if np.round(tmp,1)==3.0:
            print res[t_,:] 
    return res
    

print 'dt .1'   #imprime resultados para delta de timpo 0.1
plt.figure(1)
plt.title('Concentracion dt .1') 
res=metodo(0.1,3) 
plt.plot(res[:,0],res[:,1])  
plt.plot(res[:,0],res[:,2])      
plt.plot(res[:,0],res[:,3])
plt.xlabel('Tiempo')                    
plt.ylabel('Concentracion')

print 'dt .2'   #imprime los resultados para delta de tiempo 0.2
plt.figure(2)
plt.title('Concentracion dt .2')
res=metodo(0.2,3)   
plt.plot(res[:,0],res[:,1])   
plt.plot(res[:,0],res[:,2])  
plt.plot(res[:,0],res[:,3])  
plt.xlabel('Tiempo [s]')
plt.ylabel('Concentracion') 
plt.show()           
