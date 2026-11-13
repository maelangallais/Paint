#Créé le 18 Novembre 2023
from kandinsky import fill_rect,get_pixel,draw_string
from ion import keydown
from time import sleep,monotonic

new,toggle=True,True
show,fill=False,False

m=3
a,p=m,5
w,wa=6*m,m
bw=w
sw,sh=320%m,222%m
x,y=160+sw//2-w//2,111+sh//2-w//2
px,py=x,y
Rgb,rGb,rgB=255,0,0
c,cp=(Rgb,rGb,rgB),(255,)*3
t,tp=monotonic(),0.5

interface=(255,182,57)
fill_rect(0,0,320,sh,interface)
fill_rect(0,0,sw,222,interface)
dessin=[[(255,)*3]*(320//m) for i in range(222//m)]
s_fill=[[0,1],[1,0],[1,1],[1,2],[2,1]]
dir=[[1,0],[0,1],[-1,0],[0,-1]]

def search(x,y,c):
 cl=dessin[y//m][x//m]
 if c==cl:return
 dessin[y//m][x//m]=c
 buffer=[[x,y]]
 while buffer:
  cx,cy=buffer[0][0],buffer[0][1]
  for dx,dy in dir:
   nx,ny=cx+dx*m,cy+dy*m
   if sw<=nx<=320-m and sh<=ny<=222-m and dessin[ny//m][nx//m]==cl:
    dessin[ny//m][nx//m]=c
    fill_rect(nx,ny,m,m,c)
    buffer.append([nx,ny])
  buffer.remove([cx,cy])

def draw(x,y,c):
  if fill:
    x,y=x-m,y-m
    for dx,dy in s_fill:
      if 0<=x+dx*m<=320-m and 0<=y+dy*m<=222-m:
        fill_rect(x+dx*m,y+dy*m,m,m,c)
  else:fill_rect(x,y,w,w,c)

while True:
  if new:
#mov utilise pour les mouvements en diagonale
    new,mov=False,0
#Redessiner les zones derriere le passage
    for yd in range(w//m):
      for xd in range(w//m):
        fill_rect(px+xd*m,py+yd*m,m,m,dessin[yd+py//m][xd+px//m])
    if fill:
      for yd in range(m):
        for xd in range(m):
          if 0<=px-m+xd*m<=320-m and 0<=py-m+yd*m<=222-m:
            fill_rect(px-m+xd*m,py-m+yd*m,m,m,dessin[yd+py//m-1][xd+px//m-1])
#Dessiner le carre de selection
    draw(x,y,c)
#Redefinir le temps d'attente du toggle
    toggle,tp=False,1
#Actualisation des couleurs
    c=Rgb,rGb,rgB
#Temps d'attente
#    sleep(0.1)

#Clignotement du carre
  if monotonic()-t>=tp:
    tp=0.5
    if toggle:
      toggle,t=False,monotonic()
      draw(x,y,(255-Rgb,255-rGb,255-rgB))
    else:
      toggle,t=True,monotonic()
      draw(x,y,c)
#Affichage du RGB
  if show:draw_string(str(Rgb)+", "+str(rGb)+", "+str(rgB),sw,0)

  if keydown(45)and w<222 and x+w<320 and y+w<222 and fill==False:w,new=w+wa,True
  elif keydown(46)and w>wa and fill==False:
    for yd in range(w//m):
      for xd in range(w//m):
        fill_rect(x+xd*m,y+yd*m,m,m,dessin[yd+y//m][xd+x//m])
    w,new=w-wa,True
  if keydown(1) and y-a>=0:px,py,y,new,mov=x,y,y-a,True,1
  elif keydown(2) and y+a+w<=222:px,py,y,new,mov=x,y,y+a,True,1
  if keydown(0) and x-a>=0:px,py,x,new=x,y if mov==0 else py,x-a,True
  elif keydown(3) and x+a+w<=320:px,py,x,new=x,y if mov==0 else py,x+a,True
  if keydown(4):
    if fill:search(x,y,c)
    else:
      new=True
      for ym in range(w//m):
        for xn in range(w//m):
          if dessin[y//m+ym][x//m+xn]!=c:
            dessin[y//m+ym][x//m+xn]=c
  if keydown(16)and Rgb>0:Rgb,new=Rgb-p,True
  elif keydown(17)and Rgb<255:Rgb,new=Rgb+p,True
  if keydown(22)and rGb>0:rGb,new=rGb-p,True
  elif keydown(23)and rGb<255:rGb,new=rGb+p,True
  if keydown(28)and rgB>0:rgB,new=rgB-p,True
  elif keydown(29)and rgB<255:rgB,new=rgB+p,True
  if keydown(15):
    c=dessin[y//m][x//m]
    col,si=["","",""],0
    for i in str(c):
      if i!="(" and i!=")":
        if i==",":si+=1
        else:col[si]+=i
    Rgb,rGb,rgB=int(col[0]),int(col[1]),int(col[2])
    new=True
  if keydown(12):
    if show:
      show=False
      for yd in range(18//m):
        for xd in range(130//m):
          fill_rect(xd*m+sw,yd*m,m,m,dessin[yd][xd])
    else:show=True
    sleep(0.2)
  if keydown(13):
    if fill:
      fill=False
      for cx,cy in[[px,py],[x,y]]:
        for dx,dy in s_fill:
          if 0<=cx-m+dx*m<=320-m and 0<=cy-m+dy*m<=222-m:
            fill_rect(cx-m+dx*m,cy-m+dy*m,m,m,dessin[dy+cy//m-1][dx+cx//m-1])
      w=bw
      x,y=min(max(x,sw),320-w),min(max(y,sh),222-w)
      px,py=x,y
    else:
      fill=True
      for yd in range(w//m):
        for xd in range(w//m):
          fill_rect(x+xd*m,y+yd*m,m,m,dessin[yd+y//m][xd+x//m])
          fill_rect(px+xd*m,py+yd*m,m,m,dessin[yd+py//m][xd+px//m])
      bw,w=w,3
    new=True
    sleep(0.2)
