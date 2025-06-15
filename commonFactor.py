import math

def pgcd(a, b):
   
    while b != 0:
        a, b = b, a % b
    return a

def attaque_facteur_commun(n1, n2):
   
    # Calcul du PGCD
    facteur_commun = pgcd(n1, n2)
    
    if facteur_commun > 1 and facteur_commun != n1 and facteur_commun != n2:
       
        p = facteur_commun
        q1 = n1 // p
        q2 = n2 // p
        
        print(f"Facteur commun trouvé : {p}")
        print(f"Facteurs de n1 = {n1} : {p} × {q1}")
        print(f"Facteurs de n2 = {n2} : {p} × {q2}")
        
        return p, q1, q2
    else:
        print("Aucun facteur commun trouvé")
        return None, None, None

n1 = int(input("Entrez n1 : "))
n2 = int(input("Entrez n2 : "))


p, q1, q2 = attaque_facteur_commun(n1, n2)