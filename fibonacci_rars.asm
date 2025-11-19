############################################################
# Fibonacci in RARS – versione corretta (no .org)
# Calcola i primi N numeri e li salva in memoria
############################################################

.data
N:      .word 10                # Numero di valori da calcolare
array:  .space 40               # 10 valori × 4 byte = 40 byte

.text
.globl main
main:

    # Carica N
    la t0, N
    lw t1, 0(t0)                # t1 = N

    # Puntatore all'array
    la t2, array

    # Inizializza F0 e F1
    li t3, 0                    # F0
    li t4, 1                    # F1

    # Salva F0 in memoria
    sw t3, 0(t2)

    # Se N == 1 finiamo qui
    addi t1, t1, -1
    beqz t1, end

    # Salva F1 in memoria
    sw t4, 4(t2)

    addi t2, t2, 8              # t2 ora punta alla terza cella

loop:
    add t5, t3, t4              # t5 = F(n) = F(n-1) + F(n-2)
    sw t5, 0(t2)                # salva in array

    # Shift valori
    mv t3, t4                   # F(n-2) = F(n-1)
    mv t4, t5                   # F(n-1) = F(n)

    # Avanza puntatore array
    addi t2, t2, 4

    # Decrementa contatore
    addi t1, t1, -1
    bnez t1, loop

end:
    # ----- STAMPO RISULATI FOR TESTING -----
    la t2, array
    la t0, N
    lw t1, 0(t0)

print_loop:
    lw a0, 0(t2)
    li a7, 1         # STAMPO integer
    ecall

    # stampa spazio
    li a0, 32
    li a7, 11        # STAMPO char
    ecall

    addi t2, t2, 4
    addi t1, t1, -1
    bnez t1, print_loop

    # Exit
    li a7, 10
    ecall
