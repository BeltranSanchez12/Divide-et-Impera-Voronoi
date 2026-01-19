# 📐 Geometría Computacional: Diagramas de Voronoi

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/SageMath-9.0+-purple.svg" alt="SageMath">
  <img src="https://img.shields.io/badge/License-Academic-green.svg" alt="License">
</p>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Euclidean_Voronoi_diagram.svg/400px-Euclidean_Voronoi_diagram.svg.png" alt="Voronoi Diagram" width="300">
</p>

Implementación de algoritmos fundamentales de **Geometría Computacional** con énfasis en la construcción de **Diagramas de Voronoi** mediante el método **Divide y Vencerás**.

---

<br>

<p align="center">
  <a href="https://github.com/BeltranSanchez12/Divide-et-Impera-Voronoi/InteractivoVoronoi.html">
    <img src="https://img.shields.io/badge/🚀_DEMO_INTERACTIVA-Diagrama_de_Voronoi-blue?style=for-the-badge&logoColor=white" alt="Demo Interactiva" height="60">
  </a>
</p>

<p align="center">
  <b>👆 Haz clic para visualizar el algoritmo en tiempo real 👆</b>
</p>

<br>

---

## 📋 Descripción

Este proyecto implementa desde cero los principales algoritmos de geometría computacional, incluyendo:

- **Diagramas de Voronoi** - Partición del plano en regiones según proximidad a puntos semilla
- **Ordenación geométrica** - Ordenación de puntos por coordenadas, ángulo y direcciones arbitrarias
- **Poligonización** - Construcción de polígonos simples a partir de nubes de puntos
- **Operaciones fundamentales** - Área signada, intersección de rectas, recorte de polígonos

## 🎯 Algoritmos Implementados

### Diagramas de Voronoi
| Algoritmo | Complejidad | Descripción |
|-----------|-------------|-------------|
| Voronoi incremental | O(n²) | Construcción región por región |
| **Divide y Vencerás** | O(n log n) | Fusión de subproblemas mediante "cicatriz" |

### Ordenación Geométrica
- Ordenación por abscisas (X) y ordenadas (Y)
- Ordenación según dirección de un vector arbitrario
- Ordenación angular respecto a un punto (para poligonización estrellada)
- Cálculo de puntos extremos (Xmax, Xmin, Ymax, Ymin, Vmax, Vmin)

### Poligonización de Nubes de Puntos
- **Monotonía en X** - Polígono monótono respecto al eje horizontal
- **Monotonía en Y** - Polígono monótono respecto al eje vertical
- **Monotonía direccional** - Polígono monótono en dirección arbitraria
- **Poligonización estrellada** - Ordenación angular desde el baricentro

### Operaciones Básicas
- Área signada de triángulos (orientación)
- Intersección de rectas y segmentos
- Recorte de polígonos por semiplanos (Sutherland-Hodgman)
- Cálculo de mediatrices

## 🗂️ Estructura del Proyecto

```
├── InteractivoVoronoi.html      # 🌐 Demo interactiva (SageMath embebido)
├── Proyecto_final.ipynb         # 📓 Notebook principal con desarrollo completo
├── Biblioteca_GC.py             # 📦 Funciones básicas de geometría
├── Biblioteca2_GC.py            # 📦 Ordenación y poligonización
├── Biblioteca3_GC.py            # 📦 Algoritmos avanzados
├── Biblioteca_Voronoi.py        # 📦 Implementación de Voronoi (Divide y Vencerás)
└── README.md
```

## ⚙️ Requisitos

### Opción 1: SageMath (Recomendado)
```bash
# Instalar SageMath
sudo apt install sagemath  # Linux
# o descargar desde https://www.sagemath.org/

# Ejecutar notebook
sage -n jupyter Proyecto_final.ipynb
```

### Opción 2: Python + Dependencias
```bash
pip install numpy matplotlib scipy
```

## 🚀 Uso

### Demo Interactiva (sin instalación)
Simplemente abre [`InteractivoVoronoi.html`](InteractivoVoronoi.html) en tu navegador. Utiliza SageMath Cell para ejecutar el código directamente.

### Notebook Local
```bash
sage -n jupyter Proyecto_final.ipynb
```

### Importar Bibliotecas
```python
from Biblioteca_GC import *
from Biblioteca2_GC import *
from Biblioteca_Voronoi import *

# Generar nube de puntos aleatorios
P = [[random(), random()] for i in range(20)]

# Calcular y dibujar Voronoi
dibujaVoronoi(P)

# Ejecutar Divide y Vencerás con visualización
voronoi_main(P, iteraciones=30)
```

## 📊 Ejemplos Visuales

### Diagrama de Voronoi
```python
P = [[gauss(0,1), gauss(0,1)] for i in range(30)]
dibujaVoronoi(P, color='blue')
```

### Poligonización Estrellada
```python
P = [[random(), random()] for i in range(50)]
polygon(poligonizacionEstrellada(P)[0], alpha=0.3)
```

### Ordenación Angular
```python
P = [[random(), random()] for i in range(20)]
C = [0.5, 0.5]  # Centro
line(ordenAngular(P, C)) + point(C, color='red', size=50)
```

## 🔬 Fundamentos Teóricos

### Diagrama de Voronoi
Dado un conjunto de puntos P = {p₁, p₂, ..., pₙ}, el diagrama de Voronoi particiona el plano en n regiones, donde cada región V(pᵢ) contiene todos los puntos más cercanos a pᵢ que a cualquier otro punto:

$$V(p_i) = \{x \in \mathbb{R}^2 : d(x, p_i) \leq d(x, p_j), \forall j \neq i\}$$

### Algoritmo Divide y Vencerás
1. **Dividir**: Separar P en dos subconjuntos P₁ y P₂ por una línea vertical
2. **Conquistar**: Calcular recursivamente Voronoi(P₁) y Voronoi(P₂)
3. **Combinar**: Fusionar ambos diagramas mediante una "cicatriz" que recorre las mediatrices

### Complejidad
| Operación | Tiempo |
|-----------|--------|
| Voronoi (D&V) | O(n log n) |
| Ordenación angular | O(n log n) |
| Recorte por semiplano | O(n) |
| Poligonización | O(n log n) |

## 📚 Referencias

- de Berg, M., et al. *Computational Geometry: Algorithms and Applications*
- Preparata, F. P., & Shamos, M. I. *Computational Geometry: An Introduction*
- Fortune, S. (1987). *A sweepline algorithm for Voronoi diagrams*

## 👤 Autor

**Beltrán Sánchez Careaga**

Proyecto Personal - Geometría Computacional

## 📄 Licencia

Proyecto académico - (2024)

---

<p align="center">
  <a href="https://tu-usuario.github.io/nombre-repo/InteractivoVoronoi.html">
    <img src="https://img.shields.io/badge/▶️_Probar_Demo_Interactiva-1565C0?style=for-the-badge" alt="Demo" height="50">
  </a>
</p>

