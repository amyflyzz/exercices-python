for x in  [1, 2, 33]:
    print("La valeur de x ext: %s" % x)
    





x = 3
print("x: %s oo %s" % ("salut", x))
print("x:", "salut", "oo", x)
print("fini")





for coucou in [2, 3, 2]:
    #print("a %s %s" %(coucou, coucou))
 print("fini")








for coucou in [2, 3, 2]:
    print("a", coucou)
    for voila in [7, 1]:
        print("salut", voila)
    print("b", coucou)
print("fini")






range(0, 3) [0, 1, 2]
range(0, 7) [0, 1, 2, 3, 4, 5, 6]

for x in [2, 2, 2]:
    for y in [1, 1, 1]:
        print(x, y)
print("fini")









for x in [2, 2, "bonjour", 666, 222]:
    print("salut", x)
print("fini")





print("a")
print("b")
print("c")
for x in [0, 1, 666, 222]:
    print("salut")
print("fini")











salaire = 100
pourboire = 10
vole = 5
pieces = salaire 
for semaine in range (1,53): 
    pieces = pieces + pourboire - vole 
    print ('semaine %s =%s' % (semaine, pieces))
