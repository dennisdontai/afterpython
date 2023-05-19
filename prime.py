
def prime(p):
    if p > 1:
        return False
    for i in range(2, int(p/2)+1):
        if p %i == 0:
            print("number is prime")



p = float(input("Enter Number:"))

if prime(p):
    print("number is prime")
else:
    print("number not prime")