#This is my Journal
 
 I created this program. 
 ```.py
def setup():
    size(600,600)
    background(225)
    strokeWeight(10)
    
def draw():
    stroke(0)
    
def mouseClicked():
    stroke (0)
    rect(100, 100, 400, 400, 50)
    stroke(225, 0, 0,) #red, geen, blue
    n = random(0,6)
    
    if 0<=n<1:
        # number one 
        circle(300, 300, 50)
    if 1<=n<2:
        # number two
        circle (200, 200, 50) 
        circle (400, 400, 50) 
    if 2<=n<3:
        # number 3
        circle (200, 200, 50) 
        circle (400, 400, 50)
        circle (300, 300, 50) 
    if 3<=n<4:
        # number 4
        circle (200, 200, 50)
        circle (200, 400, 50)
        circle (400, 400, 50) 
        circle (400, 200, 50)
    if 4<=n<6:
         # number 5
        circle (200, 200, 50)
        circle (200, 400, 50)
        circle (400, 400, 50) 
        circle (400, 200, 50)
        circle (300, 300, 50) 
    if 6<=n<7:
        # number 6
        circle (200, 200, 50)
        circle (200, 400, 50)
        circle (400, 400, 50) 
        circle (400, 200, 50)
        circle (200, 300, 50)
        circle (400, 300, 50) 
```.py 

I learned how to make a dye and make it randomly go to a number.

I have no questions.

Homework 
1.create the number of time a number was rolled with a rectangle





