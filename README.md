### Autore
Elena Maria Ciuffreda, matr.119325

### Informazioni sul progetto:

Questo progetto implementa un core RISC-V a 32 bit secondo l’architettura RV32I, realizzato interamente con Logisim.
Il processore è in grado di eseguire istruzioni di base (aritmetiche, logiche, load/store, branch e jump) e può far girare programmi come la serie di Fibonacci caricata in memoria.

### Tech Stack 
- Logisim
- Python
- JAVA / JVM

### Come eseguire il progetto
1. Apri il circuito principal
Apri Main/Final.circ con Logisim.
2. Carica il programma
Click destro su IMem → View IMEM
Click destro sul componente RAM
Carica Fibo.txt
3. Avvia l’esecuzione
Attiva il pin di Load (in alto a sinistra )
Premi Ctrl + T per avviare il clock
Osserva i valori della serie di Fibonacci cambiare sul display
4. Reset
Premere il tasto Reset
Il processore è pronto per un nuovo programma.