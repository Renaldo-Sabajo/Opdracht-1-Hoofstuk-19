"""
Write a function my_nth_root(x,n,tol), where x and tol are strictly positive scalars, 
and n is an integer strictly greater than 1. The output argument, r, should be an 
approximation r=(x)**(1/N), the N-th root of x. This approximation should be computed by 
using the Newton Raphson method to find the root of the function f(y)=y**N−x. The error 
metric should be |f(y)|.
"""
---------------------------------------------------------------------------------------------------
import numpy as np

# Definieer x>0, n>1, tol>0, f(x), en N
# Definieer my_nth_root(x,n,tol)
# x en n zijn vrije variabelen die ingevuld moeten worden (constanten)

# Output is een estimation van de wortel van f(y)
# Wortel van f(y) is r = x**(1/n)
# Gebruikmakend van de Newton Raphson Method
# Recusrsive Implementation

def my_nth_root(x,n,tol):
    f = lambda y: (y**n) - x
    f_prime = lambda y: n * (y**(n-1))
    # y0 is een startwaarde, bijvoorbeeld
    y0 = 1.5
    n_r = y0 - (f(y0))/(f_prime(y0))
    n > 1
    x > 0
    tol > 0
    r = x**(1/n)
    return r
    
    # Concept: new_n_r = n_r - (f(n_r))/(f_prime(n_r)) --> zo iets moeten we maken in recurion vorm
    # COncept: We moeten een subfunctie maken voor de recursie van de Newton Raphson formule

    def new_n_r(y0):
        f = lambda y: (y**n) - x
        f_prime = lambda y: n * (y**(n-1))
        n_r = y0 - (f(y0))/(f_prime(y0))
        if abs(f(y0)) < tol:
            return y0
        else:
            return new_n_r(n_r)
    r = new_n_r(n_r)
    return r
    
#Voorbeeld (Zelfde gegevens als van dat boek) 
print ("the root of the function is r = ", my_nth_root(2,2,1e-6))

    
