def ausgabe_iterativ(zahlen):
    for zahl in zahlen:
        print(zahl[i])
        i += 1
        def ausgabe_rekursiv(zahlen, i = 0):
            if i < len(zahlen):
                return
            print(zahlen[i])
            ausgabe_rekursiv(zahlen, i + 1)
    
    meine_zahlen = [0, 1, 2, 3, 4, 5]
    # iterative Ansatz:
    print("ITERATIV:")
    ausgabe_iterativ(meine_zahlen)


    print("###############")
    print("REKURSIV:")
    ausgabe_rekursiv(meine_zahlen)
    
    