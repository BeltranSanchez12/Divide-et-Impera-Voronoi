#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# # PRÁCTICA 3: Polígonos
# 
# * Como en la práctica anterior, en cada ejercicio debes escribir las funciones correspondientes.
# 
# * En el enunciado se especifica el nombre y las variables y se indica cuál debe ser la salida.
# 
# * También debes realizar las pruebas necesarias que muestren que la función hace lo que debe.

# ## Elementos de la práctica:
# 
# 1. Cadena poligonal. Polígono simple. Polígono monótono. Núcleo de un polígono.
# 2. Polígono estrellado. Polígono convexo.
# 3. Oreja de un polígono. Triangulación de polígonos.
# 4. Región de Voronoi. Diagrama de Voronoi.

# ## Ejercicios a resolver:
# 1. Test polígono simple
# 2. Test punto en polígono
# 3. Recorte de polígono por semiplano
# 4. Núcleo de un polígono
# 5. Test polígono estrellado
# 6. Test polígono convexo
# 7. Localización de puntos respecto de cadena poligonal monótona
# 8. Cálculo de una oreja de un polígono
# 9. Triangulación de polígonos mediante escisión de orejas
# 10. Región de Voronoi mediante intersección de semiplanos
# 11. Diagrama de Voronoi mediante intersección de semiplanos
# 

# In[1]:


# Antes de empezar cargamos todas las funciones de las prácticas anteriores

load("Biblioteca_GC.py")
load("Biblioteca2_GC.py")


# ### Problema 1: 
# **Test Polígono simple**

# In[2]:


# 1. Test polígono simple
# Escribe una función que determine si un polígono P es simple (salida true o false)

def testPoligonoSimple(P):
    n=len(P)
    for i in range(-1,n-1):
        for j in range (-1,n-1):
            if P[j] not in [P[i-1],P[i],P[i+1]] and testInterseccionSegmentos([P[i],P[i+1]],[P[j],P[j+1]]):
                return false
    return true


# In[3]:


# Q=[[0,0],[1,0],[0,1]]
# testPoligonoSimple(Q)


# In[39]:


# Ejecutamos un ejemplo
# Generamos 50 puntos aleatorio y generamos una poligonización X monótona.
# Después comprobamos si los puntos tal cual constituyen un polígono simple y la poligonización

# Q=[[random(),random()] for i in range(30)]

# # Comprobamos si el polígono es simple

# testPoligonoSimple(Q)


# In[40]:


# Efectivamente vemos que si pintamos el polígono no es simple
# Añadimos Q[0] para que se cierre el polígono

# line(Q+[Q[0]],alpha=0.6)+polygon(Q,color="orange",alpha=0.3)#+point(Q)


# In[41]:


# Poligonizamos los puntos y vemos si el polígono es simple
# Q=poligonizacionYmonotona(Q)
# print(testPoligonoSimple(Q))
# line(Q+[Q[0]],alpha=0.6)+polygon(Q,color="orange",alpha=0.3)#+point(Q)


# ### Problema 2: 
# **Test Punto en Polígono**

# In[3]:


# 2. Test punto en polígono
# Escribe una función que determine si un punto q está contenido en un polígono P (salida true o false)

def testPuntoEnPoligono(q,P):
    m=max(P)
    M=[m[0]+1,m[1]+0.001*random()]
    if q in P:
        sol=true
    else:
        cont=0
        for i in range(len(P)):
            if testInterseccionSegmentos([M,q],[P[i-1],P[i]]):
                cont+=1
              #  print("Cortes=",cont)
        if cont%2==0:
            sol=false
        else:
            sol=true
    return (sol,M)
    


# In[8]:


# Ejecutamos un ejemplo sobre el polígono generado en el Problema 1
# q=[random(),random()]
# s=testPuntoEnPoligono(q,Q)
# print(s[0])

# # Pintamos el polígono, el punto y el segmento
# line(Q+[Q[0]],alpha=0.6)+polygon(Q,color="orange",alpha=0.3)+point([s[1],q],color="red",size=10)+line([s[1],q],color="red")


# #### Un Ejemplo interesante con el Problema 2

# In[9]:


# Testeamos la función punto en polígono, generando un polígono y una lista de puntos aleatorios.
# Tras aplicar el test a cada punto de la lista, dibujamos el polígono y los puntos, distinguiendo los que están en el
# polígono en color rojo

# Q=[[random(),random()] for i in range(30)]
# P=poligonizacionXmonotona(Q)
# q=[[random(),random()] for i in range(3000)]

# dentro=[]
# fuera=[]
# for i in q:
#     if testPuntoEnPoligono(i,P)[0]:
#         dentro.append(i)
#     else:
#         fuera.append(i)
        
