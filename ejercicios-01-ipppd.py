#Jaime Gómex del Rey
# -*- coding: utf-8 -*-
# ejercicios-01-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos


#Cambio en fichero para commit


# Práctica 1: Introducción a Python
# =================================

# -----------
# EJERCICIO 1
# -----------

# Definir una función suma(l) que recibiendo como entrada una lista l de
# números, devuelva la suma de sus elementos.

# Por ejemplo:

# >>> suma([2,4.6,3.1,2.8,5,8,9,23])
# 57.5

def suma(l):
    sum=0;
    for x in l:
        sum+= x;
    return sum
        
# -----------
# EJERCICIO 2
# -----------

# Definir una función n_elementos_pos(l) que recibiendo como entrada una
# lista l de números enteros, devuelva el número de elementos positivos de la
# lista 

# Por ejemplo:

# >>> n_elementos_pos([-2,2,1,-3,2,5,-6,4,5,2,-8])
# 7

def n_elementos_pos(l):
    acum=0;
    for x in l:
        if x > 0:
            acum+=1
        else: 
            acum
    return acum

# -----------
# EJERCICIO 3
# -----------

# Definir una función máximo(l) que recibiendo como entrada una lista l de
# números, devuelva el mayor de sus elementos

# Por ejemplo:

# >>> máximo([23,2,45,6,78,2,4,9,55])
# 78

def máximo(l):
    max=float("-inf");
    for x in l:
        if x > max:
            max = x
        else:
            max
    return max

# -----------
# EJERCICIO 4
# -----------

# Definir una función suma_saltando(l,i,n) que recibiendo como entrada una lista
# números, una posición i de esa lista, y un número natural n, devuelve la
# suma de los elementos de la lista, empezanod en el i-ésimo y saltando de n
# en n. 

# Por ejemplo:

# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],4,3)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],2,2)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],3,2)
# 20

def suma_saltando(l,i,n):
    sum=0
    for x in range(i,len(l),n):
        sum+=l[x]
    return sum

#def suma_saltando(l,i,n):
#    sum=0
#    for x in l[i::n]:
#        sum+=x
#    return sum

# -----------
# EJERCICIO 5
# -----------

# Definir una función pos_máximo(l) que recibiendo como entrada una lista de
# números, devuelve la posición del mayor elemento de la lista.

# Por ejemplo:

# >>> pos_máximo([23,2,45,6,78,2,4,9,55])
# 4

def pos_máximo(l):
    max=float("-inf");
    posicion = 0;
    for x in l:
        if x > max:
            posicion=l.index(x)
            max=x 
        else:
            max
            posicion
    return posicion

#def pos_máximo(l):
#    max=float("-inf");
#    pos_max = -1
#    pos=0
#    for x in l:
#        if x > max:
#            max=x
#            pos_max=pos            
#        pos+=1
#    return pos_max

# -----------
# EJERCICIO 6
# -----------

# Definir una función media(l) que recibiendo una lista numérica como entrada,
# devuelve la media aritmética de sus elementos 

# Por ejemplo:

# >>> media([1,2,5,2,3,6,7])
# 3.7142857142857144

def media(l):
    sum=0
    media=0
    for x in l:
        sum+=x
    media = sum/len(l)
    return media

#def media(l):
#    sum=0
#    cont=0
#    for x in l:
#        sum+=x
#        cont+=1
#    return sum/cont
    
# -----------
# EJERCICIO 7
# -----------

# Definir una función varianza(l) que recibiendo una lista numérica como
# entrada, devuelve la varianza de ese conjunto de números

# Por ejemplo:

# >>> varianza([1,2,5,2,3,6,7])
# 4.489795918367346

def varianza(l):
    varianza =0
    for x in l:
        med=media(l)
        varianza+=(x-med)**2
    return varianza/len(l)

#def varianza(l):
#    acum=0
#    cont=0
#    for x in l:
#        acum+=x**2
#        cont+=1
#    return acum/cont (terminar)


# -----------
# EJERCICIO 8
# -----------

