import xml.etree.ElementTree as ET
import argparse
# Funzione per leggere il file XML e creare la lista di persone/veicoli
def leggi_persone_da_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    persone = {}

    for person in root.findall('.//person'):
        id = str(person.get('id'))
        x = float(person.get('x'))
        y = float(person.get('y'))
        timestamp = root.get('timestamp')
        pos = (x, y)

        # Aggiorna le informazioni sulla persona/veicolo corrente
        if id not in persone:
            persone[id] = {'celle_visit': set(), 'cambi_cella': 0}
        celle_visit = persone[id]['celle_visit']
        cambi_cella = persone[id]['cambi_cella']


        # cella_x = int(x / dimensione_cella)
        # cella_y = int(y / dimensione_cella)


        if pos not in celle_visit:
            celle_visit.add(pos)
            if len(celle_visit) > 1:
                cambi_cella += 1
        persone[id]['cambi_cella'] = cambi_cella
        persone[id]['celle_visit'] = celle_visit

    return persone

# Dimensione di ciascuna cella in metri
dimensione_cella = 5.0

# Leggi le informazioni delle persone/veicoli dal file XML
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='nome del file XML contenente le coordinate')
args = parser.parse_args()
persone = leggi_persone_da_xml(args.file)

# Calcola le statistiche persona/veicolo
fx = open("Dati.txt", "w")
for id, info in persone.items():
    celle_visit = info['celle_visit']
    cambi_cella = info['cambi_cella']

    # Stampa le informazioni sulla persona/veicolo corrente

    print(f"ID: {id}",file=fx)
    print(f"Numero di celle visitate: {len(celle_visit)}",file=fx)
    print(f"Numero di cambi di cella: {cambi_cella}",file=fx)
    print(file=fx)
fx.close()