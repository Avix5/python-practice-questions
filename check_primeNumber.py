
user=int(input("enter a number to check its prime or not"))

if user % user==0:
    print(user,"is a prime number")
else:
    print(user,"it is not a prime number")
is_Prime=True
for i in range(2,user):
    if user%i==0:
        # print(user,"is not a prime number")
        is_Prime=False
if is_Prime:
    print(user,"is prime number")
else:
    print(user,"is not a prime number")
