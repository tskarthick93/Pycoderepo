c=int(input("Entered natural number:"))
count=0
print ("Value c:",c)
while c != 1:       
    if c%2==0:
        c=c/2
        count  +=1
        print ("Value c:",int(c))
    elif c%2 != 0:
        c=3*c+1
        print ("Value c:",int(c))
        count  +=1
    else:
        print ("Value c:",int(c))
        count  +=1
print("Count value:",count)               