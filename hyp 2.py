#import parser
from math import *
print("!!!Warning!!! x-coordinate is not automatically put into a negative in the answer. Check your start point to determine if the x-coordinate should be negative!")
while True:
    print("\nexample: 1 2 3")
    eqn= input("Enter values for a hyperbola in tbe form Ax^2 + By^2 = C; input \"A B C\": ")
    #eqn = "2 -8 10"
    point = input("Enter a start point in form \"x,y\": ")
    #point = "0,-4"
    data1 = eqn.split(" ")
    a = data1[0]
    b = data1[1]
    c = data1[2]

    data2 = point.split(",")
    xcor = data2[0]
    ycor = data2[1]

    #pretend these x variables are actually y
    #newtop = "2*(("+c+"-"+b+"*x**2)/("+a+")-"+ycor+")*(-2*("+b+"/"+a+")*x)+2*(x-"+ycor+")"
    #this is the nasty calculus part
    new = "((-2*"+b+"*x)/"+a+")*(1-(2*"+xcor+")/(2*(("+c+"-"+b+"*x**2)/+"+a+")**.5))+2*(x-"+ycor+")"
    #newbottom = "2*(((("+c+"-"+b+"*x**2)/"+a+")-"+ycor+")**2+(x-"+ycor+")**2)**.5"
    #new = "("+newtop+")/"+"("+newbottom+")"
    #new = "((-2*("+b+"/"+a+")*x)/(2*(("+c+"-"+b+"*x**2)/"+a+")**.5))" "+2*(x-" + ycor + ")"+"=0"
    data = new.split("=")
    global left

    left = data[0]
    cont = 1
    low=0
    du=10
    dj=10
    guess = 0
    u = guess
    j = guess
    iterations = 0
    print("Hyperbola:",a,"x^2+",b,"y^2=",c)

    #this is my algebraic solver
    while cont == 1:
        #st1 = parser.expr(left)
        #code1 = st1.compile("file.py")
        x=u
        high = eval(left)
        #print(high)
        if high<0 and low>0:
            if abs(low)<abs(high):
                u = j
                j = j
                du = du/10
                dj = dj/10
            if abs(high)<abs(low):
                u = u
                j = u
                du = du/10
                dj = dj/10
        if high>0 and low<0:
            if abs(low)<abs(high):
                u = j
                j = j
                du = du/10
                dj = dj/10
            if abs(high)<abs(low):
                u = u
                j = u
                du = du/10
                dj = dj/10
        
        #st2 = parser.expr(left)
        #code2 = st2.compile("file.py")
        x=j
        low = eval(left)
        if high<0 and low>0:
            if abs(low)<abs(high):
                u = j
                j = j
                du = du/10
                dj = dj/10
            if abs(high)<abs(low):
                u = u
                j = u
                du = du/10
                dj = dj/10
        if high>0 and low<0:
            if abs(low)<abs(high):
                u = j
                j = j
                du = du/10
                dj = dj/10
            if abs(high)<abs(low):
                u = u
                j = u
                du = du/10
                dj = dj/10
        #print("low: ", low)
        #print("high: ", high)
        #print(u, j)
        if abs(low)<.0000001:
            answer = round(j, 4)
            y = answer
            left = "(("+c+"-"+b+"*y**2)/"+a+")**.5"
            #st1 = parser.expr(left)
            #code1 = st1.compile("file.py")
            x = eval(left)
            x = round(x, 4)
            print("Point from (",point,") closest to hyperbola:\n(",x, " , ", y,")")
            #print("Y =", answer)
            answer = str(answer)
            answer = "Y = " + answer
            cont = 0 
            break
        
        if abs(high)<.0000001:
            answer = round(u, 4)
            y = answer
            left = "(("+c+"-"+b+"*y**2)/"+a+")**.5"
            #st1 = parser.expr(left)
            #code1 = st1.compile("file.py")
            x = eval(left)
            x = round(x, 4)
            print("Point from (",point,") closest to hyperbola:\n(",x, " , ", y,")")
            #print("Y =", answer)
            answer = str(answer)
            answer = "Y = " + answer
            cont = 0  
            break
        
        u = u+du
        j = j-dj
        -1*((7-(50)**(.5)))**(1/3)
        #((7+(50)**(.5))**(1/3)) + (-1*((7-(50)**(.5))))**(1/3))

        iterations+=1
        if iterations>100000:
            print("Error \n max iterations or no sign change. ")
            break
