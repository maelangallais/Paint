#Créé le 31 Mars 2023
from turtle import *
from ion import *
from random import *
from time import *

def up():setheading(90),forward(t)
def down():setheading(270),forward(t)
def right():setheading(0),forward(t)
def left():setheading(180),forward(t)

a=5
h=5
c='black'
fd(0)
global t
t=10
while True:
  speed(h),pensize(a),color(c)
  if keydown(KEY_TOOLBOX):a-=1
  if keydown(KEY_BACKSPACE):a+=1
  if keydown(KEY_COMMA):a-=5
  if keydown(KEY_POWER):a+=5
  if keydown(KEY_SQRT):a-=10
  if keydown(KEY_SQUARE):a+=10
  if a<=0:raise ValueError("La pinceau ne peut pas être inférieure à 1.")
  if keydown (KEY_LEFTPARENTHESIS):h-=1
  if keydown(KEY_RIGHTPARENTHESIS):h+=1
  if h<=-0.1:raise ValueError("La vitesse ne peut pas être inférieure à 0.")
  if keydown(KEY_UP):up()
  if keydown(KEY_DOWN):down()
  if keydown(KEY_RIGHT):right()
  if keydown(KEY_LEFT):left()
  if keydown(KEY_BACK):break
  if keydown(KEY_VAR):reset()
  if keydown(KEY_ZERO):c='white'
  if keydown(KEY_DOT):c='black'
  if keydown(KEY_ONE):c='red'
  if keydown(KEY_TWO):c='green'
  if keydown(KEY_THREE):c='blue'
  if keydown(KEY_FOUR):c='orange'
  if keydown(KEY_FIVE):c='pink'
  if keydown(KEY_SIX):c='purple'
  if keydown(KEY_SEVEN):c='yellow'
  if keydown(KEY_EIGHT):c='brown'
  if keydown(KEY_NINE):c='gray'
