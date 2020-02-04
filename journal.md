#This is my Journal
 
 I created this program. 
 ```.py
 x = 0

def setup():
    size(1000, 1000)
    background(255)
    textAlign(CENTER, CENTER)

def draw():
    print("")
    
def mouseClicked():
    x = mouseX
    y = mouseY
    r = random (1, 100)
    myred = random(0, 255)
    myblue = random(0, 255)
    mygreen = random(0, 255)
    fill(myred, myblue, mygreen)
    circle(x, y, r)  
    fill(0)
    textSize(r/3);
    text("HAC", x, y)

    print (x, y)
```.py 

I learned basic commands regarding circles in Pyhton. I also learned the functions size, set up background, textAlign, draw, print, MouseClicked, functions regarding colors, circle, fill textSize, and text.

I have no questions.

Homework 
1. Add lines from middle of the window to the middle of circle
2. Add lines from circle to circle
