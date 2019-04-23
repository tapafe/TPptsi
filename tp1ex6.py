from time import *
before = time()
t = int(input("Rentrer le nombre de seconde \n"))
print (t, "secondes correspont à: ", t//(60*60*24), "jours", (t%(60*60*2))//3600, "heures", (((t%(60*60*2))//3600)%3600)//60, "minutes", ((((t%(60*60*2))//3600)%3600)//60)%60, "secondes" )
after = time()
print ("le temps d'exécution de l'affichage de la phrase à été de: ", after-before)