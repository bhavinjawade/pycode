def getFirstNPrimes(N):
    table = [True]*(N+1)
    # 0 and 1 are neither prime nor composite:
    table[0] = table[1] = False
    # 2 is the first prime number
    p = 2
    while p*p <= N:
        if table[p] == True:
            for j in range(p*p, N+1, p):
                table[j] = False
        p += 1
    
    # printing all the prime numbers:
    for index, value in enumerate(table):
        if value == True:
            print(index, end=' ')

if __name__ == '__main__':
    N = int(input("Enter a number: "))
    getFirstNPrimes(N) 