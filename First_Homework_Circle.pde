```
def setup():
      size(500,500)
      background(255)
      textAlign(CENTER,CENTER)

def draw():
      print("")


def mouseClicked():
      x=mouseX
      y=mouseY
      r=random(0,100)
      myr=random(0,255)
      myg=random(0,255)
      myb=random(0,255)

      fill(myr,myg,myb)
      circle(x,y,r)

      fill(0)
      textSize(r/5)
      text("HAC",x,y)

      line(x,y,250,250)
      ```
