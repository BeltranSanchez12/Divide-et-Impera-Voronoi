#!/usr/bin/env python
# coding: utf-8

# ![Encabezado.JPG](attachment:Encabezado.JPG)

# # PRÁCTICA 2: Ordenación geométrica
# 
# * Como en la práctica anterior, en cada ejercicio debes escribir las funciones correspondientes.
# 
# * En el enunciado se especifica el nombre y las variables y se indica cuál debe ser la salida.
# 
# * También debes realizar las pruebas necesarias que muestren que la función hace lo que debe.
# 

# ## Elementos de la práctica:
# 
# 1. Ordenación de listas con Python.
# 2. Puntos extremos de una lista de puntos.
# 3. Ordenación de listas de puntos.
# 4. Generación de polígonos.

# In[8]:


# Antes de empezar cargamos todas las funciones de la Práctica 1

# ### Problema 1: 
# **Puntos extremos**

# In[14]:


# 1. Puntos extremos.

#    Dada una lista de puntos p, hallar los puntos máximos y mínimos respecto de sus abscisas
#    y respecto de sus ordenadas: Xmax , Xmin, Ymax, Ymin

# De forma natural lo podríamos hacer como:

def Xmax(p):
    max=p[0]
    for i in p:
        if(i[0]>max[0]):
            max=i
    return max

#pero esta función ya está definida en Sage

def Xmax(p):
    return(max(p))

#Igualmente podríamos definir la función Xmin como

def Xmin(p):
    min=p[0]
    for i in p:
        if(i[0]<min[0]):
            min=i
    return min

#pero utilizando la función de Sage

def Xmin(p):
    return min(p)


#Igualmente podríamos definirla funciones Ymax e Ymin como sigue:

def Ymax(p):
    max=p[0]
    for i in p:
        if(i[1]>max[1]):
            max=i
    return max
    
def Ymin(p):
    min=p[0]
    for i in p:
        if(i[1]<min[1]):
            min=i
    return min
    
#pero podemos utilizar una función de comparación:

def comparacion(x):
    return([x[1],x[0]])
            
def Ymax(p):
    return max(p,key=comparacion)
   
#Las dos últimas funciones se pueden sustituir por una funcion con una función anónima de comparación:

def Ymax(p):
    return max(p,key=lambda x:[x[1],x[0]]) #Si dos x[1] coinciden se mira x[0]

def Ymin(p):
    return min(p,key=lambda x:[x[1],x[0]])   
    
# # Ejecutamos las funciones sobre una lista completa
# show(Xmax([[1,2],[6,4],[8,5],[7,1]]))
# show(Xmin([[1,2],[6,4],[8,5],[7,1]]))
# show(Ymax([[1,2],[6,4],[8,5],[7,1]]))
# show(Ymin([[1,2],[6,4],[8,5],[7,1]]))
    


# In[15]:


#Probamos estas funciones en una nube de puntos generados aleatoriamente

# p=[[random(),random()] for i in range(100)]
# point(p,aspect_ratio=1)+point(Ymax(p),color="red",size=50)+point(Ymin(p),color="green",size=50)+point(Xmax(p),color="blue",size=50)+point(Xmin(p),color="orange",size=50)


# ### Problema 2: 
# **Puntos extremos según una dirección**

# In[25]:


# 2. Dada una lista de puntos p y un vector V, hallar los puntos máximos y mínimos respecto de la dirección del vector v

#    Ordenamos por el producto escalar con el vector v=(a,b), pues realmente lo que hacemos el proyectar el vector que 
#    representa cada punto sobre el vector v y nos vamos quedando con la menor o mayor proyección según lo que queramos.
#    Pero si el producto escalar es 0 al haber puntos en la perpendicular al vector, o dos productos escalares son
#    iguales, entonces ordenamos por el vector (-b,a)

def Vmax(p,v):
    return max(p,key=lambda x:[x[0]*v[0]+x[1]*v[1],-x[0]*v[1]+x[1]*v[0]])
    
def Vmin(p,v):
     return min(p,key=lambda x:[x[0]*v[0]+x[1]*v[1],-x[0]*v[1]+x[1]*v[0]])


# In[26]:


# Vmax(p,[1,0.75])


# In[29]:


# p=[[random(),random()] for i in range(100)]
# u=vector([1,0.75])
# u.plot(color="orange")+point(p,aspect_ratio=1)+point(Vmax(p,[1,1]),color="red",size=50)+point(Vmin(p,[1,1]),color="green",size=50)


# In[6]:


