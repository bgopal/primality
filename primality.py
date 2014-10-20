#!/usr/bin/python
import math

"""
Routines to check primality of a given number.
"""

# global variables
prime_seed=[2,3,5,7]
prime_step=4
prime_bmp=[3]
last_bit, last_n=0,0
chunksz=32
chunksz_width=int(math.log(chunksz,2))

last = lambda pl: pl[len(pl)-1]

def isPrime(n):
	"""
	isPrime(n): Returns True if n is prime. Returns False otherwise.
	"""
	global prime_seed
	if n<last(prime_seed):
	# check if n is in prime_seed
		if n in prime_seed:
			return True
		else:
			return False
	elif n<last(prime_seed)*last(prime_seed):
	# if n>=ps and n<ps**2: I have enough primes to 
	# check if p is prime
		for p in prime_seed:
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
		global prime_step
		nextPrime = last(prime_seed)+prime_step
		prime_step=6-prime_step
		foundPrime=False
		while True:
		# loop to add one prime to prime_seed
		# check if nextPrime is a prime
			for p in prime_seed:
				if nextPrime%p:
					if p*p>nextPrime:
						foundPrime=True
						break
					continue
				else:
					break
			if foundPrime:
				prime_seed.append(nextPrime)
				if nextPrime*nextPrime>n:
				# I have found enough primes now
				# I can call myself to check if n is a prime now
					return isPrime(n)
			foundPrime=False
			nextPrime+=prime_step
			prime_step=6-prime_step


def idx_and_bit(n):
	""" Find the idx and bit position in the bitmap array given 
	a number. Returns a tuple (idx,bit)"""
	# assuming 32-bit integer array for prime_bmp
	# the first 27 bits will give the array index
	idx=(n>>chunksz_width)
	# the last 5 bits give the bit position
	bit=(n&(chunksz-1))
	return (idx, bit)

def sieve(n):
	""" Find all primes upto and including n"""
	global prime_bmp
	global last_n, last_bit

	if (n <= last_n):
		return
	
	(idx,bit)=idx_and_bit(n)
	# if we require more than what is allocated in prime_bmp
	# extend the array	
	if ((len(prime_bmp)-1) < idx):
		prime_bmp[len(prime_bmp):idx]=[0 for x in range(len(prime_bmp),idx+1)]

	p=2
	while (p<=math.sqrt(n)):
		mark_all_mults(p, last_n, n)
		p=find_next_prime(p)
	last_n=n

def find_next_prime(p):
	p+=1
	(idx,bit)=idx_and_bit(p)
	while (prime_bmp[idx]&(1<<bit)):
		p+=1
		(idx,bit)=idx_and_bit(p)
	return p

def mark_all_mults(p, last_n, n):
	if (last_n==0):
		s=p**2
	else:
		s=((last_n+p-1)/p)*p
	while (s<n):
		mark_as_composite(s)
		s+=p

def mark_as_composite(s):
	(idx,bit)=idx_and_bit(s)
	prime_bmp[idx] |= (1<<bit)

def is_prime_sieve(n):
	(idx,bit)=idx_and_bit(n)
	if (prime_bmp[idx]&(1<<bit)):
		return False
	else:
		return True
