a=int(input("enter the number:"))
def fact(num):
    fact = 1
    for i in range(num,0,-1):
        fact=fact*i
    print("factorial=",fact)
fact(a)
