"""
Write a function my_nth_root(x,n,tol), where x and tol are strictly positive scalars, 
and n is an integer strictly greater than 1. The output argument, r, should be an 
approximation r=(x)**(1/N), the N-th root of x. This approximation should be computed by 
using the Newton Raphson method to find the root of the function f(y)=y**N−x. The error 
metric should be |f(y)|.
"""
---------------------------------------------------------------------------------------------------
import numpy as np

# Definieer x, n, tol, f(x), en N
# Definieer my_nth_root(x,n,tol)
# x en n zijn gewoon variabelen die ingevuld moeten worden (constanten)
# x maakt geen deel uit van de functie

# Output is een estimation van de wortel van f(y)
# Root of wortel van f(y) is y = r = x**(1/n)
# Gebruikmakend van de Newton Raphson Method
# Recusrsive Implementation

def my_nth_root(x,n,tol):
    f = lambda y: (y**n) - x
    f_prime = lambda y: n * (y**(n-1))
    r = x**(1/n) 
    # y moeten we nog defieneren, y is een beginpunt 
    y = 1.4
    newton_raphson = y - (f(y))/(f_prime(y))
    if abs(f(y)) < tol:
        return y
    else:
        print('newton_raphson',newton_raphson)

#Voorbeeld (Zelfde gegevens als van dat boek) 
print (my_nth_root(2,2,1e-6))
    