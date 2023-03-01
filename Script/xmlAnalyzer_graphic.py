import xml.etree.ElementTree as ET
import argparse
import matplotlib.pyplot as plt
import numpy as np

# Definisci gli argomenti da linea di comando
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='nome del file XML contenente le coordinate')
parser.add_argument('--n', type=int, default=10, help='dimensione della griglia (default: 10,max:100)')
args = parser.parse_args()

# Leggi il file XML e ottieni le coordinate x e y
tree = ET.parse(args.file)
root = tree.getroot()
x_coords = [float(coord.get('x')) for coord in root.findall('.//person')]
y_coords = [float(coord.get('y')) for coord in root.findall('.//person')]

# Calcola la larghezza e l'altezza di ogni cella
width = (max(x_coords) - min(x_coords)) / args.n
height = (max(y_coords) - min(y_coords)) / args.n

# Crea una matrice vuota per rappresentare la griglia
grid = [[0 for _ in range(args.n)] for _ in range(args.n)]

# Aggiungi ogni punto alle celle corrispondenti nella griglia
for i, j in zip(x_coords, y_coords):
    row = int((j - min(y_coords)) // height)
    col = int((i - min(x_coords)) // width)
    if row >= args.n or col >= args.n:
        continue
    grid[row][col] += 1

# Stampa la griglia
# for row in grid:
#     for cell in row:
#         print(cell, end=' ')
#     print()

# Crea una visualizzazione grafica della griglia
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='inferno')

# Aggiungi i numeri di conteggio come testo nelle celle della griglia
for i in range(args.n):
    for j in range(args.n):
        text = ax.text(j, i, grid[i][j], ha='center', va='center', color='white')

# Aggiungi una barra di colori per la visualizzazione
cbar = ax.figure.colorbar(im, ax=ax)

# Mostra la visualizzazione grafica
plt.show()
