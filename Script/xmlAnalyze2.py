import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

# Leggi il file XML e ottieni le coordinate x e y
tree = ET.parse('mappa.xml')
root = tree.getroot()
x_coords = [float(coord.text) for coord in root.findall('.//x')]
y_coords = [float(coord.text) for coord in root.findall('.//y')]

# Definisci la dimensione della griglia e calcola la larghezza e l'altezza di ogni cella
n = 10 # numero di celle in ogni riga/colonna
width = (max(x_coords) - min(x_coords)) / n
height = (max(y_coords) - min(y_coords)) / n

# Crea una matrice vuota per rappresentare la griglia
grid = np.zeros((n, n))

# Aggiungi ogni punto alle celle corrispondenti nella griglia
for i, j in zip(x_coords, y_coords):
    row = int((j - min(y_coords)) // height)
    col = int((i - min(x_coords)) // width)
    grid[row][col] += 1

# Visualizza la griglia sulla mappa
plt.imshow(grid, cmap='binary', interpolation='nearest', origin='lower')
plt.show()