# polygon(P,alpha=0.3)+line(P+[P[0]],alpha=0.3)+point(dentro,color="red",size=2)+point(fuera,size=1)


# In[10]:


# Vamos a aprovechar para comparar el área del polígono con la proporción de puntos aleatorios que contiene

# print(areaPoligono(P))
# print(n(len(dentro)/len(q),digits=4))


# ### Problema 3: 
# **Recorte de Polígono por semiplano**

# In[ ]:





# In[4]:


# 3. Recorte de polígono por semiplano 
# Escribe una función que devuelva la intersección de un polígono simple P y un semiplano s
# El semiplano es el semiplano izquierdo de un segmento orientado s=[a,b]

def recortePoligonoSemiplano(P,s):
    if(len(P)==0):
        return []
    if(len(P)==1):
        if areaSignada(s[0],s[1],P[0])>=0:
            return([P[0]])
        else:
            return []
    lista=[]
    if areaSignada(s[0],s[1],P[0])>=0:
        dentro=true
        lista.append(P[0])
    else:
        dentro=false
   
    for i in range(1,len(P)):
        if areaSignada(s[0],s[1],P[i])>=-valor_cero and dentro:
            lista.append(P[i])
        elif areaSignada(s[0],s[1],P[i])>=0 and not dentro:
            lista.append(interseccionRectas([P[i-1],P[i]],s))
            lista.append(P[i])
            dentro=true
        elif areaSignada(s[0],s[1],P[i])<valor_cero and dentro:
            lista.append(interseccionRectas([P[i-1],P[i]],s))
            dentro=false          
    if(areaSignada(s[0],s[1],P[-1])*areaSignada(s[0],s[1],P[0]))<0:
        lista.append(interseccionRectas([P[-1],P[0]],s))       
    return lista


# In[7]:


# # Un ejemplo de ejecución
# P=[[random(),random()] for i in range(30)]
# P=poligonizacionXmonotona(P)
# s=[[random(),random()],[random(),random()]]
# line(P+[P[0]],alpha=0.3)+polygon(P,alpha=0.3)+polygon(recortePoligonoSemiplano(P,s),color="yellow",alpha=0.3)+line(s,color="red")+point(s[0],color="red",size=20)+point(s[1],color="green",size=20)


# ### Problema 4: 
# **Núcleo de un polígono**

# In[5]:


# 4. Núcleo de un polígono
# Escribe una función que calcule el núcleo de un polígono simple P

def nucleo(P):
    if len(P)<=1:
        return P
    N=deepcopy(P)
    
    for i in range(len(P)):
        N=recortePoligonoSemiplano(N,[P[i-1],P[i]])
    return N
    


# In[9]:


# Un ejemplo de ejecución
# P=[[random(),random()] for i in range(10)]
# P=poligonizacionXmonotona(P)
# if nucleo(P):
#     show(line(P+[P[0]],alpha=0.6)+polygon(P,alpha=0.3)+polygon(nucleo(P),color="yellow",alpha=0.3))
# else:
#     print("Núcleo vacío")
#     show(line(P+[P[0]],alpha=0.6)+polygon(P,alpha=0.3))#+point(P)


# ### Problema 5: 
# **Test polígono estrellado**

# In[6]:


# 5. Test polígono estrellado
# Escribe una función que determine si un polígono simple P es estrellado (salida true o false)

def testEstrellado(P):
    if nucleo(P):
        return(true)
    else:
        return (false)
    


# In[16]:


# Un ejemplo de ejecución
# P=[[random(),random()] for i in range(10)]
# PM=poligonizacionXmonotona(P)
# print("El polígono xMonotono es estrellado:",testEstrellado(PM))
# if (nucleo(PM)==[]):
#     print("Núcleo vacío")
#     show(line(PM+[PM[0]],alpha=0.6)+polygon(PM,alpha=0.3))
# else:
#     show(line(PM+[PM[0]],alpha=0.6)+polygon(PM,alpha=0.3)+polygon(nucleo(PM),color="yellow",alpha=0.3))


# ### Problema 6: 
# **Test polígono convexo**

# In[7]:


# 6. Test polígono convexo
# Escribe una función que determine si un polígono P es convexo

def testConvexo(P):
    if len(P)<=3:
        return true
    for i in range(len(P)):
        if areaSignada(P[i-2],P[i-1],P[i])<0:
            return false
    return true
    


# In[19]:


# # Un ejemplo de ejecución

# P=[[random(),random()] for i in range(5)]
# PM=poligonizacionXmonotona(P)
# print("El polígono es convexo:",testConvexo(PM))
# if (nucleo(PM)==[]):
#     print("Núcleo vacío")
#     show(line(PM+[PM[0]],alpha=0.6)+polygon(PM,alpha=0.3))
# else:
#     show(line(PM+[PM[0]],alpha=0.6)+polygon(PM,alpha=0.3)+polygon(nucleo(PM),color="yellow",alpha=0.3))


