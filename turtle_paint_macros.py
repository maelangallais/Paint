#Créé le 15 Mars 2023
from turtle import *
from ion import *
from random import *
from kandinsky import *
from time import *

def dessin():
  penup()
  for i in range(10):down()
  pendown()
  for i in range(12):right(),up()
  for i in range(6):up(),left()
  for i in range(1):left()
  for i in range(5):down(),left()
  for i in range(5):left(),up()
  for i in range(1):left()
  for i in range(6):left(),down()
  for i in range(12):down(),right()
  sleep(0.5)

def grille():
  penup(),goto(-160,110),pendown()
  for i in range(12):
    for i in range(32):right()
    down()
    for i in range(32):left()
    down()
  up()
  for i in range(17):
    for i in range(23):up()
    right()
    for i in range(23):down()
    right()
  sleep(0.5)

def rond():
  r=0
  d=10
  for i in range(160/d):
    r+=d
    penup(),goto(-r,0),pendown(),setheading(270),circle(r)
  sleep(0.5)

def up():setheading(90),forward(t)
def down():setheading(270),forward(t)
def right():setheading(0),forward(t)
def left():setheading(180),forward(t)

def go():
  a=5
  h=0
  fd(0)
  global t
  t=10
  while True:
    fill_rect(10,10,30,18,(255,255,255)),draw_string(str(a),10,10),fill_rect(10,30,30,18,(255,255,255)),draw_string(str(h),10,30),speed(0),pensize(a)
    if keydown (KEY_TOOLBOX):a-=1
    if keydown(KEY_BACKSPACE):a+=1
    if keydown (KEY_LEFTPARENTHESIS):a-=5
    if keydown(KEY_RIGHTPARENTHESIS):a+=5
    if keydown (KEY_MULTIPLICATION):a-=10
    if keydown(KEY_DIVISION):a+=10
    if a<=0:raise ValueError("La pinceau ne peut pas être inférieure à 1.")
    if keydown (KEY_TANGENT):h-=0.1
    if keydown(KEY_PI):h+=0.1
    if h<=-0.1:raise ValueError("La vitesse ne peut pas être inférieure à 0.")
    if keydown(KEY_UP):up()
    if keydown(KEY_DOWN):down()
    if keydown(KEY_RIGHT):right()
    if keydown(KEY_LEFT):left()
    if keydown(KEY_BACK):break
    if keydown(KEY_VAR):reset()
    if keydown(KEY_COMMA):showturtle()
    if keydown(KEY_POWER):hideturtle()
    if keydown(KEY_SHIFT):dessin()
    if keydown(KEY_ALPHA):grille()
    if keydown(KEY_XNT):rond()
    sleep(h)

go()
