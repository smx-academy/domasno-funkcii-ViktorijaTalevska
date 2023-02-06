#Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri,
#  da presmetuvaat plostinata i perimetarot na pravoagolnik. Korisnikot da gi 
# vnesuva broevite i korisnikot da izbere koja presmetka da se izvrsi.
# DA NE SE IZVRSUVAAT DVETE


def ploshtina(str1,str2):
    plostina=str1*str2
    print("Ploshtinata na pravoagolnikot iznesuva:{}".format(plostina))

def perimetar(str1,str2):
    L=2*str1+2*str2
    print("Perimetarot na pravoagolnikot iznesuva: {}".format(L))


strana1=int(input("Vnesete ja prvata strana na pravoagolnikot:\n"))
strana2=int(input("Vnesete ja drugata strana:\n"))
odgovor=input("Shto sakate da presmetame? ploshtina ili perimetar?\n")
if odgovor=="ploshtina":
    ploshtina(strana1,strana2)
elif odgovor=="perimetar":
    perimetar(strana1,strana2)
else:
    print("Imate greshka.Obidete se povtorno")