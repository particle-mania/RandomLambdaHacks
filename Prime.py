#-------------------------------------------------------------------------------
# Name:        Prime.py
# Purpose:     {Primes:int->list(int)} generates the first n primes for input n
# Author:      particle.mania
# Created:     20-07-2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from TJ import Divides

notMultiple = lambda d: lambda n: not Divides(d)(n)

Sieve = lambda L: [L[0]] if len(L)==1 else [L[0]] + Sieve(filter(notMultiple(L[0]),L[1:]))

Primes = lambda n: Sieve(range(2,n+1))