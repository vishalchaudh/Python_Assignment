def num(x):
    i=j=1
    while j<=x:
        if i%2==0:
            print(i,end="")
            j=j+1
        i=i+1
x=(int(input("enter the number")))
num(x)