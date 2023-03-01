import xml.etree.ElementTree as ET

# Leggi il file XML
tree = ET.parse('/home/toore/Tirocinio_SUMO/Scenario/Modena/fcd_dump.xml')
root = tree.getroot()

# Crea un dizionario per le informazioni sui veicoli/persone
veicoli = {}

# Definisci la griglia quadrata di celle con dimensioni fisse
dim_cella = 10 # dimensione della cella in metri
x_min, y_min, x_max, y_max = (0, 0, 1000, 1000) # coordinate della mappa
celle = []
for x in range(x_min, x_max, dim_cella):
    for y in range(y_min, y_max, dim_cella):
        celle.append(Cell(x, y))

# Analizza i dati per ogni veicolo/persona
for veicolo in root.findall('.//veicolo'):
    id_veicolo = veicolo.get('id')
    celle_visit = [] # lista di celle visitate
    last_cella = None # ultima cella visitata
    num_cambi_cella = 0 # numero di cambi di cella
    for pos in veicolo.findall('./posizione'):
        x = float(pos.get('x'))
        y = float(pos.get('y'))
        cella = get_cella(x, y, celle) # ottieni la cella corrispondente
        if cella is not None:
            if cella != last_cella:
                num_cambi_cella += 1
                last_cella = cella
            if cella not in celle_visit:
                celle_visit.append(cella)
    veicoli[id_veicolo] = [celle_visit, num_cambi_cella]

# Funzione per ottenere la cella corrispondente alle coordinate (x, y)
def get_cella(x, y, celle):
    for cella in celle:
        if cella.x <= x < cella.x + dim_cella and cella.y <= y < cella.y + dim_cella:
            return cella
    return None
