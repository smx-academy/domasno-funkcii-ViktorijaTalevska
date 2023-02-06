#Da se kreira funkcija so ime pecati_zdravo koja ke prima parametar ime
#  i da se pecati poraka so pozdrav zaedno so imeto koe e
#  isprateno kako parametar. Imeto da go vnese korisnikot.

def pecati_ime(ime):
    print("Zdravo,{}".format(ime))


name=str(input("Vnesete go vasheto ime\n"))
pecati_ime(name)