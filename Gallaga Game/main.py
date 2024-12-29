from random import randint
import pgzrun
WIDTH=600
HEIGHT=800
TITLE='Gallaga Game'

bugs=[]
bullets=[]

Castle=Actor('space_ship')
Castle.x=300
Castle.y=750

def bugfunc():
    for j in range(5):
        for i in range(5):
            Bug=Actor('bug')
            Bug.x=100+i*100
            Bug.y=100+j*50
            bugs.append(Bug)
    


    



def draw():
    screen.fill('Purple')
    Castle.draw()
    for x in bugs:
        x.draw()
    for z in bullets:
        z.draw()



def update():
    if keyboard.left:
        Castle.x=Castle.x-10
    if keyboard.right:
        Castle.x=Castle.x+10
    
    for z in bullets:
        z.y=z.y-10

def on_key_down(key):
    global bullets
    if key==keys.UP:
        Bullet=Actor('bullet')
        Bullet.x=Castle.x
        Bullet.y=Castle.y
        bullets.append(Bullet)

bugfunc()
pgzrun.go()
