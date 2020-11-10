# f="from"
# t="to"
# v="via"
# h="helper"

def move(f,t) :
    print("Move from {} to {}.".format(f,t))

move("WDC","001")

def moveVia(f,v,t) :
    move(f,v)
    move(v,t)

moveVia("Patagonia","EDC","003")


#towers of hanoi game solver
def hanoi(n,f,h,t) :
    if n==0 :
        pass
    else :
        hanoi(n-1,f,t,h) #
        move(f,t)
        hanoi(n-1,h,f,t)

#three slotting locations, lighter package must go on top. move all units from a to c.
locationA = ["Vancouver","British Columbia", "Canada"]
locationB = ["Surrey","British Columbia","Canada"]
locationC = ["Dawson City","Yukon","Canada"]

hanoi(5,locationA[0], locationB[0],locationC[0])

def factorial(n) :
    if n < 0 :
       return -1
    elif n < 2 :
        return 1
    else :
        return n * factorial(n-1)

print(factorial(10))
