import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
background=pygame.Surface(screen.get_size())
background.fill((255,0,0))
background.convert()
screen.blit(background,(0,0))
player=pygame.image.load('spaceship.png')
screen.blit(player,(100,300))
mainloop=True
n=2
dx=dy=bombs=problem1=problem2=bomby1=bomby2=shot1=shot2=shot1y=shot2y=shot1x=shot2x=m=p=0
c=d=1
maxshot=1
alx1=5
pos1=10
pos2=400
alx2=-5
clock=pygame.time.Clock()
while mainloop:
	bki=pygame.image.load("backgroundSpace1.jpg")
	screen.blit(bki,(0,0))

	
	x1=random.randint(1,160)
	x2=random.randint(1,160)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			mainloop=False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				n=0
			if event.key==pygame.K_RIGHT:
				n=1
			if event.key==pygame.K_ESCAPE:
				mainloop=False
			if event.key==pygame.K_UP:
				m=1
				p=1
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				n=2
	if(5*x1 == pos1 and problem1==0): # drop the bomb from the spaceship
		#bombs=1
		bombx1=5*x1                #bomb x-coordinate
		problem1=1                 #this is done so that bomb fall once until the previous one does not reaches down
	if(problem1==1):
		bomb1=pygame.image.load("bomb.gif")
		screen.blit(bomb1,(bombx1+5,10+bomby1+10))
		bomby1+=5
	if bomby1==450:
		problem1=0
		bomby1=0

	if(5*x2 == pos2 and problem2==0):
		bombx2=5*x2
		problem2=1
	if(problem2==1):
		bomb2=pygame.image.load("bomb.gif")
		screen.blit(bomb2,(bombx2+5,10+bomby2+10))
		bomby2+=5
	if(bomby2==450):
		bomby2=0
		problem2=0
	if(n==1):
		dx=dx+4
		

	elif(n==0):
		dx=dx-4

	elif(n==2):
		dx=dx+0
	if pos1>780 or pos1< 5:
		alx1*= -1
	pos1=pos1+alx1
	if pos2>780 or pos2<5:
		alx2*= -1
	pos2=pos2+alx2
	if(m==1 and maxshot==1):
		shot1=1
		shot1x=100+dx
		#c=0
		maxshot+=1
		m=0
	if(shot1==1):
		shot1y=shot1y-10
		shoti1=pygame.image.load("shot.gif")
		screen.blit(shoti1,(shot1x+22,400+shot1y))
	if(400+shot1y<=40):
		m=0
		#c=1
		maxshot-=1
		shot1=0
		shot1y=0
	
	if(m==1 and maxshot==2):
		shot2=1
		shot2x=100+dx
		#d=0
		#p=0
		m=0
		maxshot+=1
	if(shot2==1):
		shot2y=shot2y-10
		shoti2=pygame.image.load("shot.gif")
		screen.blit(shoti2,(shot2x+22,400+shot2y))
	if(400+shot2y<=40):
		#d=1
		#p=0
		shot2=0
		shot2y=0
		maxshot-=1
		m=0
	
	#if(((shot1x>pos1 and shot1x<pos+80) and (400+shot1y>0 and 400+shot1y<80) or ((shot2x>pos2 and shot2x<pos2+80) and (400+shot2y>0) and 400 + shot2y<80))):
		
	alien1=pygame.image.load("alien.png")
	screen.blit(alien1,(pos1,10))
	alien2=pygame.image.load("alien.png")
	screen.blit(alien2,(pos2,10))
	player=pygame.image.load('spaceship1.png')
	screen.blit(player,(100+dx,400+dy))
	print(p)
	pygame.display.flip()
