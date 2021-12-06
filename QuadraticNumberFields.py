#In this file we present some functions to deal with norms and invertible elements in quadratic number fields, that is fields of the form Q(sqrt(D)) where D
#is a square free integer.

#Remember that the norm in such field is given by the formula
#N(a+b*sqrt(D))= a^2+D*b^2

#A member a+b*sqrt(D) is invertible in Z[sqrt(D)]={a+b*sqrt(D): a,b in ZZ}
#if and only if it's norm is equal to +-1

#When D is negative we can check many things easily.

import numpy as np

#The next function determines if there is an element in Z[\sqrt{-D}] whose norm is equal to z.

def sol_norm(D,z):
#Says if there is an element alpha=a+b\sqrt{-D} such that N(alpha)=a^2+Db^2=z.
#Observe that the range can be a^2 <=z y Db^2 <= z, and given that a and b are integers
#then we can use a between 0 and ceil(\sqrt{z}) y b between 0 and ceil(\sqrt{z/D}).

    resp = False
    lim_a= ceil(np.sqrt(z)) + 1
    lim_b= ceil(np.sqrt(z/D)) + 1
    for a in range(0,lim_a):
        for b in range(0,lim_b):
            if(a^2+D*b^2==z): resp=True
    return(resp)
    
    
def sol_norm_element(D,z):
#Returns a list of elements a+ b\sqrt{-D} of Z[\sqrt{-D}] such that N(a+b\sqrt{-D})=z
#The number sqrt{-D} is written as w
    K.<w> = NumberField(x^2 + D)
    if(sol_norm(D,z)==True):
       lim_a= ceil(np.sqrt(z)) + 1
       lim_b= ceil(np.sqrt(z/D)) + 1 
       v=[]
       for r in range(0,lim_a):
           for s in range(0,lim_b):
               if(r^2+D*s^2==z): 
                   v.append(r+s*w)
                   v.append(r-s*w)
       return(list(set(v)))
    else: print('There is no solution')
    
    
#The next function determines if an element of Z[\sqrt{-D}] is irreducible or not.
#If it is reducible then it will return a list of factorizations by two non-units.


def is_irreducible_in_number_field(alpha, D):

    K.<w>= NumberField(x^2+D)
    if(alpha in K):
       N=norm(alpha)
    
       listdiv = [r for r in divisors(N) if r>1 and r<N and r<=median(divisors(N))] 
       #Returns non trivial divisors of N, paired to avoid repetitions in our answer.
       resp=True
    
       #For each n we have to see if there are beta, gamma en Z[\sqrt{-D}]
       #such that N(beta)= n and N(gamma)=N/n and also that beta*gamma=alpha.
       #If we don't find them then the element is irreducible.
       #If we find them then the function will display them.
       u=[]
       for n in listdiv:
           if(sol_norm(D,n)==True and sol_norm(D,N/n)==True):
               #This tells us if there are elements with these norms.
               v1=sol_norm_element(D,n)
               v2=sol_norm_element(D,N/n)
               if(alpha in [a*b for a in v1 for b in v2]):
                     u.append(set([ (a,b) for a in v1 for b in v2 if a*b==alpha]))
                     resp=False
           
       if(resp==False):
           print(f'This element es reducible. Some factorizations of {str(alpha)} as a product of two non-units are')
           print(u)
       else: print('This element is irreducible.')
       
  
  #When D>0 the situation is different. Infinite elements can have norm equal to one. This is Pell's Equation: x^2-Dy^2=1.
  #We present the function to compute the fundamental solution from Pell's equation.
  
  #Taken from http://mathsci.kaist.ac.kr/cms/wp-content/uploads/2017/11/NumberTheory_Sage.pdf
  
  def solve_pell (N , numTry = 100):
    cf = continued_fraction(sqrt(N))
    for i in range(numTry):
        denom = cf.denominator(i)
        numer = cf.numerator(i)
        if(numer ^2 - N * denom ^2 == 1): return (numer, denom)
    return('You need a higher number of steps') 