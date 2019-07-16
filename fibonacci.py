
x=int(input("enter the num"))
sum=0
temp=x
r=0
while x>0:
    r=x%10    
##    print(r)
    x=int(x/10)
    sum=sum+r**3

##print(sum)

##print(3**3+1**3+5**3)
    
if(sum==temp):
    print("armstrong")
else:    
    print("no")
