blocks = int(input("Enter the number of blocks: "))

height = 0

inlayer = 1

while inlayer <= blocks:
   
    height += 1
    print("h:",height)
    blocks -= inlayer
    print("b:",blocks)
    inlayer += 1
    print("I:",inlayer)

print("The height of the pyramid: ", height)

