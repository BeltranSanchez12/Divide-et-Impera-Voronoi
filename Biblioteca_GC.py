#!/usr/bin/env python
# coding: utf-8

# ![Encabezado-7.JPG](attachment:Encabezado-7.JPG)

# # PRÁCTICA 1: Funciones básicas
# 
# * En cada ejercicio debes escribir las **funciones correspondientes** (en el enunciado se especifica el nombre y las
# variables y se indica cuál debe ser la salida).
# También debes realizar las pruebas necesarias que muestren que la función hace lo que debe.
# 
# * Una salida gráfica es, en ocasiones, una buena manera de verificar el resultado.
# 
# * Las pruebas deben ser de dos tipos:
# 
#     * Con *datos aleatorios*.
# 
#     * Con datos *elegidos* especialmente para verificar los casos especiales.
# 
# * En el apéndice al final tienes indicaciones sobre generación aleatoria de datos y representación gráfica de los mismos.

# ## Elementos de la práctica:
# 
# 1. Representación de puntos, listas de puntos, segmentos, triángulos, polígonos, círculos.
# 
# 2. Área signada de un triángulo. Área de un polígono simple.
# 
# 3. Intersección de segmentos, semirrectas y rectas.
# 
# 
# 

# ### Problema 1: 
# **Distancia entre dos puntos**

# In[2]:


# 1. Distancia entre dos puntos p=[px,py], q=[qx,qy]. 
#    La salida es el valor numérico correspondiente.

def dist(p,q):
    
    return sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

# dist([0,0],[1,2])

# Si queremos calcular el valor aproximado utilizamos n, N, numerical_approx, que son sinónimos

# n(dist([0,0],[1,1]),digits=12)


# In[3]:


# Si queremos que se impriman varios elementos en una celda, utilizamos la función print

# print(dist([0,0],[1,1]))
# n(dist([0,0],[1,1]),digits=12)


# ### Problema 2: 
# **Punto medio**

# In[4]:


# 2. Punto medio de dos puntos p=[px,py], q=[qx,qy]. 
#    La salida es un punto con el mismo formato [mx,my].

def puntoMedio(p,q):
     return ([(p[0]+q[0])/2,(p[1]+q[1])/2])

#  Ejecutamos la función

# puntoMedio([2,2],[1,1])
    


# ### Problema 3: 
# **Area signada**

# In[5]:


# 3. Area signada del triángulo determinado por tres puntos a,b,c. 
#    La salida es el valor numérico del area signada del triangulo abc.