# Si coinciden varios maximos o mínimos en la perpendicular a v, buscamos en la dirección (-b,a) el más alejado como hemos
# explicado antes. Así, si añadimos los puntos (1,-1),(3,-3),(2,-2),(0,2), se tiene:

# p+=[[1,-1],[3,-3],[2,-2],[0,2]]
# u.plot(figsize=12,color="orange")+point(p,aspect_ratio=1)+point(Vmax(p,[1,1]),color="red",size=50)+point(Vmin(p,[1,1]),color="green",size=50)


# In[7]:


# u=vector([1,1])
# # Si queremos borrar algún elemento de una lista usamos p.remove([3,-3]), por ejemplo
# p.remove([3,-3])
# u.plot(figsize=8,color="orange")+point(p,aspect_ratio=1)+point(Vmax(p,[1,1]),color="red",size=50)+point(Vmin(p,[1,1]),color="green",size=50)


# ### Problema 3: 
# **Pendiente máxima y mínima**

# In[30]:


# 3. Dada una lista de puntos p de coordenadas positivas, hallar el punto cuyo vector de posición 
#    tiene pendiente mínima y el que tiene pendiente máxima.

def pendienteMinima(p):
    return min(p,key = lambda x:[x[1]/x[0],dist([0,0],x)])
    
    
def pendienteMaxima(p):
    return max(p,key = lambda x:[x[1]/x[0],dist([0,0],x)])
    


# In[31]:


# p=[[random(),random()] for i in range(25)]
# sum(line([i,[0,0]],color="orange") for i in p)+point(p,aspect_ratio=1)+point(pendienteMinima(p),color="red",size=50)+point(pendienteMaxima(p),color="green",size=50)


# In[32]:


#Si no cabe todo en una línea también podemos dividir las gráficas de la siguiente forma
# g1=sum(line([i,[0,0]],color="orange") for i in p)+point(p,aspect_ratio=1)+point(pendienteMinima(p),color="red",size=50)
# g2=point(pendienteMaxima(p),color="green",size=50)
# g1+g2


# ### Problema 4: 
# **Ordenación por abscisas**

# In[33]:


# 4. Ordenación de una lista de puntos por abscisas.
#    Dada una lista de puntos p, obtener una lista L que contenga los puntos de p 
#    ordenados por sus abscisas.

def ordenX(p):
    return sorted(p)
    


# In[34]:


# p=[[0,-1],[3,0],[-1,2],[2,1],[1,1]]
# ordenX(p)


# In[35]:


#¿Cómo ordenaríamos por el método de la burbuja?

