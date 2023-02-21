import pygame, random
pygame.init()

displayWidth = 600
displayHight = 600
display = pygame.display.set_mode((displayWidth, displayHight))
pygame.display.set_caption("Первая игра")

white = ( 255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)
Yellow = (255,255,0)
black = (0,0,0)

bodyImg = pygame.image.load("img/body.png")
foodYellowImg = pygame.image.load("img/Yellow.jpg")
foodFioletImg = pygame.image.load("img/Fiolet.jpg")
foodRedImg = pygame.image.load("img/Red.jpg")
errorImg = pygame.image.load("img/rock.png")
snakeBlock = 50
snakeX = displayWidth / 2
snakeY = displayHight / 2
snakeChangeX = 0
snakeChangeY = 0
snakeSpeed = 5

snakeList = []
leghtSnake = 1
foodErrorX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
foodErrorY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
foodYellowX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
foodYellowY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
foodBlueX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
foodBlueY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
foodX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
foodY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock

score = pygame.font.SysFont("Calibri", 25)
gameOver = False

clock = pygame.time.Clock()
def showScore(scr):
	temp = score.render("Score:" + str(scr), True, black)
	display.blit(temp,[50,50])
def drawSnake (snakeBlock,snakeList):
	for i in snakeList:
		# pygame.draw.rect(dislay, green, [i[0], i[1], snakeBlock, snakeBlock])
		display.blit(bodyImg,[i[0], i[1], snakeBlock, snakeBlock])
while not gameOver:
	showScore(leghtSnake - 1)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				snakeChangeX = 0
				snakeChangeY = -snakeBlock
			elif event.key == pygame.K_s:
				snakeChangeX = 0
				snakeChangeY = snakeBlock
			elif event.key == pygame.K_a:
				snakeChangeX = -snakeBlock
				snakeChangeY = 0
			elif event.key == pygame.K_d:
				snakeChangeX = snakeBlock
				snakeChangeY = 0
	if snakeX >= displayWidth or snakeX < 0 or snakeY >= displayHight or snakeY < 0:
		gameOver = True
	display.fill(white)
	snakeX += snakeChangeX
	snakeY += snakeChangeY
	snakeHead = []
	snakeHead.append(snakeX)
	snakeHead.append(snakeY)
	snakeList.append(snakeHead)
	if len(snakeList) > leghtSnake:
		del snakeList[0]
	for i in snakeList[:-1]:
		if i == snakeHead:
			gameOver = True
	drawSnake (snakeBlock,snakeList)

	display.blit(errorImg, [foodErrorX, foodErrorY, snakeBlock, snakeBlock])
	pygame.display.update()
	display.blit(foodYellowImg, [foodX, foodY, snakeBlock, snakeBlock])
	pygame.display.update()
	display.blit(foodRedImg, [foodBlueX, foodBlueY, snakeBlock, snakeBlock])
	pygame.display.update()
	display.blit(foodFioletImg,[foodYellowX, foodYellowY, snakeBlock, snakeBlock])
	pygame.display.update()
	if snakeX == foodErrorX and snakeY == foodErrorY:
		foodErrorX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
		foodErrorY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
		leghtSnake -= 1
		snakeList[:-1]
		if leghtSnake == 0:
			gameOver = True
	if snakeX == foodX and snakeY == foodY:
		foodX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
		foodY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
		leghtSnake += 1
	if snakeX == foodBlueX and snakeY == foodBlueY:
		foodBlueX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
		foodBlueY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
		leghtSnake += 1
	if snakeX == foodYellowX and snakeY == foodYellowY:
		foodYellowX = round(random.randrange(0, displayWidth - snakeBlock) / snakeBlock) * snakeBlock
		foodYellowY = round(random.randrange(0, displayHight - snakeBlock) / snakeBlock) * snakeBlock
		leghtSnake += 1
	clock.tick(snakeSpeed)