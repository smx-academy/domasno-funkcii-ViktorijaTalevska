#Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar,
#da go njade najdolgoto ime od lista, 
#da go ispecati i da kaze od kolku parametri e sostaveno.
# Korisnikot da gi vnesuva iminjata

def najdolgo(lista):
 lista1=[]
 for i in lista:
  dolzhina=len(i)
  lista1.append(dolzhina)
 najgolemo=max(lista1)
 index=lista1.index(najgolemo) 
 print("Najdolgo ime e imeto:{}".format(lista[index])) 



iminja=[]
while True:
 ime=(input("Vnesete ime (napishete stop dokolu sakate da prestanite)\n"))
 if ime=="stop":
    break
 iminja.append(ime)
print(iminja)
najdolgo(iminja)
