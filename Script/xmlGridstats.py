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

for person in root.findall('.//person'):
    person_id = person.get('id')
    x, y = float(person.get('x')), float(person.get('y'))
    cell_x1 = GRID_SIZE * (math.floor(x/GRID_SIZE))
    cell_y1 = GRID_SIZE * (math.floor(y/GRID_SIZE))
    cell_x2 = cell_x1 + GRID_SIZE
    cell_y2 = cell_y1 + GRID_SIZE
    cell = (cell_x1, cell_y1, cell_x2, cell_y2)
    if person_id not in [p[0] for p in grid[cell]]:
        grid[cell].append((person_id, x, y))


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

cell_stats = get_cell_stats(grid)

results = pd.DataFrame(cell_stats.items(), columns=['cell', 'stats'])
results = pd.concat([results.drop(['stats'], axis=1), results['stats'].apply(pd.Series)], axis=1)
results.to_csv('cell_stats.csv', index=False)
