import pgzrun
import random
import time
TITLE="APPLE CATCHER"
WIDTH=500
HIEGHT=400
apple=Actor('apple')
basket=Actor('basket')
basket.x=250
basket.y=350
collected=0
missed=0

def draw():
    screen.blit('applegamebg',(0,0))
    apple.draw()
    basket.draw()
    screen.draw.text("Apples Collected: "+str(collected),color="black",topleft=(20,10))
    screen.draw.text("Apples Missed: "+str(missed),color="black",topright=(480,10))
    
    if missed>collected/10:
        screen.clear()
        apple.y=-9999999999
        screen.fill("red")
        screen.draw.text("YOU LOSE",color="black",center=(250,250))
        screen.draw.text("(DONT MISS MORE APPLES THAN YOU CATCH)",color="black",center=(250,270))
        screen.draw.text("Apples Collected: "+str(collected),color="black",topleft=(20,10))
        screen.draw.text("Apples Missed: "+str(missed),color="black",topright=(480,10))
        screen.draw.text("Final Score: "+str(collected-missed),color="black",center=(250,290))
    

def place_apple():
    apple.y=70
    apple.x=random.randint(85,405)


def update():
    global collected
    global missed
    apple.y=apple.y+(1+(collected/10))
    if keyboard.left:
        basket.x=basket.x-2
    if keyboard.right:
        basket.x=basket.x+2
    apple_caught=basket.colliderect(apple)
    
    if apple_caught:
        collected=collected+1
        place_apple()
    if apple.y>500:
        place_apple()
        missed=missed+1

    
pgzrun.go()

