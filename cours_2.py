
# laliste = ["fraise","orange","mangue","banane"]
# laliste.sort()
# print(laliste)

# laliste = [45,67,69,23]
# laliste.sort()
# print(laliste)

# si je veux reverse mon tri
# laliste =["fraise","orange","mangue","banane"]
# laliste.sort(reverse = True)
# print(laliste)

# def myFunction(x):
#         return abs(x-50)
#
# laliste =[100,56,67,34]
# laliste.sort(key = myFunction)
# print(laliste)

# attention a la casse elle compte  aussi sur sort
# faire une copie d'un liste
# laliste2=[100,78,34,12]
# laliste3 = laliste2.copy()
# print(laliste3)

# jointure deux listes
# liste1 =  [2,67,65,90,32]
# liste2 = [67,98,1,43]
# liste3 = liste1+liste2
# print(liste3)

# for x in liste2:
#     liste1.append(x)
# print(liste1)

#liste1.extend(liste1)

# clear() va vider la liste
# liste1.clear()
# print(liste1)

# les TUPLES
# montuple = ('pomme','babane','kiwi')
# print(len(montuple))
# print(type(montuple))

# creer un tuple avec un objet
# montuple = ('poire',)
# print(type(montuple))
# on peut mélanger les types et avoir des tuples constituer de boolean,chaine,entier, etc
# le tuple est une classe comme les autres types en python
# faire appel au constructeur du tuple

# montuple= tuple(("pomme","poire","kiwi"))
# print(montuple)
# print(montuple[1])
#montuple = ('poire','banane','pomme','kiwi','citron')
# print(montuple[2:5])
# if 'citron' in montuple:
#     print('oui il y a du citron')
# a=list(montuple)
# a[1] = 'fraise'
# montuple = tuple(a)
# print(montuple)

# a=list(montuple)
# a.append("pasteque")
# montuple = tuple(a)
# print(montuple)

# a = ("fraise",) # ne pas oublier la virgule
# montuple += a
# print(montuple)

#supp un element
# a = list(montuple)
# a.remove('pomme')
# montuple = tuple(a)
# print(montuple)

#supprimer un tuple : dell
# recup les element du tuple dans des variables

# montuple = ('poire','banane','pomme',)
# (a,b,c) = montuple
# print(a)

from random import randrange


montuple = ('poire','banane','pomme','citron')
# (a,b,*c) = montuple
# print(c)

# parcourir un tuple avec une boucle
# for x in montuple:
#     print(x)
    
#paprcourir un tuplee en utilisant le numéro d'index et la longueur du tuple 
# for i in range(len(montuple)):
#         print(montuple[i]) 
# i= 0
# while i< len(montuple):
#     print(i)
#     i = i +1
    
#joindre des tuples et le multiplier
# montuple1 = ('pomme','kiwi','poire')
# montuple2 = (1, 12, 6)
# montuple3 = montuple1 + montuple2

#projet date butoire = avant restitution note pour l'epsi
# critere lisibilite du code/ commentaire du code/ présentation projet (10 15 min)

# exo 1 construire un code qui affiche une liste des nombres pairs de 1 à 100

# for x in range(1,100):
#         if(x%2 == 0): print(x)

# exo 2 construire un code qui affiche le lancé de 6 des aléatoire
# import random

# for x in range(1,7):
#     print(random.randrange(1, 7))

# exo 3 compter le nbr d'occurence d'une lettre dans une phrase par exemple 'salut ca av ?' compter le nombre de a soit 3
# def occurence 
# def occurence(text, letter):
#     return text.lower().count(letter)

# text = 'salut ca vA'
# print(occurence(text, 'a'))

# import importlib
# file = importlib.import_module("code")
# obj = file.Codeclass()
# obj.show()