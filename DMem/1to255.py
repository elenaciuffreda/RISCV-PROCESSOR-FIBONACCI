# Apriamo (o creiamo) un file chiamato "1to255.txt" in modalità scrittura ("w")
file = open('1to255.txt', 'w')

# Scriviamo l'intestazione richiesta da Logisim per i file di memoria
# "v2.0 raw" indica il formato della memory image
file.write("v2.0 raw\n")

# Variabile di input inizializzata a 0
din = 0

# Ciclo che gira finché din non arriva a 255 (255 escluso)
while int(din) != 255:
    # Convertiamo din in una stringa esadecimale (es. "0x1a")
    dout = hex(din)
    # dout[2:] serve per togliere "0x" e lasciare solo il valore esadecimale
    # Poi scriviamo il valore nel file seguito da una nuova riga
    file.write(str(dout[2:]) + '\n')
    # Incrementiamo din di 1
    din = 1 + din
# Chiudiamo il file dopo aver finito di scrivere
file.close()
