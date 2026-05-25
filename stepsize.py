new_list = [1,2,3,4,5,6,7,8,9,10]
print(new_list[2:7:-1])
#loops#
#while loop
#num = int(input("what number do you want to see the multplication of "))
#lim = int(input("what is the limit: "))
#i = 1
#while (i <= lim):
    #print(f"{num} x {i} = {num * i}")
    #i +=1
n = int(input("Enter any number you wish to stop at: "))
j = 1
print("Start:\n")
while (j<=n):
    print(j)
    j+=1
print("Stop")
k =1
h = int(input("Enter a number:"))
while(k<=h):
    if(k%2 == 0):
        print(f"{k} is an even number")
    else:
        print(f"{k} is an odd number")
    k+=1