# Definir una función mediana(l) que recibiendo una lista numérica como
# entrada, devuelve la mediana de ese conjunto de números. Nota: puede ser de
# utilidad usar la función predefinida sorted(l), que ordena listas. 

# Por ejemplo:

# >>> mediana([3,1,4,2,7,8,5,3,5])
# 4
# >>> mediana([9,1,4,3,3,2,2,4,5,3,11,6])
# 3.5

def mediana(l):
    l1 = sorted(l)
    n=len(l1)
    if len(l1)%2 ==0:
        medi=(l1[round((n/2)-1)]+l1[round((n/2)+1)])/2
    else:
        medi=l1[round((n/2)-0.5)]
    return medi
            
# -----------
# EJERCICIO 9
# -----------

# Definir una función cuadrados_lista(l),que recibiendo como entrada una lista
# l de números, devuelve la lista de los cuadrados de los elementos de l, en
# el mismo orden. 

# Por ejemplo:


# >>> cuadrados_lista([2,3,1,2.5,7,8/3])
# [4, 9, 1, 6.25, 49, 7.111111111111111]

def cuadrados_lista(l):
    l1=l
    for x in range(len(l)):
        l1[x]=l[x]*l[x]
    return l1

#def cuadrados_lista(l):
#    res=[]
#    for x in l:
#        res.append(x*x)
#    return res

#def cuadrados_lista(l):
#    return[x*x for x in l]

# ------------
# EJERCICIO 10
# ------------


# Definir una función prod_map(x,l) que recibiendo como entrada un número
# x y una lista de números l, devuelve la lista resultante de multiplicar cada
# elemento de l por x.

# Por ejemplo:

# >>> prod_map(2.5,[7,8.2,6,10.7,3,21])
# [17.5, 20.5, 15.0, 26.75, 7.5, 52.5]

def prod_map(x,l):
    l1=l
    for n in range(len(l)):
        l1[n]=x*l[n]
    return l1

#def prod_map(x,l):
#    res=[]
#    for n in l:
#        res.append(x*e)
#    return res

#def prod_map(x,l):
#    return[x*e for e in l]

# ------------
# EJERCICIO 11
# ------------

# Definir una función suma_vec(l,m) que recibiendo como entrada dos listas
# numéricas (de la misma longitud), devuelva la lista resultante de sumarla
# componente a componente.

# Por ejemplo:

# >>> suma_vec([8,5,4,2,7],[4,1,7,4,2])
# [12, 6, 11, 6, 9]

def suma_vec(l,m):
    l1=l
    for n in range(len(l)):
        l1[n]=l[n]+m[n]
    return l1

#def suma_vec(l,m):
#    res=[]
#    for n in range(len(l)):
#        res.append(l[n]+m[n])
#    return l1

#def suma_vec(l,m):
#    res=[]
#    for n,y in zip(l,m):
#        res.append(n+y)
#    return res

#def suma_vec(l,m):
#   return[x+y for x,y in zip(l,m)]

#res=[0 for _ in l]

# ------------
# EJERCICIO 12
# ------------


# Definir una función producto_escalar(l,m), que recibiendo como entrada dos
# listas numéricas de la misma longitud, devuelve su producto escalar

# Por ejemplo:

# >>> producto_escalar([2,1,3,4,2,4],[1,2,3,1,1,0])
# 19

def producto_escalar(l,m):
    prod=0
    for n in range(len(l)):
        prod+=l[n]*m[n]
    return prod

#def producto_escalar(l,m):
#    acum=0
#    for x, y in zip(l,m):
#        acum+=x*y
#    return acum

# ------------
# EJERCICIO 13
# ------------

# Definir una función covarianza(l,m) que recibiendo dos listas numéricas de
# la misma longitud, devuelve su covarianza.

# Por ejemplo:

# >>> covarianza([7,2,3,5,6,2,1],[6,1,2,4,5,1,0])
# 4.489795918367346

def covarianza(l,m):
    covar=0
    n=len(l)
    medl=media(l)
    medm=media(m)
    for x, y in zip(l,m):
        covar+=(x-medl)*(y-medm)
    return covar/n
        
