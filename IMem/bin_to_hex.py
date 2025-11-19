# Apriamo (o creiamo) un file chiamato "cont.txt" in modalità scrittura
file = open('cont.txt', 'w')

# Scriviamo l'intestazione richiesta da Logisim per file di memoria (.txt)
# "v2.0 raw" indica che i dati successivi sono valori grezzi (raw) in esadecimale
file.write("v2.0 raw\n")

# Leggiamo il primo valore di ingresso da tastiera
# L'utente deve inserire una stringa contenente un numero binario (es. "1010")
din = input()

# Continuare a leggere valori finché l’utente non inserisce "-1"
while int(din) != -1:
    # Convertiamo il valore binario inserito (din) in intero: int(din, 2)
    # Poi convertiamo l'intero in esadecimale tramite hex()
    dout = hex(int(din, 2))

    # dout è una stringa del tipo "0x1a"
    # dout[2:] serve a rimuovere il prefisso "0x" e lasciare solo "1a"
    file.write(str(dout[2:]) + '\n')

    # Chiediamo un nuovo input all'utente
    din = input()

# Chiudiamo il file dopo aver terminato la scrittura
file.close()
