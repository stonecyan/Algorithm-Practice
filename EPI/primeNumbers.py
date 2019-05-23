    
def primeNumbers(n):
    if n < 2:
        return []
    primes = [2]
    isPrime = [True]*((n-3)//2+1)
    i=3
    while i<=n:
      if isPrime[i//2-1]:
        primes.append(i)
      if i+i*2<n: 
        for x in range(i*3, n, i*2):
          isPrime[(x-1)//2-1]=False
      i+=2
    return primes

x=primeNumbers(27)
print(x)
