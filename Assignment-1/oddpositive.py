import random

n = random.randint(-10,10)

if n % 2 == 0 and n > 0:
    print(n, "is even and positive")

elif n % 2 == 0 and n < 0:
    print(n, "is even and negative")

elif n % 2 == 1 and n > 0:
    print(n, "is odd and positive")

else:
    print(n, "is odd and neagtive")