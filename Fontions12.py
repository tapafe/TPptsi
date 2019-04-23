def bissextile(annee):
    if annee%400==0 or (annee%4==0 and annee%100!=0):
        return True
    else:
        return False
        
        
def jours(mois, annee):
    if mois%2 == 1 or mois == 8:
        print("31")
    elif mois != 2:
        print("30")
    else:
        if bissextile == True:
            print("29")
        else:
            print("28")
        
     
               
  
a = bissextile(2020)
jours(2, 2020)