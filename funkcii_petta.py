#Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata


def prosek(lista):
    suma=sum(lista)
    dolzhina=len(lista)
    pro=suma/dolzhina
    print("Prosekot na listata iznesuva:{}".format(pro))

list=[]
while True:
 broj=input("Vnesi broj:\n napishi stop za da prestanish\n")
 if broj=="stop":
    break
 list.append(int(broj))

print(list)
prosek(list)
