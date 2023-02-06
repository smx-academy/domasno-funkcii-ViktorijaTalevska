#Da se napravi funkcija koja kako parametar ke prima nekoj string i da proveri 
# dali toj string e palindrom t.e. dali toj string se cita od dvete strani
#Primer: ana, kalabalak


def proveri_palindrom(zbor):
 prevrten=zbor[::-1]
 if zbor==prevrten:
    print("Zborot e palindrom")
 else:
    print("Ne e palindrom")




list=[]
word=input("Vnesi go zborot koj sho sakash da go proverish:\n")
list.append(word)
proveri_palindrom(word)