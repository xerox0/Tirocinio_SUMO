import matplotlib.pyplot as plt

# Definiamo i dati per l'istogramma
settimana = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
quantita_prodotto = [10, 8, 5, 2, 1, 0, 0]

# Creiamo l'istogramma
plt.bar(settimana, quantita_prodotto)

# Aggiungiamo i titoli al grafico
plt.title('Discesa del Propano nella Settimana')
plt.xlabel('Giorni della Settimana')
plt.ylabel('Quantità del Prodotto')

# Visualizziamo il grafico
plt.show()
