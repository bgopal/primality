#!/usr/bin/python

primeSeed=[2,3,5,7]
step=4

last = lambda pl: pl[len(pl)-1]

def isPrime(n):
	print primeSeed
	if n<last(primeSeed):
	# if n is less than 10, then just check if it is in primeSeed
		if n in primeSeed:
			return True
		else:
			return False
	elif n<last(primeSeed)*last(primeSeed):
	# if n>=ps and n<ps**2
		for p in primeSeed:
			if n%p:
				if p*p>n:
					return True
				else:
					continue
			else:
				return False
	else:
	# I do not have enough primes to test this number
	# let me extend primes upto sqrt(n) and then check
		while True:
		# loop to add one prime to primeSeed
		# this loop adds one prime at a time
			global step
			nextPrime = last(primeSeed)+step
			step=6-step
			foundPrime=False
			for p in primeSeed:
				if p*p>nextPrime:
					foundPrime=True
					break
				if nextPrime%p:
					continue
				else:
					nextPrime+=step
					step=6-step
			if foundPrime:
				primeSeed.append(nextPrime)
				if last(primeSeed)*last(primeSeed)>n:
				# I have found enough primes now
				# I can call myself to check if n is a prime now
					return isPrime(n)

print isPrime(9973)
