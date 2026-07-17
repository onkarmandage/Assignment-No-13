num=int(input("Enter the Number :"))
binary=""
if num==0:
    print("binary equivalent is :0")
else:
    while num>0:
        rem=num%2
        binary=str(rem)+binary
        num=num//2
    print("binary equivalent is :",binary)