def areaSignada(a,b,c):
    return((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2

# Ejecutamos la función

# areaSignada([0,0],[2,0],[0,2])


# In[6]:


# areaSignada([0,0],[0,2],[2,0])


# ### Problema 4: 
# **Test punto en segmento**

# In[7]:


# 4. Test punto en segmento 
#    Entrada un punto p = [x,y] y un segmento s = [[a1,a2],[b1,b2]]  determinado por sus extremos . 
#    La salida es true o false.

def enSegmento(p,s):
    if areaSignada(p,s[0],s[1])!=0: # compruebo si el punto está en la 'dirección' del segmento
        return false
    return float(dist(p,s[0]))+float(dist(p,s[1]))==float(dist(s[0],s[1]))  # Comprobar si está dentro del segmento en sí

# LLamamos a la función
# Cuidado con Sage, pues si los ejemplos son enteros considera que manejamos enteros y podría no obtener el valor final.

# enSegmento([1,1],[[0,0],[2,2]])


# # In[8]:


# print(enSegmento([2,0],[[0,0],[2,2]]))
# line([[0,0],[2,2]])+point([2,0],color="blue",size=40)


# # In[9]:


# # Podemos comproba el tiempo de ejecución
# get_ipython().magic('time enSegmento([2,0],[[0,0],[2,2]])')


# In[10]:


# Podemos definir también la función:

# Es necesario mirar que la x y la y del punto están en el rango, las dos, pues el segmento podría ser vertical paralelo al
# eje y

def enSegmentoII(p,s):
    if areaSignada(p,s[0],s[1])!=0:
        return false
    if s[0][0]<=p[0] and p[0]<=s[1][0] or s[0][0]>=p[0] and p[0]>=s[1][0]:
        if s[0][1]<=p[1] and p[1]<=s[1][1] or s[0][1]>=p[1] and p[1]>=s[1][1]:
            return true
    return false

# enSegmentoII([1,1],[[0,0],[2,2]])


# ### Problema 5: 
# **Test punto en triángulo**

# In[11]:


# 5. Test punto en triangulo. 
#    Entrada un punto p=[x,y] y un triángulo dado por una lista con sus tres vértices. 
#    Salida true o false.

def enTriangulo(p,t):
    a1=areaSignada(t[0],t[1],p)
    a2=areaSignada(t[1],t[2],p)
    a3=areaSignada(t[2],t[0],p)
    
    if a1>=0 and a2>=0 and a3>=0 or a1<=0 and a2<=0 and a3<=0:
        return true
    else:
        return false
    
# # Ejecutamos la función sobre un triangulo
# p=[random()*2,random()*1]
# print("¿El punto está dento del triangulo? Respuesta=", enTriangulo(p,[[0,0],[3,0],[3,3]]))
# polygon([[0,0],[3,0],[3,3]],color="green",alpha=.20)+point(p,color="red",size=30)


# ### Problema 6: 
# **Test intersección de segmentos**

# In[123]:


# 6. Test de intersección de segmentos. 
#    La entrada son dos segmentos con formato [[a1,a2],[b1,b2]]. 
#    La salida es true o false.

def testInterseccionSegmentos(p,q):
    if (areaSignada(p[0],p[1],q[0])*areaSignada(p[0],p[1],q[1])<0 and areaSignada(q[0],q[1],p[0])*areaSignada(q[0],q[1],p[1])<0):
        return True
    else:
        if enSegmento(p[0],q) or enSegmento(p[1],q) or enSegmento(q[0],p) or enSegmento(q[1],p):
            return False
        else:
            return False

# Ejecutamos la función en un ejemplo

# p=[[random(),random()],[random(),random()]]
# q=[[random(),random()],[random(),random()]]
# print(testInterseccionSegmentos(p,q))
# line(p)+line(q)+point(p[0],color="green",size=30)+point(q[0],color="red",size=30)


# ### Problema 7: 
# **Test intersección recta y segmento**

# In[13]:


# 7. Test de intersección de recta y segmento. 
#    La entrada es una recta determinada por dos puntos dados en una lista r = [[a1,a2],[b1,b2]] 
#    y un segmento determinado por sus extremos con el mismo formato. 
#    La salida es true o false.

def testInterseccionRectaSegmento(r,s):
    if areaSignada(r[0],r[1],s[0])*areaSignada(r[0],r[1],s[1])>0:
        return false
    else:
        return true

# Ejecutamos la función en un ejemplo

# print(testInterseccionRectaSegmento([[0,0],[1,1]],[[2,1],[0,2]]))
# line([[0,0],[1,1]])+line([[2,1],[0,2]])
    


# In[14]:


# Sin embargo vemos la difencia en caso de ser segmentos

# testInterseccionSegmentos([[0,0],[1,1]],[[2,1],[0,2]])


# ### Problema 8: 
# **Punto intersección de dos rectas**

# In[15]:


# 8. Punto de intersección de dos rectas (definidas por dos puntos cada una). 
#    La salida es un punto o mensaje de error.

def interseccionRectas(r,s):
    x1=r[1][1]-r[0][1] # Diferencias en y
    y1=r[0][0]-r[1][0] # Diferencias en x
    
    x2=s[1][1]-s[0][1] # Diferencias en y
    y2=s[0][0]-s[1][0] # Diferencias en x
    if x1*y2-x2*y1==0:
        print("\n* Rectas paralelas. ", end="")
        return None
    else:
        z1=r[0][0]*r[1][1]-r[0][1]*r[1][0]
        z2=s[0][0]*s[1][1]-s[0][1]*s[1][0]
        x=(z1*y2-z2*y1)/(x1*y2-x2*y1)
        y=(x1*z2-x2*z1)/(x1*y2-x2*y1)
        return [x,y]
        
# # Llamamos a la función
# p=interseccionRectas([[0,0],[1,1]],[[2,1],[0,2]])
# print("El punto de corte es:",p,".")
# line([[0,0],[1,1]])+line([[2,1],[0,2]])+point(p,color="red",size=30)
   


# In[16]:


# p=interseccionRectas([[0,0],[1,1]],[[1,0],[0,2]])
# print("El punto de corte es:",p,".")
# if(p==None):
#     show(line([[0,0],[1,1]])+line([[1,0],[0,2]]))
# else:
#     show(line([[0,0],[1,1]])+line([[1,0],[0,2]])+point(p,color="red",size=30))  

#     #Si no se pone así fallaría cuando son paralelas   


# In[17]:


# También podemos generar aleatoriamente las rectas

# r=[[random(),random()],[random(),random()]]
# s=[[random(),random()],[random(),random()]]
# p=interseccionRectas(r,s)
# print("El punto de corte es:",p,".") 
# if(p!=None):
#     show(line(r)+line(s)+point(p,color="red",size=30))
# else:
#     show(line(r)+line(s))


# ### Problema 9: 
# **Circuncentro de tres puntos**

# In[18]:


# 9. Circuncentro del triángulo abc. 
#     La salida es un punto o un mensaje de error.

# Podemos calcular directamente el circuncentro, calculando la intersección de las rectas

def circuncentro(a,b,c):
    mx=2*(b[0]-a[0])
    my=-2*(a[1]-b[1])
    m=b[0]^2-a[0]^2+b[1]^2-a[1]^2
    nx=2*(c[0]-a[0])
    ny=-2*(a[1]-c[1])
    n=c[0]^2-a[0]^2+c[1]^2-a[1]^2
    if mx*ny-nx*my==0:
        print("puntos alineados")
        return 
    x=(m*ny-n*my)/(mx*ny-nx*my)
    y=(mx*n-nx*m)/(mx*ny-nx*my)
    return [x,y]


# In[19]:


# Una pequeña aplicación del circuncentro

# a= [random(),random()]
# b= [random(),random()]
# c= [random(),random()]

# cc = circuncentro(a,b,c)
# area = float((dist(cc,a)^2)*pi)
# print("area: ",area)
# circle(cc,dist(cc,a)) + point(cc) + point([a,b,c],color="red",size=20)+polygon([[0,0],[1,0],[1,1],[0,1]],alpha=.20)


# In[20]:


# También podemos utilizar la función interseccionRectas, dando dos puntos de cada una de las rectas. A cada punto
# central, le sumamos su vector director correspondiente para obtener otro punto

def circuncentro(a,b,c):
    r=[[(a[0]+b[0])/2,(a[1]+b[1])/2],[(a[0]+b[0])/2+(a[1]-b[1]),((a[1]+b[1])/2)+b[0]-a[0]]]
    s=[[(a[0]+c[0])/2,(a[1]+c[1])/2],[(a[0]+c[0])/2+(a[1]-c[1]),((a[1]+c[1])/2)+c[0]-a[0]]]
    return(interseccionRectas(r,s))


# In[21]:


# def circuncentro(a,b,c):
#     r = [[(a[0]+b[0])/2,(a[1]+b[1])/2],[(a[0]+b[0])/2 + (a[1]-b[1]), ((a[1]+b[1])/2) + b[0]-a[0]]]
#     s = [[(a[0]+c[0])/2,(a[1]+c[1])/2],[(a[0]+c[0])/2 + (a[1]-c[1]), ((a[1]+c[1])/2) + c[0]-a[0]]]
#     return(interseccionRectas(r,s))

# # Una pequeña aplicación del circuncentro

# a= [random(),random()]
# b= [random(),random()]
# c= [random(),random()]

# print(a,b,c)
# cc = circuncentro(a,b,c)
# area = float((dist(cc,a)**2)*pi)
# print("area: ",area)
# circle(cc,dist(cc,a)) + point(cc) + point([a,b,c],color="red",size=20)+polygon([[0,0],[1,0],[1,1],[0,1]],alpha=.20)


# ### Problema 10: 
# **Test punto en círculo**

# In[22]:


# 10. Test punto en circulo. 
#    Entrada cuatro puntos a,b,c,d  
#    salida true o false dependiendo de que el punto d este incluido en el circulo que determinan a,b y c.


def enCirculoI(a,b,c,d):
    cc=circuncentro(a,b,c)
    if(dist(cc,d)<=dist(cc,a)):
        return true
    else:
        return false
    


# In[23]:


# Un ejemplo
# get_ipython().magic('time enCirculoI([-1,0],[3,0],[1,3],[0,0])')
# print(enCirculoI([-1,0],[3,0],[1,3],[0,0]))
# circle([1,0],2)+point([[-1,0],[1,2],[3,0]],color="blue",size=30)+point([0,0],color="red",size=30)


# In[24]:


# Este método para ver si un punto es interior a un círculo puede tener alguna dificultad, además de ser más lento que
# el método que veremos a continuación usando el volumen signado.

# La desventaja de calcular el circuncentro es que, si los tres puntos que definen el círculo están "muy alineados", 
# el circuncentro se va "muy" lejos y hay dos problemas:

#  1. Muy pequeños errores en los datos (coordenadas de los puntos) pueden provocar grandes errores en el 
#     resultado (coordenadas del circuncentro).
#  2. Las coordenadas del circuncentro pueden resultar inmanejables por ser excesivamente grandes.


# In[25]:


# Para obtener una función más robusta podemos emplear numpy para calcular en volumen signado.

import numpy as np # para poder usar la función numpy.linalg.det()
def enCirculo(a,b,c,d):
    
    t=matrix([[1,1,1],[a[0],b[0],c[0]],[a[1],b[1],c[1]]])
    dt=np.linalg.det(t)
    if dt==0:
        print ("alineados")
        return 
    m=matrix([[1,1,1,1],[a[0],b[0],c[0],d[0]],[a[1],b[1],c[1],d[1]],[a[0]**2+a[1]**2,b[0]**2+b[1]**2,c[0]**2+c[1]**2,d[0]**2+d[1]**2]])
#     for row in m:
#         print(row)
    dm=np.linalg.det(m)
    print(dt,dm)
    return dt*dm<=0
    


# In[26]:


import numpy as np # para poder usar la función numpy.linalg.det()
def enCirculo(a,b,c,d):
    t = matrix([[1,1,1],[a[0],b[0],c[0]],[a[1],b[1],c[1]]])
    dt=np.linalg.det(t)
    if dt == 0:
        print('Puntos alineados')
        return 
    m = matrix([[1,1,1,1],[a[0],b[0],c[0],d[0]],[a[1],b[1],c[1],d[1]],[a[0]**2+a[1]**2,b[0]**2+b[1]**2,c[0]**2+c[1]**2,d[0]**2+d[1]**2]])
    dm=np.linalg.det(m)
    if dt * dm <= 0:
        return True
    


# In[27]:


# # Un ejemplo
# a= [random(),random()]
# b= [random(),random()]
# c= [random(),random()]
# d= [random(),random()]


# get_ipython().magic('time enCirculo(a,b,c,d)')
# print(enCirculo(a,b,c,d))
# circle(circuncentro(a,b,c), dist(circuncentro(a,b,c), a))+point([a,b,c],color="blue",size=30)+point([circuncentro(a,b,c),d],color="red",size=30)


# In[28]:


# O bien utilizamos directamente det utilizando el comando from

from numpy.linalg import * # para poder usar la función det()
def enCirculo(a,b,c,d):
    
    t=matrix([[1,1,1],[a[0],b[0],c[0]],[a[1],b[1],c[1]]])
    dt=det(t)
    if dt==0:
        print ("alineados")
        return 
    m=matrix([[1,1,1,1],              [a[0],b[0],c[0],d[0]],              [a[1],b[1],c[1],d[1]],              [a[0]**2+a[1]**2,b[0]**2+b[1]**2,c[0]**2+c[1]**2,d[0]**2+d[1]**2]])
    dm=det(m)
    return dt*dm<=0, dt, dm 


# In[29]:


# # Un ejemplo aleatorio
# a=[random(),random()]
# b=[random(),random()]
# c=[random(),random()]
# d=[random(),random()]
# cc=circuncentro(a,b,c)
# dentro, dt, dm = enCirculo(a,b,c,d)
# print(dentro, 'dt:', dt, 'dm:', dm)
# circle(cc,dist(cc,a),alpha=0.2,fill=2,facecolor="green",edgecolor="blue")+point([a,b,c],color="blue",size=30)+point(d,color="red",size=30)+point(cc,color="green",size=30)


# # PRUEBA DE TANGENTES

# In[30]:


def tangentes(poligono, p):
    vertices = []
    for i in range(len(poligono)):
#         print(poligono[i-1], poligono[i])
        a1 = areaSignada(poligono[i-1],poligono[i], p )
        a2 = areaSignada(poligono[i],poligono[(i+1)%len(poligono)], p )
#         print(poligono[i], a1,a2)
        
        if a1*a2 < 0:
            vertices.append(poligono[i])
        
    return vertices


# In[31]:


# a=[random(),random()]
# b=[random(),random()]
# c=[random(),random()]
# d=[random(),random()]
# e=[random(),random()]

# p=[random(),random()]

# poligono = [a,b,c,d,e]

def hallar_tangentes(poligono, p):
    vertices_tg = tangentes(poligono, p)
    # Graficar el polígono
    poligono_grafico = polygon(poligono, color='lightblue', alpha=0.5)  # Polígono en azul claro

    vertices = sum([point(c, color='red', size=30) for c in poligono])
    vertices2 = sum([point(c, color='blue', size=30) for c in vertices_tg])

    punto_p = point(p, color='green', size=40)  # Punto p en verde
    lineas_tg = sum([line([p, tg], color='orange', thickness=2) for tg in vertices_tg])  # Líneas en naranja


    # Mostrar la gráfica
    show(poligono_grafico + vertices + vertices2 + punto_p + lineas_tg)


# In[32]:


# # import random

# poligono1 = [(1, 1), (3, 4), (6, 3), (5, 0), (2, -1)]
# poligono2 = [(1, 1), (4, 4), (7, 1), (5, -2), (3, 0)]
# poligono3 = [[1, 1], [4, 2], [6, 1], [7, 4], [5, 5], [3, 4]]

# poligonos = [poligono1, poligono2, poligono3]

# for i in poligonos: 
#     p=[random(),random()]
#     hallar_tangentes(i, p)


# ## Aplicaciones de las funciones basicas

# ### Problema 11: 
# **Área de un polígono**

# In[33]:


# 11. Area de un polígono. 
#     Entrada una lista p con los vértices del polígono. 
#     Salida el valor numérico del área.

def areaPoligono(p):
    
    area = 0
    for i in range(1,len(p)-1):
        area += areaSignada(p[0],p[i],p[i+1])
    return area
    


# In[34]:


# P=[[0,0],[1,0.5],[2,0],[2,2],[3,2],[1,3],[0,2]]
# print(areaPoligono(P))
# polygon(P,alpha=0.3)+line(P+[P[0]])


# ### Problema 12: 
# **¿Cuántos puntos hay en un círculo?**

# In[35]:


# 12. Cuántos puntos hay en un círculo
#     Entrada: un circulo c determinado por tres puntos y una lista P de n puntos
#     Salida: el número de puntos de la lista contenidos en el círculo

def puntosEnCirculo(c,P):
    
    cont = 0
    for i in P:
        if enCirculo(c[0],c[1],c[2],i):
            cont +=1
    return cont  


# ## Ejemplos de uso de algunas funciones:
# 1. Si tiramos puntos al azar, ¿cuántos caerán sobre un segmento?
# 2. ¿Y sobre un triángulo?
# 3. ¿y sobre un círculo?
# 4. ¿Se puede conocer el área de un triángulo sabiendo cuántos puntos han caido en él?
# 5. ¿Y de un círculo?

# * ### Ejemplo 1

# In[36]:


# Genera aleatoriamente una lista de puntos en el cuadrado unidad y estudia cuantos caen en el segmento.
# Genera un segmento s al azar cuyos extremos tengan coordenadas [[0,a],[1,b]]

# ¿Podemos estimar la longitud del segmento?
# ¿Cuál dirías que es la probabilidad de que caiga un punto en el segmento?

# #Generamos puntos
# n = 20000
# P = [[random(),random()] for i in range(n)]

# #Generamos el segmento
# s =[[0,random()],[1,random()]]
# npuntos = 0
# for i in P:
#     if enSegmento(i,s):
#         npuntos += 1
# print("Puntos en el segmento: " , npuntos)        
# print("Proporción: %.15f" % (npuntos/float(n)))
# point(P,aspect_ratio=1,size=1)+line(s,alpha=.8,color="green")


# In[37]:


#¿Qué pasaría si generásemos los puntos con coordenadas enteras?

# Generamos una lista P con 10000 puntos de coordenadas enteras al azar (entre 0 y 100)
# Generamos un segmento s al azar cuyos extremos tengan coordenadas enteras [[0,a],[100,b]]
# Queremos contar cuántos puntos de P caen sobre el segmento s

# P=[[randint(0,100),randint(0,100)] for i in range(10000)]
# c = 0
# s =[[0,randint(0,100)],[100,randint(0,100)]]
# print(s)
# for i in P:
#     if enSegmento(i,s):
#         print(i)
# point(P,aspect_ratio=1,size=1)+line(s,alpha=.8,color="green")


# * ### Ejemplo 2

# In[38]:


# Para probar la función enTriangulo vamos a generar aleatoriamente un triángulo y una lista de 10000 puntos
# y vamos a contar cuántos puntos caen dentro del triángulo
#Para comprobar si la proporción de puntos contenidos en el triángulo se corresponde con el área de éste,
# compararemos la proporción entre las áreas y la proporción entre el número de puntos en el triángulo y en el cuadrado unidad
# Analiza si se puede aproximar el área de un triángulo hallando el número de puntos que contiene de una lista
# aleatoria de puntos. Haz pruebas con otras cantidades de puntos en la lista de puntos
# Compara resultados con el caso en que la lista de puntos sea esta:
#  P = [[float(i)/m,float(j)/m] for i in range(m) , for j in range(m)]
# para diferentes valores de m


# n = 22500
# P = [[random(),random()] for i in range(n)]
# '''
# Esto se prodría hacer también como:
# P=[]
# for i in range(n):
#     P.append([random(),random()])

# '''
# t = [[random(),random()],[random(),random()],[random(),random()]]
# npuntos = 0
# for i in P:
#     if enTriangulo(i,t):
#         npuntos += 1
        
# print("Puntos totales:",n)
# print("Puntos en el triangulo: " , npuntos)        
# print("Proporción: %.15f" % (npuntos/float(n)))
# print("Area triángulo: " , abs(areaSignada(t[0],t[1],t[2])))
# point(P,size=1)+polygon(t,alpha=.3,color="green")


# In[39]:


# Generamos ahora la lista en la forma:
# P = [[float(i)/m,float(j)/m] for i in range(m) , for j in range(m)]
# para diferentes valores de m

# m=150
# P = [[float(i)/m,float(j)/m] for i in range(m) for j in range(m)]
# t = [[random(),random()],[random(),random()],[random(),random()]]
# npuntos = 0
# for i in P:
#     if enTriangulo(i,t):
#         npuntos += 1
        
# print("Puntos totales:",m**2)
# print("Puntos en el triangulo: " , npuntos)        
# print("Proporción: %.15f" % (npuntos/float(m**2)))
# print("Area triángulo: " , abs(areaSignada(t[0],t[1],t[2])))
# point(P,size=1)+polygon(t,alpha=.3,color="green")


# In[40]:


# Al ser la maya más regular, aumenta el número de puntos interior al triángulo y por tanto, la estimación de su área.


# * ### Ejemplo 3

# In[41]:


# Hacemos un estudio similar para un círculo
# Para que el círculo no se salga del cuadrado unidad,generamos los puntos que lo definen de la siguiente forma:
# Tomaremos el centro del círculo en el punto [0.5,0.5]
# generaremos el radio r aleatoriamente entre 0 y 0.5
# hallaremos tres puntos aleatorios a distancia r del centro


# n = 20000
# P = [[random(),random()] for i in range(n)]
# cc = [0.5+.001*random(),0.5+.001*random()]
# r = random()/2.
# a,b,c = float(2*pi)*random() , float(2*pi)*random() ,float(2*pi)*random()
# c = [[cc[0]+r*cos(a),cc[1]+r*sin(a)],[cc[0]+r*cos(b),cc[1]+r*sin(b)],[cc[0]+r*cos(c),cc[1]+r*sin(c)]]
# npuntos = puntosEnCirculo(c,P)       
# print("puntos en el circulo: " ,npuntos )
# print("Proporción: {:.15f} ".format(npuntos/float(n)))
# print("Proporcion: %.15f " % (npuntos/float(n)))
# print("Area circulo: " , float(pi)*(dist(cc,c[0])**2))
# point(P,size=1)+circle(cc,dist(cc,c[0]),alpha=0.3,fill=2,facecolor="green",edgecolor="blue")


# In[42]:


# Podemos pedir los datos con un interactivo 

# print('\033[1m'+'APROXIMACIÓN ÁREA DE CÍRCULO'+ '\033[0m')
# @interact
def pedirVertices(Puntos=selector([(1,1),(1000,1000),(2000,2000),(3000,3000),(5000,5000),(10000,10000),(20000,20000),(30000,30000)])):
    n=Puntos
    print("n=",n)
    P = [[random(),random()] for i in range(n)]
    cc = [0.5+.001*random(),0.5+.001*random()]
    r = random()/2.
    a,b,c = float(2*pi)*random() , float(2*pi)*random() ,float(2*pi)*random()
    c = [[cc[0]+r*cos(a),cc[1]+r*sin(a)],[cc[0]+r*cos(b),cc[1]+r*sin(b)],[cc[0]+r*cos(c),cc[1]+r*sin(c)]]
    npuntos = puntosEnCirculo(c,P)       
    print("puntos en el circulo: " ,npuntos )
    print("Proporcion: {:.15f} ".format(npuntos/float(n)))
    print("Proporcion: %.15f " % (npuntos/float(n)))
    print("Area circulo: " , float(pi)*(dist(cc,c[0])**2))
    show(point(P,size=1)+circle(cc,dist(cc,c[0]),alpha=0.3,fill=2,facecolor="green",edgecolor="blue"))
    


# # Notas sobre generación aleatoria de datos
# 
# * Ejecutando la instrucción
# 
#     **random()**
# 
#     se obtiene un valor real aleatorio (con distribución uniforme) entre cero y uno.
#     
# 
# * Para que la distribución sea normal se emplea
# 
#     **gauss(0,1)**
# 
#     donde los valores 0 y 1 indican la media y la desviación típica y pueden elegirse otros valores.
#     
# 
# * Una lista de 100 puntos aleatorios con distribución uniforme en el cuadrado unidad se puede obtener así:
# 
#     **P = [[random(),random()] for i in range(100)]**
#     
# 
# * Si el rango es [0,2]x[0,3] , de esta forma:
# 
#     **P = [[2*random(),3*random()] for i in range(100)]**
#     
# 
# * Análogamente, para generar puntos con distribución gausiana (normal), empleamos:
# 
#     **P = [[gauss(2,3),gauss(-1,2)] for i in range(100)]**
# 
# ## Notas sobre representación gráfica
# 
# * Una lista de puntos P se representa mediante
# 
#     **point(P)**
#     
# 
# * Si queremos que los ejes tengan la misma escala, añadimos 'aspect_ratio=1', con la opción color="red" los puntos serán rojos, y con size=10 modificamos su tamaño
# 
#     **point(P,aspect_ratio=1, color="red", size=10)**
# 

# In[43]:


# P = [[gauss(2,3),gauss(-1,2)] for i in range(100)]
# point(P,aspect_ratio=1, color="red", size=10)


# In[44]:


# def quicksort(v, iz = 0, de = None):
#     if de == None:
#         de = len(v) - 1
    
#     if iz >= de:
#         return v

#     pivot = choose_pivot(v, iz, de)

#     mayor_izda = iz
#     menor_de = de
#     intercambiar = mayor_izda <= menor_de
#     while intercambiar:
#         while v[mayor_izda].travel_time < pivot:
#             mayor_izda += 1
#         while v[menor_de].travel_time > pivot:
#             menor_de -= 1
#         if mayor_izda > menor_de:
#             intercambiar = False
#         else:
#             swap(v, mayor_izda, menor_de)
#             mayor_izda += 1
#             menor_de -= 1

#     # print(mayor_izda - menor_de)
#     quicksort(v, iz, menor_de)
#     quicksort(v, mayor_izda, de)

#     return v


# # In[45]:


# def quicksort(a):
#     running = False
#     pivote = len(a)//2
#     num_pivote = a[floor(len(a)/2)]
#     l1 = a[0:pivote]
#     l2 = a[pivote+1:]

#     print(l1, l2)
#     for i in l1:
#         if i > num_pivote:
#             l1.remove(i)
#             l2.append(i)
#             running = True

            
#     for i in l2:
#         if i < num_pivote:
#             l2.remove(i)
#             l1.append(i)
#             running = True
#     print(l1, l2)
#     if running == True:
#         l1.append(num_pivote)
#         l1,l2 = quicksort(l1)
#         l1,l2 = quicksort(l2)
#     else:
#         return (l1,l2)
            


# # In[46]:


# # n = 10
# # array = [floor(100 * random()) for i in range(n)]
# # print(array)
# # l1, l2 = quicksort(array)
# # print(l1,l2)


# # # DIAGONALES INTERNAS

# # In[125]:


# def DiagonalesInternas(P):
#     diagonales = []
#     for i in range(len(P)):
#         # Esta línea fija el valor de `i` en 5 en cada iteración, probablemente deberías eliminarla o colocarla antes del bucle
#         # i = 5
        
#         if areaSignada(P[i-1], P[i], P[(i+1) % len(P)]) >= 0:
#             # print(i, 'CONVEXO')

#             for j in range(len(P)):
#                 if (areaSignada(P[i], P[j], P[i-1]) > 0) and (areaSignada(P[i], P[j], P[(i+1) % len(P)]) < 0):
#                     diagonales.append([P[i], P[j]])

#         elif areaSignada(P[i-1], P[i], P[(i+1) % len(P)]) < 0:
#             for j in range(len(P)):
#                 if not (areaSignada(P[i], P[j], P[j-1]) < 0 and areaSignada(P[i], P[j], P[(j+1) % len(P)]) > 0):
#                     diagonales.append([P[i], P[j]])
    
                
#     return diagonales

# P = [[0,0], [1,1], [2,0], [1.5,1.5], [3,1], [2,2], [1,2]]
# aristas = [[P[i], P[(i+1) % len(P)]] for i in range(len(P))]

# d = DiagonalesInternas(P)
# diagonales_def = []
# for dia in d:
#     running = True
#     for i in aristas:
#         if testInterseccionSegmentos(dia, i):

#             running = False
            
#     if running == True:
#         diagonales_def.append(dia)
    
# # Dibuja el polígono y las diagonales

# diagonales = []
# for d_point in diagonales_def:
#     line_plot = line([d_point[0], d_point[1]], color='blue', linestyle='--')
#     diagonales.append(line_plot)
    
# aristas2 = []
# for a_point in aristas:
#     line_plot = line([a_point[0], a_point[1]], color='red')
#     aristas2.append(line_plot)


# polygon(P, color="green", alpha=0.20) + sum(diagonales) + sum(aristas2)



# # In[ ]:


# #     # Elimina las diagonales que intersectan con los lados del polígono
# #     for d in diagonales[:]:  # Usa una copia de la lista para poder modificar la original
# #         running = True 
# #         for i in range(len(P)):
# #             if testInterseccionSegmentos(d, [P[i], P[(i+1) % len(P)]]):
# #                 running = False
            
# #         if not running:
# #             diagonales.remove(d)


# # In[ ]:


# def tangentes(poligono, p):
#     vertices = []
#     for i in range(len(poligono)):
# #         print(poligono[i-1], poligono[i])
#         a1 = areaSignada(poligono[i-1],poligono[i], p )
#         a2 = areaSignada(poligono[i],poligono[(i+1)%len(poligono)], p )
# #         print(poligono[i], a1,a2)
        
#         if a1*a2 < 0:
#             vertices.append(poligono[i])
        
#     return vertices


# # In[ ]:




