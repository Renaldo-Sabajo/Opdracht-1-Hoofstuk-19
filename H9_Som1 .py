"""
Write a function my_nth_root(x,n,tol), where x and tol are strictly positive scalars, 
and n is an integer strictly greater than 1. The output argument, r, should be an 
approximation r=(x)**(1/N), the N-th root of x. This approximation should be computed by 
using the Newton Raphson method to find the root of the function f(y)=y**N−x. The error 
metric should be |f(y)|.
"""
---------------------------------------------------------------------------------------------------
import numpy as np

# Definieer x>0, n>1, tol>0, f(y), en N
# Definieer my_nth_root(x,n,tol)
# x en n zijn vrije variabelen die ingevuld moeten worden (constanten)

# Output is een estimation van de wortel van f(y)
# Wortel van f(y) is r = x**(1/n)
# Gebruikmakend van de Newton Raphson Method
# Recusrsive Implementation
# We geven een maximale waarde aan de tolerance, dat is 0.0001
# De Newton Raphson formule wordt dan: y1 = y0 - (f / f_prime)

def my_nth_root(x,n,tol):
    f = lambda y: (y**n) - x
    f_prime = lambda y: n * (y**(n-1))
    # y0 is een startwaarde, bijvoorbeeld
    y0 = float(input("Kies een beginwaarde: y0 = "))
    n_r = y0 - (f(y0))/(f_prime(y0))
    n > 1
    x > 0
    tol > 0
    if tol < 0.0001: break
    
    
    
    # Concept: new_n_r = n_r - (f(n_r))/(f_prime(n_r)) --> zo iets moeten we maken in recurion vorm
    # COncept: We moeten een subfunctie maken voor de recursie van de Newton Raphson formule
    # De begin waarde opvragen van de gebruiker 
    
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


# Hi Renaldo, ik heb dit erbij geplaatst. Er zijn ook wat andere aanpassingen. Hieronder kan je 
# zien hoe de iteratie erbij kan. Nu dit samen zetten met wat je boven hebt.
# De iteratie zal 5 keer uitgvoerd worden
# noem de volgende y waarde y_next

for i in range(5):
 y_next = y - (f / f_prime)
 if abs(y_next - y)> 0.0001: break
    y = y_next 
    
print ( '
    
___________________________________________________________________________________________________________________________________________________________________________
 #Bisection Method: dit is maar een concept 
def my_nth_root(x,n,tol):
       f = lambda y: (y**n) - x
       print("Kies de grenzen voor het interval [a,b]:")
       def bisection(a,b):
       # Middelpunt definieren van de interval 
            a = float(input("a = "))
            b = float(input("b = "))
            m = (a+b)/2
            f = lambda y: (y**n) - x
            # Na gaan als er een wortel tussen de eindpunten a en b ligt 
       if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("er zit geen wortel tussen de eindpunten a and b")
        
        # We stoppen de recursion indien de approximate error is < tolerance
       if np.abs(f(m)) < tol:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            # Geval waar f(b) en f(m) tegengestelde tekens hebben dan kiezen we interval [m,b] 
            # Maak een recursive call met a = m
            return bisection(m, b)
        elif np.sign(f(b)) == np.sign(f(m)):
            # Geval waar f(a) en f(m) tegengestelde tekens hebben dan kiezen we interval [a,m]
            # Maak een recursive call met b = m
            return bisection(a, m)
     
# Zelfde voorbeeld als bij Newton Raphson Methode 
r1 = my_nth_root(2,2,1e-6)
print(r1)       

# Ik kwam hierop, weet niet zeker als het correct is.
    
def my_nth_root(a,n,tol):
    f = lambda y: (y**n) - a
    n > 1
    a > 0
    tol > 0
    
    def midpoint(p, q):
        m = (p + q)/2
        if np.abs(f(m)) < tol:
            return m
        elif np.sign(f(p)) == np.sign(m):
            return midpoint(m, q)
        elif np.sign(f(q)) == np.sign(m):
            return midpoint(p, m)
        
    return my_nth_root
print ('de wortel bij a = 2, n = 2 en tol = 0.01 is', my_nth_root(2, 2, 0.01)
    
    
       
#--------
# Fixed point iteration

#Algoritme:
# maak een functie die a, n en tol neemt, noem my_nth_root
# herschrijf f(y) in de vorm van y = ...
# definieer de functie g(y)
# definieer de functie dg/dy 
# g(y) = y
# Check als abs(dg/dy) < 1 dan een unieke fixed point
# maak een andere functie in de huidige die de beginschatting opvraagt met y_past en de beginschatting, y0, als parameters , noem kies_waarde 
# met deze beginwaarde wordt de fixed point, g(y) = y berekend
# y_past is de variabele van de vorige iteratie, y  is die van de volgende
# Er moet een elif statement komen, nog niet zeker hoe dat erbij moet 
# g(y_past) = y
# return y 



# Regula Falsi Mehtode
# 
# maak een functie die a, n en tol neemt, noem my_nth_root
# maak een andere functie in de huidige die de beginschatting opvraagt met p en q als argumenten , noem kies_waarden 
# Bereken f(p) en f(q)
# maak c_begin = q - (f(q) * (q - p))/ (f(q) - f(p))
# 
    
