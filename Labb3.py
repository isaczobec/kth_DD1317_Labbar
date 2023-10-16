import felhantering

def aritmetrisksumma(a1, # Första talet i talserien
                    d, # Differensen mellan varje tal
                    n): # Antalet tal i talserien

    return(n*(a1+(a1+d*(n-1)))/2) #returnerar aritmetiska summan enligt dess formel


def geometrisksumma(g1, # Första talet i talserien
                   q, # Kvoten mellan varje tal i talserien
                   n): # Antalet tal i talserien

    if q == 1:
        return g1 * n # blir division med noll enligt formeln om man inte gör såhär

    return(g1*((q**n)-1)/(q-1)) # returnerar den geometriska summan enligt dess formel


def main():

    # använder felhanteringsmodulen för att se till att alla inputs är av rätt typ
    a1 = felhantering.felhantering_flyttal("Ange ett startvärde (a1): ")
    d = felhantering.felhantering_flyttal("Ange differensen (d): ")
    g1 = felhantering.felhantering_flyttal("Ange startvärde (g1): ")
    q = felhantering.felhantering_flyttal("Ange kvot (q): ")


    
    n = felhantering.felhantering_heltal("Ange antalet element (n): ")
    while n < 0:
        print("n måte vara 0 eller större!") # en talföljd får inte ha ett negativt antal tal!
        n = felhantering.felhantering_heltal("Ange antalet element (n): ")


    ariSumma = aritmetrisksumma(a1, d, n)
    geoSumma = geometrisksumma(g1, q, n)

    print("aritmetiska summan är:",ariSumma)
    print("geometiska summan är:",geoSumma)


    if geoSumma > ariSumma:
        print("Den geometriskasumman är störst!")
    elif geoSumma == ariSumma:
        print("Summorna är lika stora!")
    else:
        print("Den aritmetriska är större!")


main()


