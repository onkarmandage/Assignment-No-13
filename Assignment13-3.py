num=int(input("Enter the number "))
original=num
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if original==sum:
    print("number is perfect")
else:
    print("number is not perfect")