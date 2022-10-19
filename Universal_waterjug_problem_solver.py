x=0
y=0
Initial = (x,y)
print ("Initial State is (0,0)")
print ("Enter Capacities of each jug ")
o = int(input())
p = int(input())
capacities = (o,p)
print ("your desired Capacities are ")
print (o,p)
print("Enter your Desired goal state(According to capacities assigned)")
m = int (input())
n = int (input())
goal = (m,n)
print ("Goal state is")
print(goal)
print ("Rule 1 = Jug 1 empty")
print ("Rule 2 = jug 2 empty")
print ("Rule 3 = jug 1's Water is transfered to Jug 2")
print ("Rule 4 = jug 2's Water is transfered to jug 1")
print ("Rule 5 = jug 1 full")
print ("Rule 6 = jug 2 full") 
while x!=m or y!=n:
    r = int(input("enter rule : "))
    if r==1:
        x=0
    elif r==2:
        y=0
    elif r==3:
        t=p-y
        if t>x:
            y+=x
            x=0
        elif t<x:
            y=p
            x-=t
    elif r==4:
        t=o-x
        if t>y:
            x+=y
            y=0
        elif t<y:
            x=o
            y-=t
    elif r==5:
        x=o
    elif r==6:
        y=p
    else :
        print("Wrong Input")
    print ( x,y )
