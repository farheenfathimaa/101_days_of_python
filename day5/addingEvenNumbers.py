a=int(input("Enter the first number: "))
b=int(input("Enter the last number: "))
sum=0
for i in range(a,b+1):
    if i%2==0:
        sum+=i
print(f"The sum is: {sum}")