# definition of variables
x = [100, 200]
y = [100, 250]
h = [False, True] # False=>infected
infected = 0 # count number of infected individuals
iteration = 0
peopleMoving = 2

def bargraph():
    global infected, x, iteration, peopleMoving
    line(0,500, 500, 500)
    healthy = len(x) - infected
    fill(255)
    rect(150, 520, 10*healthy, 20)
    fill(0)
    text("Healthy {}".format(healthy), 50, 530)
    text("Iteration No {}". format(iteration), 350, 530)
    text("People  Moving {}". format(peopleMoving), 350, 550)
    fill(255,0,0)
    rect(150, 550, 10*infected, 20)
    text("Infected {}".format(infected), 50, 560)


def setup():
   size(500,600)
   #create random individuals
   for n in range(20):
       x. append(random(0,500))
       y. append(random(0,500))
       h. append(True) #All healthy
       
def distance(x1, x2, y1, y2):
   a = (x1 - x2)
   b = (y1 - y2)
   c = sqrt(a**2 + b**2)
   return c
       
def draw():
   global x, y, infected, iteration, peopleMoving
   iteration += 1
   background(255)
   
   #number of infected
   infected = 0
   for i in range (len(h)):
       if h[i]== False:
           infected += 1
   bargraph() 
    
    #show the individuals
   for ind in range (len(x)):
       if h[ind] == True:
           fill(255) #healthy
       else:
           fill(255, 0, 0) #infected
           
       circle(x[ind], y[ind], 40)
       #calculate the distance to each neighbour
       for nei in range(len(x)):
           if nei == ind:
               continue
           d = distance(x[ind], x[nei], y[ind], y[nei])
           if d < 40 and (h[nei] == False or h[ind] == False):
                   # infection happens
                   h[ind] = False
                   h[nei] = False
   
   # move the  individuals
       for m in range(peopleMoving):
           # move randomly
           x[m] += random(-10, 10)
           y[m] += random(-10, 10)
       
           # bounderies conditions
           if x[m] > 500: x[m] = 500
           if x[m] < 0: x[m] = 0
           if y[m] < 0: y[m] = 0
           if y[m] > 500: y[m] = 500

   delay(100)
