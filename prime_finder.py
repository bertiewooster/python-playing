def prime_finder(n):
  # Write your code here
 primes = []
 for i in range(n+1):
   if is_prime(i):
     primes.append(i)

def is_prime(number):
  for i in range(2,number):
    if number % i == 0:
      return False
  return True

print(prime_finder(11))