import xml.etree.ElementTree as ET
import math
import statistics
import argparse


GRID_SIZE = 10
MIN_X, MAX_X = -850, 850
MIN_Y, MAX_Y = -850, 850


grid = {}
for i in range(MIN_X, MAX_X, GRID_SIZE):
    for j in range(MIN_Y, MAX_Y, GRID_SIZE):
        cell_x = i
        cell_y = j
        grid[(cell_x, cell_y)] = []


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='nome del file XML contenente le coordinate')
args = parser.parse_args()
tree = ET.parse(args.file)
root = tree.getroot()

for person in root.findall('.//person'):
    x, y = float(person.get('x')), float(person.get('y'))
    cell_x = GRID_SIZE * (math.floor(x/GRID_SIZE))
    cell_y = GRID_SIZE * (math.floor(y/GRID_SIZE))
    cell = (cell_x, cell_y)
    grid[cell].append((x, y))

# Funzione per calcolare le statistiche di ogni cella
def get_cell_stats(grid):
    cell_stats = {}
    for cell, people in grid.items():
        x_coords = [p[0] for p in people]
        y_coords = [p[1] for p in people]
        cell_stats[cell] = {
            'num_people': len(people),
            'std_dev_x': statistics.stdev(x_coords) if len(x_coords) > 1 else 0,
            'std_dev_y': statistics.stdev(y_coords) if len(y_coords) > 1 else 0
        }
    return cell_stats

# Esempio di utilizzo
cell_stats = get_cell_stats(grid)
fx=open("Variazioni_celle.txt","w")
for cell, stats in cell_stats.items():
    print(f'Cella {cell}:',file=fx)
    print(f'Numero di persone: {stats["num_people"]}',file=fx)
    print(f'Deviazione standard x: {stats["std_dev_x"]}',file=fx)
    print(f'Deviazione standard y: {stats["std_dev_y"]}',file=fx)
    print(file=fx)

fx.close()