# ### Problema 7: 
# **Localización respecto a poligonas monótona**

# In[8]:


# 7. Localización de puntos respecto de cadena poligonal monótona.
# Escribe una función que determine si un punto q está encima o debajo de una cadena poligonal X-monótona C
# La ordenada del punto q debe estar comprendida entre las ordenadas del primer y último vértice de C
# La salida debe ser true si está encima y false si está debajo

# NOTA
# Este ejercicio tiene como objetivo analizar la complejidad de la búsqueda binaria (O(logn))
# Dicha complejidad exige disponer de los datos ordenados en memoria
# En la siguiente solución es un punto esencial el hecho de que la listas de Python contienen como información su longitud
# (len()), por lo que la función len() tiene complejidad O(1)

def localizacionCadenaXmonotona(q,C):
    if q[0]<C[0][0] or q[0]>C[-1][0]:
        print("Fuera de rango")
        return
    n=len(C)
    i=0
    j=n-1
    while j>i+1:
        k=int((i+j)/2)
        if q[0]<=C[k][0]:
            j=k
        else:
            i=k
    return areaSignada(C[i],C[j],q)>=0
    


# In[21]:


# Veamos un ejemplo de ejecución
# Q=[[random(),random()] for i in range(30)]
# C=sorted(Q)
# q=[random(),random()]
# r=localizacionCadenaXmonotona(q,C)
# if r==true:
#     print("\n El punto esta encima de C")
# else:
#     print("\n El punto está debajo de C")

# line(C)+point(q,color="red",size=15)


# ### Problema 8: 
# **Cálculo de una oreja en un polígono**

# In[9]:


# 8. Cálculo de una oreja de un polígono
# Escribe una función que devuelva un vértice oreja de un polígono simple P
# La salida es el índice del vértice oreja en la lista

def testOreja(P,i):
    n=len(P)
    if areaSignada(P[i-1],P[i],P[i+1%n])<0:
        return false
    
    for j in range(n):
        if j!=(i-1)%n and j!=i and j!=(i+1)%n and enTriangulo(P[j],[P[(i-1)%n],P[i],P[(i+1)%n]]):
            return false
    return true

def buscaOreja(P):
    for i in range(len(P)):
        if testOreja(P,i):
            return int(i)   


# In[24]:


# Un ejemplo de ejecución para buscar una oreja
# Q=[[random(),random()] for i in range(15)]
# P=poligonizacionXmonotona(Q)
# o=buscaOreja(P)
# line(P+[P[0]],alpha=0.3)+polygon(P,alpha=0.3)+point(P)+polygon([P[o-1],P[o],P[(o+1)%len(P)]],color="red",alpha=0.3)   


# In[25]:


# Un ejemplo INTERACTIVO en el que vamos construyendo k orejas, que justo la idea de la triangulación por orejas 
# un polígono.
# \033[1m y \33[0m es par escribir en negrita
# print('\033[1m'+'TRIANGULACIÓN POR OREJAS DE UN POLÍGONO'+ '\033[0m')

# @interact
# def pedirVertices(v=slider(3,25,1,3,label='Vértices:')):
#     Q=[[random(),random()] for i in range(v)]
#     #P=poligonizacionXmonotona(Q)
#     @interact
#     def generaPoligono(Polígono=selector([(1,'Xmonótono'),(2,'Ymonónoto')])):
#         if Polígono==1:
#             P=poligonizacionXmonotona(Q)
#         else:
#             P=poligonizacionYmonotona(Q)
#         @interact
#         def dibujadokOrejas(k=slider(0,len(P)-2,1,0,label='Oreja:')):
#             T=[]
#             n=len(P)
#             if n<=3:
#                 T.append(P)   
#             S=deepcopy(P)
        
#             for i in range(k):
#                 j=buscaOreja(S)
#                 T.append([S[j-1],S[j],S[(j+1)%n]])
#                 del S[j]
        
#             show(line(P+[P[0]],alpha=0.3)+polygon(P,alpha=0.3)+point(P)+sum(polygon(i,alpha=0.3,color="red") for i in T)+            sum(line(i+[i[0]],color="green",alpha=0.2) for i in T))



# ### Problema 9: 
# **Triangulación de polígonos mediante escisión de orejas**

# In[10]:


# 9. Triangulación de polígonos mediante escisión de orejas
# Escribe una función que devuelva una triangulación de un polígono P
# La salida es una lista de triángulos definidos por los índices de los vértices en la lista P
# Indicación: Iterar el cálculo de orejas y la eliminación del vértice oreja

