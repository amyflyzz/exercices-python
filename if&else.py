age =2
if age == 1 :
    print('tu es a la garderie')
elif age == 0 :
    print('tu es pas encore vivant')
elif age >= 2 and age <= 5 :
    print ('tu es a la maternele')
elif age >= 6 and age <= 10 :
    print ('tu es en primaire')
elif age==11 or age==12 or age==13 or age==14 or age==15  :
    print ('tu es au college')
elif age >= 16 and age <= 18 :
    print ('tu es en lycee')
elif age >= 19 and age <= 25 :
    print ('t etudiant')
elif age >= 25 and age <= 65 :
    print ('tu as un emploi')
elif age >= 65 and age <= 100 :
    print ('t es a la retraite ')
elif age == None :
    print ('tu n existes pas')
elif age >= 101 and age <= 200 :
    print ('tu vas bientot mourir')
else : 
    print ('t mort ')
