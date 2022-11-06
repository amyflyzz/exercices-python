### python

ctrl + c = copier
ctrl + v= collé 
pour utiliser " " ou () ou ’ dans une variable il faut entourer la variable 3 apostrophes ex :
 X « aujourd’hui il fait beau » 
 / ’’’aujourd’hui il fait beau ’’’
alors pour ne pas mettre les 3 apostrophes il faut mettre un slash avant la parenthèse, apostrophe, guillemet.  
«aujourd/’hui il fait beau »
Ou                                                              «/ aujourd’hui il fait beau / »

#### Calcul 
pour la division il faut utiliser  «/»
pour la somme «+»
pour la multiplication  «*»
pour la soustraction «-»
et pour l’égale «=»

#### =
avec l’égale ou peux faire devenir des mots en autre mot : 
```python
gâteau = bon
print ( gâteau)
bon
```

#### #
Les « # » servent à faire des commentaires qui ne se voient pas et qui ne changent rien 


#### %
Le % remplace le « * »  
Ex :
```python
monscore = 100 
message = « tu as obtenu %s pts » 
print ( message % monscore )
tu as obtenu 100 pts
```
quand il y a « %s », ça veut dire qu’il y a quelque chose qui va le remplacer, et quand il y a  « % », c’est un texte comme là avec monscore, c’est ce qu’il est égal au monscore qui va elle ici.
Ou sinon autre explication : dans le message, le %s est égal à monscore

#### les différentes listes 

Il y a deux sortes de listes :
la première sorte de liste est comme une sorte de bloc et qui s’écrit qu’avec juste deux guillemets (un au début et un à la fin ) 
la deuxième sorte liste où il y a plusieurs éléments distincts et chaque élément est entouré de crochets, guillemets ou apostrophes pour qu’il soit reconnaissable.

Exemple d’une liste avec plusieurs éléments distincts :
```python
Jour_de_la_semaine = ['demain', "c’est ",'samedi', 'donc',"c est", 'le' ,'week-end']
Print =( Jour_de_la_semaine[2])
'samedi'
```

Le « c’est » est entourer de guillemets au lieu d’apostrophes, car il y a une apostrophe dans l’élément. Aussi, dans une liste, on commence a compté à partir de 0. 

Pour ne prendre que certain élément, il faut faire :
```python
Jour_de_la_semaine = ['demain', "c’est ",'samedi', 'donc', "c’est", 'le' ,'week-end']
Print =( Jour_de_la_semaine[2:5])
'samedi', 'donc', "c’est", 'le'
```


ou peut aussi mettre deux chaines ensembles :
```python
liste_1 = ('a', 'b', 'c', 'd')
liste_2 = ('1', '2', '3', '4') 
print  (liste_1+liste_2)
('a', 'b', 'c', 'd', '1', '2', '3', '4')
```


Dans une liste, on peut aussi ajouter des choses grâce à « append » :
```python
liste_1 =['a', 'b', 'c', 'd']
liste_1.append ('e')
print (liste_1)
['a', 'b', 'c', 'd', 'e']
```

Et c’est la même chose pour « del »
```python
liste_1 =['a', 'b', 'c', 'd']
del liste_1 [3]
print (liste_1)
['a', 'b', 'c']
```

On peut aussi fusionner deux listes :
```python
liste_soleil = ['1','2','3']
liste_soleil2 = ['soleil']
liste_marrelle =liste_soleil+liste_soleil2
print (liste_marrelle)
['1', '2', '3', 'soleil']
```

ou les multiplier 
```python
liste_chiffre= ['1','2','3']
print (liste_chiffre*5)
['1', '2', '3', '1', '2', '3', '1', '2', '3', '1', '2', '3', '1', '2', '3']
```
mais aussi :
grâce «dict» (dictionnaire) on peut retrouver des éléments (valeur)grâce à un autre élément (la clé) :
```python
sport_pref={'joseph':'boxe','francois':'escalade','stephan':'natation','sophie':'basket','elodie':'velo'}
print (sport_pref ['joseph'])
boxe
```

#### turtle


