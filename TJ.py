#-------------------------------------------------------------------------------
# Name:        Standard Personal Library for pyLambda
# Author:      particle.mania
# Created:     08-09-2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#Mathematical Symbols

Sigma = lambda L: reduce(lambda x,y: x+y, L, 0)

Product = lambda L: reduce(Mult,L,1)

Delta = lambda L: [L[i]-L[i-1] for i in range(1,len(L))]

Mult = lambda x,y: x*y

Divides = lambda d: lambda n: n%d==0

isDividedBy = lambda n: lambda d: n%d==0


#Functional Idioms

Curry2 = lambda f: lambda x: lambda y: f(x,y)

InvCurry2 = lambda g: lambda x,y: g(x)(y)

Tupel = lambda p,q : (p,q)