# ------------
# EJERCICIO 14
# ------------


# Podemos representar una matriz bidimensional nxm en Python, como una lista
# que tiene n elementos que a su vez son listas de de m elementos
# numéricos. Por ejemplo, la siguiente lista de listas representa una matriz
# 4x7:  

# [[3,2,4,2,6,1,6],
#  [2,1,6,9,3,7,8],
#  [1,5,2,2,0,2,7],
#  [1,0,1,2,9,1,4]]

# Definir una función escalar_mat(x,m),que recibiendo un número x y una matriz
# m (representada como se ha indicado), devuelve la matriz que resulta de
# multiplicar cada elemento de la matriz por x. 

# Por ejemplo:

# >>> m=[[3,2,4,2,6,1,6],[2,1,6,9,3,7,8],[1,5,2,2,0,2,7],[1,0,1,2,9,1,4]]
# >>> escalar_mat(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]

#Existen 3 formas: construtiva, compresión, destructiva

#Constructiva

def escalar_mat_cons(x,m):
    res=[]
    for fila in m:
        fila_res=[]
        for e in fila:
            fila_res.append(x*e)
        res.append(fila_res)
    return res

#Compresión

def escalar_mat_comp(x,m):
   return[[x*e for e in f] for f in m]

#Destructiva

#def escalar_mat_des(x,m):
#    res=[]
#    for fila in m:
#        fila_res=[]
#        for e in fila:
#            fila_res.append(x*e)
#        res.append(fila_res)
#    return res

#otra version con indices
def escalar_mat_ind(x,m):
    res=[]
    n_filas=len(m)
    n_cols=len(m[0])
    for i in range(n_filas):
        resf=[]
        for j in range(n_cols):
            resf.append(x*m[i][j])
        res.append(resf)
    return res


# Definir también una versión escalar_mat_destr(x,m) que devuelve lo mismo,
# pero además modifica m para que contenga lo calculado.  

# Por ejemplo:

# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]
# >>> escalar_mat_destr(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]

#def escalar_mat_destr(x,m):
#    m1= m
#    n_filas=len(m)
#    n_cols=len(m[0])
#    for i in range(n_filas):
#        resf=[]
#        for j in range(n_cols):
#            resf.append(x*m[i][j])
#        res.append(resf)
#    return res

def escalar_mat_destr(x,m):
    res=[]
    n_filas=len(m)
    n_cols=len(m[0])
    for i in range(n_filas):
        for j in range(n_cols):
            m[i][j]*=x
    return m






# ------------
# EJERCICIO 15
# ------------


# Definir una función medias_matriz(m),que recibiendo una matriz m
# (representada como se ha indicado) cuyos elementos son números, devuelve una
# tupla con tres valores: 

# * La lista de las medias de las columnas de la matriz 
# * La lista de las medias columnas de la matriz
# * La media de todos los números de la matriz

# Por ejemplo:

# >>> medias_matriz([[1,2,5,2],[3,1,7,2],[2,1,6,1]])
# ([2.0, 1.3333333333333333, 6.0, 1.6666666666666667], [2.5, 3.25, 2.5], 2.75)











# ------------
# EJERCICIO 16
# ------------


# Definir una función producto_matrices(a,b), tal que recibiendo dos matrices
# a y b (representadas como listas de listas, tal y como se explica en el
# ejercicio anterior), devuelve la matriz resultante de multiplicar a y b
# matricialmente. Supondremos que el número de columnas de a es el mismo que
# el número de filas de b. 


# Por ejemplo:

# >>> a=[[3,1,4,5],[2,0,3,5],[1,1,4,1]]
# >>> b=[[1,2],[2,8],[4,3],[3,1]]
# >>> producto_matrices(a,b)
# [[36, 31], [29, 18], [22, 23]]









# ------------
# EJERCICIO 17
# ------------
# Definir una función vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------










# ------------
# EJERCICIO 18
# ------------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima. 

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------





        
