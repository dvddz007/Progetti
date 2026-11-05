# CICLO INFINITO SENZA WHILE TRUE

def infinito():
    try:
        print("infinito")
        infinito()
    except RecursionError:
        print("infinito")
        infinito()


infinito()
