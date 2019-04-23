def bissextile(annee):
    if annee%400==0 or (annee%4==0 and annee%100!=0):
        print("Oui")
    else:
        print("Non")
        
bissextile(10)