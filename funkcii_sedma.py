#Da se napravi funkcija koja ke presmetuva prosek na ucenik, 
# otcenite da gi prima kako parametar vo lista. 
# Da ima druga funkcija koja kako parametri ke gi prima prosekot i imeto na ucenikot, 
# ke presmetuva uspeh na ucenik spored prosekot i da ispecati so kakov uspeh e toj ucenik

def prosek(ocenki):
 vkupno=sum(ocenki)
 return vkupno/len(ocenki)
 

def uspeh(ime,lista):
 pro=prosek(lista)
 if pro==5:
    print("Uchenikot {} e odlichen".format(ime))  
 elif pro==4:
    print("Uchenikot {} e mnogu dobar".format(ime))  
 elif pro==3:
    print("Uchenikot {} e dobar".format(ime))
 elif pro==2:
    print("Uchenikot {} ima dovolen prosek".format(ime))
 elif pro==1:
    print("Ucenikot {} ima nedevolen prosek".format(ime))
 else:
    print("Imate greshka")

name=input("Vnesete go imeto na uchenikot:\n")
list=[]
while True:
 ocenka=input("Vnesete gi negovite oceni:\n izberete stop da prestanite\n")
 if ocenka=="stop":
    break
 list.append(ocenka)

print(list)
uspeh(name,list)
 