def ordenXBurbuja(p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if(p[j][0]<p[i][0]):
                aux=p[i]
                p[i]=p[j]
                p[j]=aux
     
    return(p)              


# In[36]:


# p=[[0,-1],[3,0],[-1,2],[2,1],[1,1]]
# ordenXBurbuja(p)


# In[11]:


# Una función para medir tiempos podría ser:

from time import time

def tiempos(funcion,m,s,n):
    l=[]
    l1=[]
    for i in range(s,m,s):
        suma=0
        suma1=0
        for k in range(n):
            p=[[random(),random()] for j in range(i)]
            t0=time()
            r=funcion(p)
            t1=time()
            suma+=(t1-t0)
            
          
            t0=time()
            r=sorted(p)
            t1=time()
            suma1+=(t1-t0)
        
        l.append([i,suma/n])
        l1.append([i,suma1/n])
    return(l,l1)


# In[13]:


# line(tiempos(ordenXBurbuja,100,5,10)[0],color="green")+line(tiempos(ordenXBurbuja,100,5,10)[1],color="red")


# In[14]:


#Podemos comparar los tiempos de sorted con nlogn y ver que nlogn es cota superior
# line(tiempos(ordenXBurbuja,500,5,10)[1],color="red")+plot(0.000000025*x*ln(x),x,0,500)


# In[12]:


#Podemos incluir incluso los tiempos de la burbuja
# line(tiempos(ordenXBurbuja,500,5,10)[1],color="red")+plot(0.0000025*x*ln(x),x,0,500)+line(tiempos(ordenXBurbuja,500,5,10)[0],color="green")


# ### Problema 5: 
# **Ordenación por ordenadas**

# In[40]:


# 5. Ordenación de una lista de puntos por ordenadas.
#    Dada una lista de puntos p, obtener una lista L que contenga los puntos de p 
#    ordenados por sus ordenadas.

def ordenY(p):
    return sorted(p,key=lambda x:[x[1],x[0]])
    


# In[41]:


# p=[[2,-1],[0,0],[0,2],[-1,1],[1,1],[0,-1]]
# ordenY(p)


# ### Problema 6: 
# **Ordenación según una dirección**

# In[39]:


# 6. Ordenación de una lista de puntos según una dirección.
#    Dada una lista de puntos p, obtener una lista L que contenga los puntos de p ordenados 
#    según la dirección de un vector v.

def ordenV(p,v):
    return sorted(p,key=lambda x: [x[0]*v[0]+x[1]*v[1],-x[0]*v[1]+x[1]*v[0]])
    


# In[42]:


# p=[[0,0],[-1,1],[1,-1],[2,3],[-4,-2]]
# v=[1,1]
# ordenV(p,v)


# In[43]:


# u=vector([1,1])
# u.plot(figsize=6,color="orange")+sum(point(p[i],aspect_ratio=1,size=50)+text(p[i],[p[i][0],p[i][1]+0.3])for i in range(len(p)))


# ### Problema 7: 
# **Ordenación angular respecto de un punto**

# In[19]:


# 7. Ordenación angular de una lista de puntos respecto de un punto.
#    Dada una lista de puntos p y un punto C, obtener una lista L que contenga los puntos de p 
#    ordenados angularmente respecto del punto C.

def ordenAngularMalaI(p,C):
    return sorted(p,key = lambda x:[(x[1]-C[1])/(x[0]-C[0]),dist(C,x)])
    
# p=[[random(),random()] for i in range(30)]
# C=[1/2,1/2]
# line(ordenAngularMalaI(p,C))+point(C,color="red",size=50)

#El problema de este método es que no el tercer cuadrante las tangentes también son positivas y ordena mal. 


# In[20]:


# Otra forma podría ser:

def ordenAngularMalaII(p,C):
    derecha=[]
    izquierda=[]
    for i in p:
        if i[0]>C[0]or i[0]==C[0] and i[1]>=C[1]:
            derecha.append(i)
        else:
            izquierda.append(i)
    derecha=sorted(derecha,key=lambda x:[(x[1]-C[1])/(x[0]-C[0]),dist(x,C)])
    izquierda=sorted(izquierda,key=lambda x:[(x[1]-C[1])/(x[0]-C[0]),dist(x,C)])
    return (derecha+izquierda+[derecha[0]])

#Se añade el punto derecha[0] para que cierre el polígono por la parte inferior


# In[21]:


# p=[[random(),random()] for i in range(100)]
# C=[random(),random()]
# line(ordenAngularMalaII(p,C))+point(C,color="red",size=50)


# In[22]:



#Vemos que esta segunda forma no funciona como está, pues en el momento que un punto tiene igual abscisa que el punto C
#nos aparece una división por 0

# p=[[2,3],[2,2],[-2,-2],[1,1],[1,1],[0,3],[-1,2]]
# ordenAngularMalaII(p,[0,0])


# In[56]:


def ordenAngular(p,C):
    derecha=[]
    izquierda=[]
    superior=[]
    inferior=[]
    for i in p:
        if i[0]>C[0]:
            derecha.append(i)
        elif i[0]<C[0]:
            izquierda.append(i)
        elif i[0]==C[0] and i[1]>C[1]:
            superior.append(i)
        elif i[0]==C[0] and i[1]<C[1]:
            inferior.append(i)
        
    derecha=sorted(derecha,key=lambda x:[(x[1]-C[1])/(x[0]-C[0]),dist(x,C)])
    izquierda=sorted(izquierda,key=lambda x:[(x[1]-C[1])/(x[0]-C[0]),dist(x,C)])
    superior=sorted(superior)
    inferior=sorted(inferior)
    if C in p:
        return [C]+derecha+superior+izquierda+inferior
    else:
        return derecha+superior+izquierda+inferior
    


# In[24]:


# p=[[0,0],[2,2],[-2,-2],[1,1],[0,2],[0,-1],[1,0],[0,3],[-1,2]]
# ordenAngular(p,[0,0])


# In[25]:


# line(ordenAngular(p,[0,0]))


# In[27]:


# p=[[random(),random()] for i in range(100)]
# C=[random(),random()]
# line(ordenAngular(p,C))+point(C,color="red",size=50)


# In[28]:


# Así, podemos generar una lista de puntos y ordenar con respecto al primer punto, generando un polígono 

# p=[[random(),random()] for i in range(100)]
# point(p[0],color="red",size=50)+point(p)+polygon(ordenAngular(p,p[0]),alpha=.3)


# In[31]:


# Si el punto de ordenación no está dentro del cierre convexo, podemos tener la siguiente solución:

#p=[[0.05,1]]+[[random(),random()] for i in range(100)]
#del p[0]
# point([0.05,1],color="red",size=50)+point(p)+line(ordenAngular(p,[0.05,1]),alpha=.3)


# ## Aplicaciones de las funciones de ordenación

# ### Problema 8: 
# **Poligonización de puntos según el eje x**

# In[45]:


# 8.  Poligonización de puntos.
#     El problema consiste en obtener un polígono simple cuyos vértices sean los puntos 
#     de una lista de puntos dada.

#  Poligonización monótona en abscisas:

#   1. Ordenar los puntos por sus abscisas en una lista L
#   2. Sean pmin y pmax el primer y el último punto. Suprimirlos de la lista L.
#   3. Descomponer la lista L en dos listas ordenadas por abscisas, Linf y Lsup, que contengan 
#      los puntos que están por debajo o por encima del segmento [pmin , pmax] respectivamente.
#   4. Invertir el orden de los puntos de Lsup y devolver la concatenación de las listas 
#      [pmin], Linf, [pmax], Lsup

def poligonizacionXmonotona(P):
    mi=Xmin(P)
    ma=Xmax(P)
    arriba=[]
    abajo=[]
    
    for i in P:
        if areaSignada(mi,ma,i)>=0:
            arriba.append(i)
        else:
            abajo.append(i)
    return list(reversed(ordenX(arriba)))+ordenX(abajo)


# In[46]:


# Ejecutamos un ejemplo

# p=[[random(),random()] for i in range(100)]
# point(p)+polygon(poligonizacionXmonotona(p),alpha=.3)


# ### Problema 9: 
# **Poligonización de puntos según el eje y**

# In[31]:


# 9.   Poligonización monótona en ordenadas
#    Replica el algoritmo anterior para obtener un polígono monótono respecto del eje OY

def poligonizacionYmonotona(P):
    mi=Ymin(P)
    ma=Ymax(P)
    izquierda=[]
    derecha=[]
    
    for i in P:
        if areaSignada(mi,ma,i)>=0:
            izquierda.append(i)
        else:
            derecha.append(i)
    return list(reversed(ordenY(izquierda)))+ordenY(derecha)
    


# In[32]:


# Ejecutamos un ejemplo

# p=[[random(),random()] for i in range(100)]
# point(p)+polygon(poligonizacionYmonotona(p),alpha=.3)


# ### Problema 10: 
# **Poligonización de puntos según una dirección**

# In[47]:


# 10.   Poligonización monótona respecto de la dirección de un vector.
#    Replica el mismo algoritmo para obener un polígono monótono en la dirección de un vector dado.

def poligonizacionVmonotona(P,v):
    mi=Vmin(P,v)
    ma=Vmax(P,v)
    izquierda=[]
    derecha=[]
    
    for i in P:
        if areaSignada(mi,ma,i)>=0:
            izquierda.append(i)
        else:
            derecha.append(i)
    return list(reversed(ordenV(izquierda,v)))+ordenV(derecha,v)
    


# In[53]:


# Ejecutamos un ejemplo

# p=[[random(),random()] for i in range(100)]
# v=[random(),random()]
# u=vector(v)
# u.plot(color="orange")+point(p)+polygon(poligonizacionVmonotona(p,v),alpha=.3)


# ### Problema 11: 
# **Poligonización estrellada**

# In[57]:


#  11.  Poligonización estrellada.
#     1. Hallar el baricentro B del triángulo determinado por los tres primeros puntos
#     2. Ordenar la lista angularmente respecto del punto B

def poligonizacionEstrellada(P):
    C=[(P[0][0]+P[1][0]+P[2][0])/3,(P[0][1]+P[1][1]+P[2][1])/3]
    print(C)
    return (ordenAngular(P,C),C)


# In[58]:


# Ejecutamos un ejemplo

# p=[[random(),random()] for i in range(100)]
# v=[random(),random()]
# point(p)+polygon(poligonizacionEstrellada(p)[0],alpha=.3)+point(poligonizacionEstrellada(p)[1],color="red",size=30)


# ### Problema 12: 
# **Poligonización propia**

# In[ ]:


#  12.  Diseña tu propio algoritmo para poligonizar una lista de puntos.

def poligonizacionPropia(P):
    pass
    


# In[ ]:


"""¿Qué pasa si el punto de ordenación está fuera de la nube de puntos?
     - Pues que la arista que une el primer punto y el último puede cruzar el polígono.
     - Una solución: "Une el primero y el último" (ordena los que estén a un lado, luego los que estén al otro lado y ya lo 
                     puedes unir razonablemente."""

