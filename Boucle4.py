def ecrirePunition(texte, n):
    f_texte = texte
    f_n = n
    for i in range(n):
        print(str(i+1) + " " + texte)
        
ecrirePunition("Coucou", 5)