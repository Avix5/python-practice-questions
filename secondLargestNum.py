arr = [10, 20, 4, 45, 99]
largest=0
second=0

for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(f"{second} is the second largest number")
