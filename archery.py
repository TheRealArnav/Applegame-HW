import pgzrun
import random
import time

TITLE="Archery"
WIDTH=500
HEIGHT=500
shot="not shot"

arrow=Actor('arrow')
arrow.x=250
arrow.y=380
shot_board=Actor('bullseye')
shot_board.x=500
shot_board.y=40
crossbow_loaded=Actor('loaded_bow')
crossbow_loaded.x=250
crossbow_loaded.y=380
unloaded_crossbow=Actor('unloaded_bow')
unloaded_crossbow.x=250
unloaded_crossbow.y=380

def draw():
    global play
    screen.blit('sky',(0,0))
    #screen.fill('red')
    arrow.draw()
    shot_board.draw()
    crossbow_loaded.draw()
    unloaded_crossbow.draw()
    screen.draw.text("Shot Status: "+str(shot),color='black',topleft=(20,20))


    

def on_mouse_down(pos):
    global shot
    if crossbow_loaded.collidepoint(pos):
        crossbow_loaded.x=600
        crossbow_loaded.y=600
        arrow.x=250
        arrow.y=100
    hit=arrow.colliderect(shot_board)
    if hit:
        shot_board.x=600
        shot_board.y=600
        shot="SHOT HIT! (restart to play again)"
        screen.clear()
    else:
        shot="Shot Missed (restart to play again)"

def update():
    shot_board.x=shot_board.x-5
    if shot_board.x<20:
        for i in range(10):
            time.sleep(0.001)
            shot_board.x=500
            









pgzrun.go()