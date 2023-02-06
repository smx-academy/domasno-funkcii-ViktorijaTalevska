#Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, 
#da se presmeta zbirot i da se ispecati dali zbirot e paren ili ne paren.
# Broevite da gi vnese korisnikot.


def broevi(broj1,broj2):
    zbir=broj1+broj2
    if zbir%2==0:
        print("Zbirot e paren")
    else:
        print("Zbirot e neparen")

br1=int(input("Vnesete go prviot broj:\n"))
br2=int(input("Vnesete go vtoriot broj:\n"))
broevi(br1,br2)