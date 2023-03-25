import xml.etree.ElementTree as ET
import math
import statistics
import pandas as pd
import argparse




GRID_SIZE = 10
MIN_X, MAX_X = -850, 850
MIN_Y, MAX_Y = -850, 850


grid = {}
for i in range(MIN_X, MAX_X, GRID_SIZE):
    for j in range(MIN_Y, MAX_Y, GRID_SIZE):
        cell_x1 = i
        cell_x2 = i + GRID_SIZE
        cell_y1 = j
        cell_y2 = j + GRID_SIZE
        grid[(cell_x1, cell_y1, cell_x2, cell_y2)] = []


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='nome del file XML contenente le coordinate')
args = parser.parse_args()
tree = ET.parse(args.file)
root = tree.getroot()

#FUNZIONE CHE INDIVIDUA LA CELLA CORRISPONDENTE ALLE COORDINATE DI UNA PERSONA
#
for person in root.findall('.//person'):
    person_id = person.get('id')
    x, y = float(person.get('x')), float(person.get('y'))
    cell_x1 = GRID_SIZE * (math.floor(x/GRID_SIZE))
    cell_y1 = GRID_SIZE * (math.floor(y/GRID_SIZE))
    cell_x2 = cell_x1 + GRID_SIZE
    cell_y2 = cell_y1 + GRID_SIZE
    cell = (cell_x1, cell_y1, cell_x2, cell_y2)

   #Può capitare che le coordinate di una persona cadano su due celle quindi non potendo perdere il dato
   # E non potendo allargare ogni volta la dimensione delle celle bisogna arrotondare alcune posizioni
   # In questo caso si aggiunge il dato alla cella più vicina


    if cell not in grid:
        cella_vicina = None
        #float('inf') serve a inizializzare la variabile nearest_dist al valore infinito
        # In questo modo  confrontiamo la distanza della cella più vicina successivamente
        nearest_dist = float('inf')
        for c in grid.keys():
            dist = math.sqrt((cell_x1 - c[0]) ** 2 + (cell_y2 - c[1]) ** 2)
            if dist < nearest_dist:
                cella_vicina = c
                nearest_dist = dist
        cell = cella_vicina
    if person_id not in [p[0] for p in grid[cell]]:
        grid[cell].append((person_id, x, y))

#CALCOLO DELLE STATISTICHE DI OGNI CELLA
def get_cell_stats(grid):
    cell_stats = {}
    for cell, people in grid.items():
        x_coords = [p[1] for p in people]
        y_coords = [p[2] for p in people]
        cell_stats[cell] = {
            'num_people': len(people),
            'std_dev_x': statistics.stdev(x_coords) if len(x_coords) > 1 else 0,
            'std_dev_y': statistics.stdev(y_coords) if len(y_coords) > 1 else 0
        }
    return cell_stats



#GESTIONE DELL'OUTPUT ATTRAVERSO PANDANS
cell_stats = get_cell_stats(grid)

results = pd.DataFrame(cell_stats.items(), columns=['cell', 'stats'])
results = pd.concat([results.drop(['stats'], axis=1), results['stats'].apply(pd.Series)], axis=1)
results.to_csv('cell_stats.csv', index=False)
