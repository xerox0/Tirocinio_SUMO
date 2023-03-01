import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# Lettura del file XML
tree = ET.parse('/home/toore/Tirocinio_SUMO/Scenario/Modena/fcd_dump.xml')
root = tree.getroot()

# Estrazione delle coordinate
coords = []
for point in root.findall('.//person'):
    x = float(point.get('x'))
    y = float(point.get('y'))
    coords.append((x, y))

# Dimensione della griglia da linea di comando
grid_size = int(input("Inserisci la dimensione della griglia: "))

# Calcolo dei valori massimi e minimi di x e y
min_x = min(coords, key=lambda x: x[0])[0]
max_x = max(coords, key=lambda x: x[0])[0]
min_y = min(coords, key=lambda x: x[1])[1]
max_y = max(coords, key=lambda x: x[1])[1]

# Creazione della griglia
x_step = (max_x - min_x) / grid_size
y_step = (max_y - min_y) / grid_size
grid = np.zeros((grid_size, grid_size))
for coord in coords:
    x_idx = int((coord[0] - min_x) // x_step)
    y_idx = int((coord[1] - min_y) // y_step)
    if x_idx >= grid_size or y_idx >= grid_size:
        continue
    grid[x_idx, y_idx] += 1

# Disegno del grafico
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='YlOrRd')

# Annotazione delle coordinate sulla griglia
for i in range(grid_size):
    for j in range(grid_size):
        text = ax.text(j, i, f"{grid[i, j]}\n({min_x+j*x_step:.2f}, {min_y+i*y_step:.2f})",
                       ha="center", va="center", color="white")

# Aggiunta della legenda
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Frequenza", rotation=-90, va="bottom")

# Visualizzazione del grafico
plt.show()
