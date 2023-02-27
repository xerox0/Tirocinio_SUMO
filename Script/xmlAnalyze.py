import xml.etree.ElementTree as ET
from collections import Counter

# Parse the XML file
tree = ET.parse('dati.xml')
root = tree.getroot()

# Create a dictionary to count the number of occurrences of each position
counter = Counter((int(child.attrib['x']), int(child.attrib['y'])) for child in root)

# Determine the maximum x and y coordinates
max_x = max(int(child.attrib['x']) for child in root)
max_y = max(int(child.attrib['y']) for child in root)

# Create a two-dimensional list to represent the grid
grid = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]

# Populate the grid with the counts from the dictionary
for position, count in counter.items():
    x, y = position
    grid[x][y] = count

# Determine the most frequently visited zones
most_frequent = []
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if grid[x][y] == max(grid[x]):
            most_frequent.append((x, y))

# Print the most frequent zones
print('Most frequent zones:')
for zone in most_frequent:
    print(zone)