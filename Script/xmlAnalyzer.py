import xml.etree.ElementTree as ET
import argparse
# Funzione per leggere il file XML e creare la lista di persone/veicoli
import xml.etree.ElementTree as ET


def leggi_dati_xml(file_xml,dimensione_cella):
    tree = ET.parse(file_xml)
    root = tree.getroot()

    # dizionario per tenere traccia delle celle visitate per ogni persona/veicolo
    celle_visit_person = {}

    for person in root.findall('.//person'):
        id_person = str(person.attrib['id'])
        x = float(person.attrib['x'])
        y = float(person.attrib['y'])

        # determina la cella corrente in base alle coordinate x e y
        cella_x = int(x / dimensione_cella)
        cella_y = int(y / dimensione_cella)
        cella_corrente = (cella_x, cella_y)

        if id_person not in celle_visit_person:
            celle_visit_person[id_person] = {
                'celle_visit': {cella_corrente},
                'num_cambi_cella': 0
            }
        else:
            celle_visit_person[id_person]['celle_visit'].add(cella_corrente)
            # verifica se la cella corrente è diversa dall'ultima visitata
            celle_visit = celle_visit_person[id_person]['celle_visit']
            if len(celle_visit) > 1:
                ultima_cella = list(celle_visit)[-2]
                num_cambi_cella = celle_visit_person[id_person]['num_cambi_cella']
                if ultima_cella != cella_corrente:
                    celle_visit_person[id_person]['num_cambi_cella'] = num_cambi_cella + 1

    return celle_visit_person

# Dimensione di ciascuna cella in metri
dimensione_cella = 5.0

# Leggi le informazioni delle persone/veicoli dal file XML
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='nome del file XML contenente le coordinate')
args = parser.parse_args()
dati = leggi_dati_xml(args.file,dimensione_cella)

# Calcola le statistiche persona/veicolo
fx = open("Dati.txt", "w")
for id, info in dati.items():
    celle_visit = info['celle_visit']
    cambi_cella = info['num_cambi_cella']

    # Stampa le informazioni sulla persona/veicolo corrente

    print(f"ID: {id}",file=fx)
    print(f"Numero di celle visitate: {len(celle_visit)}",file=fx)
    print(f"Numero di cambi di cella: {cambi_cella}",file=fx)

    print(file=fx)
fx.close()