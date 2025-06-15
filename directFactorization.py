import math

def p_and_q(phi_n, n):
    
    p_plus_q = n + 1 - phi_n
    
    discriminant = p_plus_q**2 - 4*n
    
    if discriminant < 0:
        print("Erreur: discriminant négatif")
        return None, None
    

    sqrt_discriminant = math.sqrt(discriminant)
    
    p = (p_plus_q + sqrt_discriminant) / 2
    q = (p_plus_q - sqrt_discriminant) / 2
    
    if p.is_integer() and q.is_integer():
        return int(p), int(q)
    else:
        return None, None

n = int(input("Entrez n : "))
phi_n = int(input("Entrez φ(n) : "))

p, q = p_and_q(phi_n, n)

if p and q:
    print(f"Facteurs premiers de n : {p} {q}")
else:
    print("Factorisation impossible")