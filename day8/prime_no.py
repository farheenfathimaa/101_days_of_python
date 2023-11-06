n=int(input("Enter a number: "))
def prime_checker(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("It's a prime number") 
    else:
        print("It's not a prime number") 
prime_checker(n)