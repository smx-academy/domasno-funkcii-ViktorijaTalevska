#Da se kreira funkcija so ime najgolem_broj koja ke prima 3 parametri,
#  da se najde najgolemiot broj i da se ispecati. 
# Broevite da gi vnese korisnikot


def najgolem(list):
    najgolem=max(list)
    print("Od vnesenite tri broevi najgolem e:{}".format(najgolem))
    


lista=[]
for i in range(3):
    broj=int(input("Vnesi broj:\n"))
    lista.append(broj)

najgolem(lista)
