""" prenom = "Pierre"
age = 19 
isMajeur = False 
compte_en_banque = 20135.384 
amis = ['Marie', 'Julien','Adrien'] 
parents = ["Marc","Caroline"] 
mere = parents[1] 
pere = parents[0] 
""" """ 
presentation = str('Salut, moi c est {} agé de {} ans') presentation.format(prenom, age) 
""" """ 
def replaceWord(text, word): 
    return(text.replace(word,"Bonsoir")) 
text = "bonjour tout le monde" 
print(replaceWord(text, "bonjour")) 
""" """ 
listOfName = "Pierre, Julien, Anne, Marie, Julien"
namesArray = listOfName.split(', ')
namesArray.sort()
print(*namesArray, sep=', ')
""" """ 
listName = ['Marie', 'Julien','Adrien', 'Anne] 
listName.remove(listName[1]) print(ListNAme) 
""" """ 
from math import pi 
def sphereVolume(rayon): 
    return (4 * pi / 3) * (rayon ** 3) 
    print (sphereVolume(10))

""" """ 
def compareNumber(number): 
if (isinstance(number, int)): 
    if (number >= 10): return(str(number) + " est supérieur à 10.")
    else: return(str(number) + " est inférieur à 10.")
    else: return(str(number) + " n'est pas un nombre."); 
    number = 9 print(compareNumber(number)) 
""" """ 
def createList(number1, number2): 
    numberlist = [] while (number1 <= number2): 
    numlist.append(number1) 
    number1 += 1 
    return numberlist 
    
number1 = 10 
number2 = 20 
print(createList(number1, number2)) 
""" 
def maFonction(n): 
        return abs(n-50) 
fruits = [100,52,87,96,56,23] 
fruits.sort(key = maFonction) print(fruits)