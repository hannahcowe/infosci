#This is my Journal
 
 I created this program. 
 ```.py
offset = 50

def mouseClicked():
    global offset
    offset = offset + 1

def setup():
    size(500,500)
    background(255)
    
def draw():
    # line(x0yo,x1,y1)
    stroke(0) # black line
    y = 0
    for n in range(10):
        line(0,y, 500, y)
        y = y + 50
        
    fill(0)
    stroke(225) #white line
    
    y=0    
    for n in range(5):
        x = 0
        for n in range(5):
            square(x,y,50)
            x = x + 100
        y = y + 100
        
    # odd rows
    y=50 
    global offset 
    for n in range(5):
        x = 0 + offset
        for n in range(5):
            square(x,y,50)
            x = x + 100
        y = y + 100
         
```.py 

I learned how to make an optical illusion and program it to move.

I want to now how to make the whole background white as some of my sqaures turned grey as I moved it.

Homework 
1.create an optical illusion and make it move.





