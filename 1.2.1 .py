# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random 

#-----game configuration----
shape = "turtle"
size = 5
color = "purple"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
T = trtl.Turtle(shape=shape)
T.color(color)
T.shapesize(size)

scoreboard= trtl.Turtle()
scoreboard.penup()
scoreboard.goto(-270,270)
font = ("Arial", 60,"bold") 
scoreboard.write(score,font=font)
scoreboard.ht()
counter =  trtl.Turtle()
counter.goto(270,-270)
#-----game functions--------
def turtle_clicked(x,y):
    print("T was clicked")
    change_position()
    score_counter()

def change_position():
    T.penup()
    T.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-400,400)
    T.goto(new_xpos,new_ypos)
    T.st()

def score_counter():
    global score
    score += 1
    print (score)
    scoreboard.clear()
    scoreboard.write(score,font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(0,0)
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_over():
    T.ht()
    T.goto(520,500)

#-----events----------------
T.onclick(turtle_clicked)

wn=trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()