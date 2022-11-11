# python

ctrl + c = copier
ctrl + v= collé 
pour utiliser " " ou () ou ’ dans une variable il faut entourer la variable 3 apostrophes ex :
 X « aujourd’hui il fait beau » 
 / ’’’aujourd’hui il fait beau ’’’
alors pour ne pas mettre les 3 apostrophes il faut mettre un slash avant la parenthèse, apostrophe, guillemet.  
«aujourd/’hui il fait beau »  
Ou                                                              
«/ aujourd’hui il fait beau / »

## Calcul 
pour la division il faut utiliser  «/»
pour la somme «+»
pour la multiplication  «*»
pour la soustraction «-»
et pour l’égale «=»

## =
avec l’égale ou peux faire devenir des mots en autre mot :   
gâteau = bon  
print ( gâteau)
>>>bon

## .#
Les « # » servent à faire des commentaires qui ne se voient pas et qui ne changent rien 


## %
Le % remplace le « * »  
Ex :  
```python
monscore = 100   
message = « tu as obtenu %s pts »   
print ( message % monscore )  
>> > tu as obtenu 100 pts
```

quand il y a « %s », ça veut dire qu’il y a quelque chose qui va le remplacer, et quand il y a  « % », c’est un texte comme là avec monscore, c’est ce qu’il est égal au monscore qui va elle ici.
Ou sinon autre explication : dans le message, le %s est égal à monscore

## les différentes listes 

Il y a deux sortes de listes :  
la première sorte de liste est comme une sorte de bloc et qui s’écrit qu’avec juste deux guillemets (un au début et un à la fin ) 
la deuxième sorte liste où il y a plusieurs éléments distincts et chaque élément est entouré de crochets, guillemets ou apostrophes pour qu’il soit reconnaissable.

Exemple d’une liste avec plusieurs éléments distincts :
```python
Jour_de_la_semaine = ['demain', "c’est ",'samedi', 'donc',"c est", 'le' ,'week-end']
Print =( Jour_de_la_semaine[2])
```
>>> 'samedi'

Le « c’est » est entourer de guillemets au lieu d’apostrophes, car il y a une apostrophe dans l’élément. Aussi, dans une liste, on commence a compté à partir de 0. 

Pour ne prendre que certain élément, il faut faire :
```python
Jour_de_la_semaine = ['demain', "c’est ",'samedi', 'donc', "c’est", 'le' ,'week-end']
Print =( Jour_de_la_semaine[2:5])
```
>>> 'samedi', 'donc', "c’est", 'le'

ou peut aussi mettre deux chaines ensembles :
```python
liste_1 = ('a', 'b', 'c', 'd')
liste_2 = ('1', '2', '3', '4') 
print  (liste_1+liste_2)
```
>>> ('a', 'b', 'c', 'd', '1', '2', '3', '4')

Dans une liste, on peut aussi ajouter des choses grâce à « append » :
```python
liste_1 =['a', 'b', 'c', 'd']
liste_1.append ('e')
print (liste_1)
```
>>>['a', 'b', 'c', 'd', 'e']

Et c’est la même chose pour « del »
```python
liste_1 =['a', 'b', 'c', 'd']
del liste_1 [3]
print (liste_1)
```
>>>['a', 'b', 'c']

On peut aussi fusionner deux listes :
```python
liste_soleil = ['1','2','3']
liste_soleil2 = ['soleil']
liste_marrelle =liste_soleil+liste_soleil2
print (liste_marrelle)
```
>>>['1', '2', '3', 'soleil']
ou les multiplier 

```python
liste_chiffre= ['1','2','3']
print (liste_chiffre*5)
```
>>>['1', '2', '3', '1', '2', '3', '1', '2', '3', '1', '2', '3', '1', '2', '3']

mais aussi :
grâce «dict» (dictionnaire) on peut retrouver des éléments (valeur)grâce à un autre élément (la clé) :
```python
sport_pref={'joseph':'boxe','francois':'escalade','stephan':'natation','sophie':'basket','elodie':'velo'}
print (sport_pref ['joseph'])
```
>>>boxe

## turtle

Pour faire avancer la tortue il faut marquer « forwad » (la longueur que on veut), puis pour tourner il faut marquer « left » ou « right » :

