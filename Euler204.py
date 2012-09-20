#-------------------------------------------------------------------------------
# Name:        pyLambda Hamming
# Purpose:     NoOfHamming returns the number of N-Hamming Numbers below Max
# Refernce:    Project Euler - Problem 204
# Author:      particle.mania
# Created:     20-09-2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#Borrowed Concepts
from TJ import Sigma, Mult, Curry2, Tupel
from Prime import Primes


#Global States (Free Variables)
Max = 10**9
N = 100
Roots = Primes(N)


#Functions
p = Curry2(Mult)

LatticeChildren = lambda V: map(Tupel,map(p(V[0]),Roots[:V[1]]),range(1,V[1]+1))

F = lambda V: 1 + Sigma(map(F,filter(lambda x: x[0]<=Max,LatticeChildren(V))))


#Output
NoOfHamming = F((1,len(Roots)))