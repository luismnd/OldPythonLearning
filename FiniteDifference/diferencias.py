# -*- coding: utf-8 -*-
import numpy as np
#definicion de metodo de diferencias finitas separadas
def difin(nx,ny,lx,ly,tipo,q,D,res1):
    deltax,deltay,numero,valor=(lx/nx,ly/ny,nx*ny,q/D)    #parametros
    mat=llenamatriz(nx,ny,deltax,deltay,numero) #calculo de la matriz
    resp=vresp(tipo,numero,valor,res1)          #calculo vector respuesta
    sol=np.linalg.solve(mat,resp)         #solucion del sistema
    return sol
#definicion de calculo de matriz de coeficientes
def llenamatriz(nx,ny,deltax,deltay,numero):
    coeficientes,matc,cont=(np.zeros((nx,ny)),np.zeros((numero,numero)),0)
    for i in range(0,nx):       #llena la matriz con coeficientes
        for j in range(0,ny):
            coeficientes[i,j]=  -2./(deltax**2.)  -   2./(deltay**2.)      
            c1,c2,c3,c4=i+1,i-1,j+1,j-1     #parametros de ubicacion en la matriz
            if c1!=nx:                      #estos condicionales discriminan los valores de frontera
                coeficientes[c1,j]=1/(deltax**2)
            if c2!=0:
                coeficientes[c2,j]=1/(deltax**2)
            if c3!=ny:
                coeficientes[i,c3]=1/(deltay**2)
            if c4!=0:
                coeficientes[i,c4]=1/(deltay**2) 
            cont2=0
            for b in range(0,nx):
                for n in range(0,ny):
                    matc[cont,cont2]=coeficientes[b,n]
                    cont2+=1
            cont,coeficientes=cont+1,np.zeros((nx,ny))
    return matc                     #retorna la matriz
#definicion de vector respuesta
def vresp(tipo,numero,valor,res1):
    resp=[]
    for i in range(0,numero):
        if tipo==1:
            resp.append(valor)
        if tipo==2:
            resp=res1
    return resp