def triangulacionOrejas(P):
    n=len(P)
    T=[]
    if n<=3:
        T.append(P)
        return T
    Q=deepcopy(P)
    #for i in range(n-2):
    while (len(Q)>=3):
        j=buscaOreja(Q)
        T.append([Q[j-1],Q[j],Q[(j+1)%n]])
        del Q[j]
        n=n-1
    return T
    


# In[29]:


# Un ejemplo de ejecución para triangular un polígono
# Q=[[random(),random()] for i in range(30)]
# P=poligonizacionXmonotona(Q)
# T=triangulacionOrejas(P)
# sum(line(i,alpha=0.4) for i in T)+polygon(P,alpha=0.3)+point(P)


# ### Problema 10: 
# **Región de Voronoi mediante intersección de semiplanos**

# In[11]:


# 10. Región de Voronoi mediante intersección de semiplanos
# Escribe una función que devuelva la región de Voronoi de un punto P[i] respecto de una lista de puntos P
# Indicación: Partiendo de un rectángulo suficientemente grande R,
# recortarlo de forma iterada con los semiplanos determinados por las mediatrices de P[i] y P[j] ,
# para j distinto de i , que contienen a P[i]

def mediatriz(a,b):
    
    if a == b:
        return
    ab = [b[0]-a[0],b[1]-a[1]]
    abo = [-ab[1],ab[0]]
    m = puntoMedio(a,b)
    
    return [m, [m[0]+abo[0],m[1]+abo[1]]]

def regionVoronoi(P,i):
    
    h = Xmax(P)[0] - Xmin(P)[0]
    v = Ymax(P)[1] - Ymin(P)[1]
    
    R = [[Xmin(P)[0]-h,Ymin(P)[1]-v],[Xmax(P)[0]+h,Ymin(P)[1]-v],[Xmax(P)[0]+h,Ymax(P)[1]+v],[Xmin(P)[0]-h,Ymax(P)[1]+v]]
    
    for j in range(len(P)):
        if j != i:
            R = recortePoligonoSemiplano(R,mediatriz(P[i],P[j]))
    return R        


# ### Problema 11: 
# **Dibujar Región de Voronoi mediante intersección de semiplanos**

# In[17]:


# 11. Diagrama de Voronoi mediante intersección de semiplanos
# Escribe una función que dibuje el diagrama de Voronoi de una lista de puntos P

def Voronoi(P):
    return [regionVoronoi(P,i) for i in range(len(P))]

def dibujaVoronoi(P,ax = 0):
    
    V = Voronoi(P)
    
    return sum(line(i + [i[0]],aspect_ratio=1,axes = ax,alpha=0.2) for i in V) + point(P,size=7)


# In[22]:


# Una primera ejecución para calcular la región de Voronoi de un número entero aleatorio entre 0 y len(P)

# P  = [[gauss(1,2),gauss(2,1)] for i in range(30)]
# show(point(P) + polygon(regionVoronoi(P,randint(0,len(P))),alpha=.3))
# show(dibujaVoronoi(P,1))
# show(dibujaVoronoi(P))


# In[48]:


# análisis experimental de la complejidad

# line(tiempos(Voronoi, 1000 , 50 , 2)[0])+plot(0.00001*x**2,0,1000,color="red")


# In[40]:


# Para ver que realmente el cálculo de una región eslineal

def regionVoronoi0(P):
    return regionVoronoi(P,0)   
# análisis experimental de la complejidad

# line(tiempos(regionVoronoi0, 1000 , 50 , 2)[0])+plot(0.00002*x,0,1000,color="red")


# In[23]:


#Un ejemplo de ejecución para el Diagrama de Voronoi interactivo
# @interact
# def pedirPuntos(p=slider(1,50,1,1,label='Puntos:')):
#     @interact
#     def generaPuntos(Distribución=selector([(1,'Uniforme'),(2,'Normal')])):
#         if Distribución==1:
#             P  = [[random(),random()] for i in range(p)]
#         else:
#             P  = [[gauss(1,2),gauss(2,1)] for i in range(p)]
   
#         V=Voronoi(P)
#         @interact
#         def dibujarPuntos(showEjes = checkbox(False, "Mostar Ejes"),showpoints = checkbox(False, "Mostar Voronoi"),showregiones=checkbox(False, "Mostar Regiones"),        showBorrar=checkbox(False, "Actualizar")):
#             if showpoints==False and showregiones==False:
#                 show()
#             elif showpoints==True and showregiones==False:
#                 show(sum(line(i + [i[0]],aspect_ratio=1,axes = showEjes,alpha=0.2) for i in V) + point(P,size=7))
#             elif showregiones==True:
#                 show(sum(line(i + [i[0]],aspect_ratio=1,axes = showEjes,alpha=0.2)+polygon(i,color=(random(),random(),random()),                alpha=.3) for i in V) + point(P,size=7))
                    
                  

