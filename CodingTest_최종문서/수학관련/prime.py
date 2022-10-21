
def isPrime(N):
    for i in range(2, int(N**1/2)):
        if N%i==0: return False
    return True

print(isPrime(17))
print(isPrime(24))

def Sieve_of_Eratosthenes():
    n=1000
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
        print(primes)