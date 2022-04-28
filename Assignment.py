x = int(input('enter a number:'))
y = []
z = []
prime = []

def finding_value(n):
    value = [True] * n
    for p in range(2, n):
        if value[p]:
            prime.append(p)
            for i in range(p*p, n, p):
                value[i] = False
    return prime

finding_value(x)
max_counter = 0
a = 5000
for prime_number in prime:
    if prime_number < a:
        prime_index = prime.index(prime_number)
        check = prime_number
        counter = 1
        while check < x:
            check += prime[prime_index + counter]
            counter += 1
            if check in prime:
                if counter > max_counter:
                    y.append(counter)
                    z.append(check)

answer = z[y.index(max(y))]
print(answer)