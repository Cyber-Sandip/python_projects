# love symbol with sound 
import turtle 
from playsound import playsound
from turtle import *

wn = Screen()
wn.bgcolor('black')
t = turtle. Turtle()
t.pencolor('white')
def curve():

       for i in range (200):

             t.rt(1)

             t.fd(1)

t.speed(100)       

def heart():

       t.fillcolor('red')

       t.begin_fill()

       t.lt (140)

       t.fd (113)

       curve () 

       t.lt (120)

       curve() 

       t.fd(112)

       t.end_fill()
heart()
t.ht()

def write(message,pos):

       x,y=pos

       t.penup()

       t.goto(x,y)

       t.color('white')

       style=("Stencil Std", 18, "italic")

       t.write(message, font=style)

playsound (r"path of your song path")

write('I',(-68,95))

write('L',(-55,95))

write('0',(-42,95))

write('V',(-30,95))

write('E',(-14,95))

write('Y', (10,95))

write('0', (26,95))

write('U', (45,95))

write('A',(-60,70))

write('r',(-42,70))

write('p',(-32,70))

write('i',(-18,70))

write('t',(-10,70))

write('a',(-2,70))

wn.mainloop()