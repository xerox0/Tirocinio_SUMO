
import csv
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.xlabel('Numero di attraversamenti')
plt.ylabel('Celle attraversate')
plt.title('Distribuzione degli spostamenti')

with open('/home/toore/Tirocinio_SUMO/Scenario/scenario_per_tesi/2023-03-31-10-37-43/cell_stats.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Salta la riga degli header del file
    num_max_cambi = 0  # Numero massimo di cambi di cella effettuati da un pedone
    num_cambi = []  # Lista dei cambi di cella effettuati da ciascun pedone
    for row in reader:
        num = int(float(row[1]))
        num_cambi.append(num)
        if num > num_max_cambi:
            num_max_cambi = num

num_bin = 8  # Numero di bin dell'istogramma
width_bin = num_max_cambi // num_bin  # Divisione intera per ottenere un numero intero
resto = num_max_cambi % num_bin  # Resto della divisione
bins = [i * width_bin for i in range(1,num_bin)]  # Crea i primi num_bin - 1 intervalli
bins.append(bins[-1] + width_bin + resto)  # Aggiunge l'ultimo intervallo allungando l'ultimo
#bins.append(num_max_cambi)  # Aggiunge l'ultimo id all'ultimo intervallo

plt.hist(num_cambi, bins=bins, align='mid', alpha=0.5, label='Numero di attraversamenti', width=width_bin, edgecolor='white',color='red')
plt.xticks(bins, rotation=90)  # Imposta le etichette degli assi x
plt.legend()  # Mostra la legenda

plt.show()