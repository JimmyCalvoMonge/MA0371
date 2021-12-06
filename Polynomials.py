#Some functions for multivariate polynomial algorithms.
#Anyone is free to use them in COCALC, which is the platform they were ment to be used at.

#Polynomial division in two variables.
def polynomial_division(f,D):
    R.<x,y> = PolynomialRing(QQ, 2, 'xy', order='lex')
    lterms =[g.lt() for g in D]
    if(f==0):
       return([0 for i in range(0,len(D))])
    else:
       ct=0
       for i in range(0,len(D)):
    			        if(R.monomial_divides(lterms[i],f.lt()) and ct==0):
                                                            a=(f.lt()).quo_rem(lterms[i])[0]
                                                            Q= polynomial_division(f-a*D[i],D)
                                                            Q[i]= Q[i]+a
                                                            ct=1
       if(ct==1):
         return Q
       else:
         return(polynomial_division(f-f.lt(),D))
 
 
#Explanation: Given a polynomial f and a list of divisors D=[g1,g2,...,gm], all being polynomials in the variables x,y over the rationals,
#this algorithm finds a set of quotients f_1,f_2,...,f_n and a residual r, all in the ring of polynomials QQ[x,y] such that
#f= f_1g_1+f_2g_2+...+f_mg_m + r and no monomial term of the residual r divides any of the leading terms of any g_i.

#This is done with the lexicographic order x>y howver it can be changed to the order y<x setting
R.<y,x> = PolynomialRing(QQ, 2, 'yx', order='lex')
#At the beginning of the function.

#The function can be modified to add more variables. For example in QQ[x,y,z] with the order x>y>z we can use
R.<x,y,z> = PolynomialRing(QQ, 2, 'xyz', order='lex')

#Naturally the field of constants can be changed as well.
#The description of the algorithm is in page 320 of 'Abstract Algebra' by David Dummit and Richard Foote.
#Check out section 9.6 for the general theory of Gröbner bases as well.#Some functions for multivariate polynomial algorithms.
#Anyone is free to use them in COCALC, which is the platform they were ment to be used at.


#Polynomial division in two variables.

def polynomial_division(f,D):
    R.<x,y> = PolynomialRing(QQ, 2, 'xy', order='lex')
    lterms =[g.lt() for g in D]
    if(f==0):
       return([0 for i in range(0,len(D))])
    else:
       ct=0
       for i in range(0,len(D)):
    			        if(R.monomial_divides(lterms[i],f.lt()) and ct==0):
                                                            a=(f.lt()).quo_rem(lterms[i])[0]
                                                            Q= polynomial_division(f-a*D[i],D)
                                                            Q[i]= Q[i]+a
                                                            ct=1
       if(ct==1):
         return Q
       else:
         return(polynomial_division(f-f.lt(),D))
 
 
#Explanation: Given a polynomial f and a list of divisors D=[g1,g2,...,gm], all being polynomials in the variables x,y over the rationals,
#this algorithm finds a set of quotients f_1,f_2,...,f_n and a residual r, all in the ring of polynomials QQ[x,y] such that
#f= f_1g_1+f_2g_2+...+f_mg_m + r and no monomial term of the residual r divides any of the leading terms of any g_i.

#This is done with the lexicographic order x>y howver it can be changed to the order y<x setting
R.<y,x> = PolynomialRing(QQ, 2, 'yx', order='lex')
#At the beginning of the function.

#The function can be modified to add more variables. For example in QQ[x,y,z] with the order x>y>z we can use
R.<x,y,z> = PolynomialRing(QQ, 2, 'xyz', order='lex')

#Naturally the field of constants can be changed as well.
#The description of the algorithm is in page 320 of 'Abstract Algebra' by David Dummit and Richard Foote.
#Check out section 9.6 for the general theory of Gröbner bases as well.