```python
import turtle
turtle.forward(100)
turtle.right(90)
```
![image](https://user-images.githubusercontent.com/117589126/201330404-ca901707-d181-436c-857a-620b626ec9bd.png)


les difffétents degrés :

![image](https://user-images.githubusercontent.com/117589126/201330245-f3ccbb40-bd2b-494f-aeaf-7f3a82f8415c.png)


donc pourun carré il faut fair ça :

```python
import turtle 
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
```
ou pour que ça soit plus simple fair ça :

```python
from turtle import *
for x in range(4) :
    forward(100)
    right(90)
```

pour que la commande reste afficher il faut mettre 

```python
turtle.exitonclick()
```
a la fin 

pour qu’à la fin du dessin le dessin s’enlève et que la flèche revienne au point de départ il faut mettre ça
```python
«turtle.reset()» 
```

et si on met
```python 
«turtle.clear()» 
```
ça enlève aussi le dessin mais ça laisse la flèche où elle est. 

Avec la commande 
```python
«turtle.backward(...)»
```
on peut faire un trait en arrière. 

Pour lever la flèche (pour mettre un espace) il faut mettre 
```python
« turtle.up() »
```
au début et 
```python
« turtle.down() »
```
a la fin et au milieu 
```python
turtle.forward(100)
``` 

Pour remplir une forme il faut marquer au début 
```python
« turtle.begin_fill() »  
``` 
et à la fin 
```python
« turtle.end_fill() » 
```  
et pour y mettre une couleur il faut mettre   
```python
« turtle.color() » 
```

Pour faire un cercle il faut mettre juste  
```python 
« turtle.circle(50,360) » 
```

## if,else,elif
*chap 5*

- `if` = si
- `else` = sinon/autrement


### `if`

```python
if age > 20:
    print('tu as le bon age')
```  

L’âge de la personne est de 25 ans. 
L’âge maximum avant d’être trop vieux de 20 ans.  
Si la personne a plus de 20 il sera trop vieux donc le message va apparaître, mais s’il a moins de 20 ans il sera plus jeune donc aucun message ne va apparaître.  
Attention : mettre bien autant d’espace si vous voulez mettre plusieurs phrase/ (print) et if est obligatoire
Il y a aussi d’autres symboles pour les conditions :  



| Symbole  |      Définition         |
|----------|:-----------------------:|
| `==` |  Egale à |
| `!=` |  N'es pas égale à |
| `x > y` |  `x` est superieur a `y`|
| `x < y` |  `x` est inferieur a `y`|
| `x >= y` |  `x` est superieur ou égale a `y`|
| `x <= y` |  `x` est inferieur ou egale a `y`|


### `else`

```python
âge = 12 
if âge > 16 :
    print('tu as le bonne âge ')
else :
    print ('tu n as pas le bonne âge')

```
S’il avait 16 ans, ça aurait marqué « tu as le bon âge » mais comme il a 12 ans et comme on a mis else ça va marquer « tu n’as pas le bon l'âge ».

### `elif`

```python
age = 12
if age >= 16 :
    print('tu as le bonne age ')
elif age == 15 :
    print ('tu auras le bon âge dans 1 ans')
elif âge == 14 :
    print ('tu auras le bon âge dans 2 ans')
elif âge == 13 :
    print ('tu auras le bon âge dans 3 ans')
else :
    print ('tu n as pas le bonne âge')
```
elif sert en quelque sorte à mettre plusieurs choix

### `and`
```python
age=3
if age >= 7 and age <= 77 :
    print ('tu peux jouer')
else :
    print ('tu ne peux pas jouer')
```
Dans ce cas-là « « and » veux dire entre : entre 7 et 77 ans, tu peux jouer et avec else si tu as moins de 7 ou plus 77 ans, tu ne peux pas jouer

### `or`
```python
age=18
if age==11 or age==12 or age==13 or age==14 or age==15 :
    print ('tu es au college') 
else :
    print ('tu n es pas au college')
```
dans ce cas-ci or sert à mettre plusieurs choix/âge  

### `none`
None est une valeur qui n’a pas de valeur, une valeur vide, mais ce n’est pas comme la valeur zéro car la valeur zéro a une valeur : « Zéro » alors que None n’est rien, ce n’est aucune valeur.

```python
age= None
if age==None :
    print ('tu es au college') 
else :
    print ('tu n es pas au college')
```
ceci est pratique pour calculer une valeur à partir d’une variable qui n’a pas encore été calculée.

#### bonnus a part
convertir nombre en chaine et vis-versa :
La différence visuelle d’une chaîne a un nombre, ce sont les guillemets. Les nombres en n’ont pas, mais la chaîne si, mais la différence pour l’ordi est beaucoup plus grande, car si on met des guillemets au nombre, pour l’ordinateur, ça voudra dire que le nombre est une variable. Et pour convertir une chaîne et un nombre entier, il faut faire ça.

## les boucles 
Pour ne plus répéter on peut utiliser la boucle for au lieu d’écrire a la main ligne par ligne :
```python
for x in range (0,5) : 
    print ('bonjour')
```
>>>bonjour  
>>>bonjour  
>>>bonjour   
>>>bonjour  
>>>bonjour

on peut aussi mélanger les listes avec les boucles :
```python
print(list(range(10,20)))
```
>>>[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

Attention : la lettre au milieu de « for » et « in » est une lettre qu’on peut choisir on peut même le remplacer par un mot mais pas un nombre ou une phrase.

```python
liste_de_course = ["lait","oeuf","framboise","tomate","poulet","salade"]
for x in liste_de_course :
    print(x)
```
cette commande permet de reproduire une liste 
et celle si de la doubler 
```python
liste_de_course = ["lait","oeuf","framboise","tomate","poulet","salade"]
for x in liste_de_course :
    print(x)
    print(x)
```
>>>lait  
>>>oeuf  
>>>oeuf  
>>>framboise    
>>>framboise  
>>>tomate  
>>>tomate  
>>>poulet  
>>>poulet  
>>>salade  
>>>salade

```python
alphabet = ['a','b','c']
for x in alphabet:
    print(x)
    for y in alphabet:
        print(y)

```
>>>a  
a  
b  
c  
b  
a  
b  
c  
c  
a  
b  
c

Ici ça donne ca car dans le premier bloque de code c’est dit que il faut faire « a » a la ligne « b » a la ligne « c » a la ligne puis dans le deuxième bloque de code il faut faire la même chose sauf que l’ordinateur produit le code de haut en bas c’est à dire que ça va faire « a » (du premier, bloque.) a la ligne « a » (du deuxième, bloque.) a la ligne « b » (du deuxième, bloque.) a la ligne « c » (du deuxième, bloque.) a la ligne ensuite « b » du premier bloque puis « a » (du deuxième, bloque.) a la ligne « b » (du deuxième, bloque. ) a la ligne « c » (du deuxième, bloque. ) a la ligne puis « c » du premier bloque puis « a » (du deuxième, bloque.) a la ligne « b » (du deuxième, bloque.) a la ligne « c » (du deuxième, bloque.) a la ligne puis fin


```python 
x = 45 
y = 80
while x < 100 and y < 100 : 
    x =x + 1 
    y = y + 1 
    print(x,y)
```

>>>46 81  
47 82  
48 83  
49 84  
50 85  
51 86  
52 87  
53 88  
54 89  
55 90  
56 91  
57 92  
58 93  
59 94  
60 95  
61 96  
62 97  
63 98  
64 99  
65 100

La commande va donner cette réponse, car dans la commande, d’abord, le « x » commence à 45 et le « y » commence à 80 lignes de codage s’arrêta à 100 car c’est ce qui est marquer et dans ce codage, c’est quand le premier finit en l’occurrence le « y » l’autre s’arrête automatiquement.

Petit bonus : 
Break sert à quitter des boucles.

```python
for x in [0, 1, 6, 222]:
    print("salut")
```
cette commande permet de mettre autant de fois « salut » qui il y a de nombre à côté du « for x in » exemple : si a la place de [0, 1, 666, 222] il y aurait par exemple [0, 1, 666, 222, 35, 86, 25] il apparaîtra alors 7 fois salut, car il y a 7 nombres .

```python
for x in [0, 1,66, 222]:
    print("salut", x)
print("fini")
```
comme on a rajouter le x a coter de « "salut" » alors il y aura dans le shell (les résultats en bat ) a coter des « "salut" » il y aura les nombre choisit 

on peut aussi rajouter des mots 
```python
for x in [2, 2, "bonjour", 666, 222]:
    print("salut", x)
print("fini")
```
```python
for x in [2, 3, 2]:
    print("a", x)
    for y in [7, 1]:
        print("salut", y)
    print("b", x)
```
>>>a 2  
salut 7  
salut 1  
b 2  
a 3  
salut 7  
salut 1  
b 3  
a 2  
salut 7  
salut 1  
b 2

car comme dans le premier print il y a un « x » à coter du « a » il y aura un nombre qui va suivre en l’occurrence « 2 » puis ensuite à coter du premier « salut » il y aura un « 7 » car dans la commande a coter du « salut » il y a un « y » et que c’est le premier nombre dans la commande puis comme il y a deux nombre il y aura deux « salut » et du coup a coter du deuxième « salut » il y aura un « 1 » comme c’est le deuxième nombre. Puis pour le « b » c’est la même chose que pour le « a » comme il est au même niveau ‘contrairement au « salut » qui est à un cran au-dessus ) Donc, à coter du « b » il y aura un « 2 ». Pour la deuxième boucle, ça sera la même chose juste à la place du « 2 » il y aura un « 3 » vu que c'est la deuxième boucle.

```python
for x in [2, 3, 2]:
    print("a %s %s" %(x, x))
```
>>>a 2 2  
a 3 3  
a 2 2
Car dans la commande le « %s %s » est égale a « %(x, x) » ce qui est lui-même égale dans la première ligne du codage au premier « 2 » et pareil pour les deux autres boucles.

```python
for x in range (0,3) :
     print("a %s %s" %(x, x))
```
>>>a 0 0  
a 1 1  
a 2 2

Car pour la même raison que le précédent, mais dans ce cas-ci, on n’est pas obligé de mettre des chiffres choisit, on peut juste mettre le chiffre 
