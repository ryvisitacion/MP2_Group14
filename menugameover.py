import pyglet
from pyglet.window import mouse
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

def compareHighScores(score):
	highscore = []
	file_stream = open("highscore.txt", 'r')
	for line in file_stream:
		highscore.append(int(line.strip()))
	file_stream.close()

	highscore.append(score)
	highscore = sorted(highscore, reverse=True)
	highscore = highscore[:-1]

	
	
	i=0
	while i<5:
		highscore[i] = str(highscore[i])+"\n"
		i+=1

	file_stream = open("highscore.txt", 'w')
	file_stream.writelines(highscore)
	file_stream.close()
	
def gameOverScreen(score):
	compareHighScores(score)
	window = pyglet.window.Window(width = 1200, height = 900)
	gameover_label = pyglet.text.Label('GAME OVER',
		font_name ='Times New Roman',
		font_size = 80,
		x = window.width//2, y = 3 * window.height//4,
		anchor_x ='center', anchor_y = 'top')
	scoreLabel = pyglet.text.Label('SCORE: {}'.format(score),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y = 2.5 * window.height//4,
		anchor_x ='center', anchor_y = 'top')

	global mainMenu
	mainMenu = pyglet.resource.image('mainMenu.png')
	mainMenuSprite = pyglet.sprite.Sprite(mainMenu)
	mainMenuP = pyglet.resource.image('mainMenuP.png') 
	mainMenuPSprite = pyglet.sprite.Sprite(mainMenuP)

	gameOverButtons = [mainMenuSprite, mainMenuPSprite]
	
	for buttons in gameOverButtons:
		buttons.position = (window.width//2.5, window.height//3)
		global a, b
		a, b = buttons.position

	def cursorCheck(x, y):
		if (a < x < a + mainMenu.width) and (b < y < b + mainMenu.height):
			return True
		return False
	
	@window.event()
	def on_draw():
		gameover_label.draw()
		scoreLabel.draw()

	@window.event()
	def on_mouse_motion(x, y, button, modifiers):
		if not cursorCheck(x, y):
			mainMenuSprite.draw()

	@window.event()
	def on_mouse_press(x, y, button, modifiers):
		if cursorCheck(x, y):
			mainMenuPSprite.draw()

	@window.event()
	def on_mouse_release(x, y, button, modifiers):
		if cursorCheck(x, y):
			window.close()
			mainMenuSprite.draw()
			mainMenuScreen()
	pyglet.app.run()
	
def highScoreScreen():
	highscore = []
	file_stream = open("highscore.txt", 'r')
	for line in file_stream:
		highscore.append(int(line.strip()))
	file_stream.close()
	window = pyglet.window.Window(width = 1200, height = 900)
	
	mainMenu = pyglet.resource.image('mainMenu.png')
	mainMenuSprite = pyglet.sprite.Sprite(mainMenu)
	mainMenuP = pyglet.resource.image('mainMenuP.png') 
	mainMenuPSprite = pyglet.sprite.Sprite(mainMenuP)
	
	gameOverButtons = [mainMenuSprite, mainMenuPSprite]
	
	
	highScore_label = pyglet.text.Label('HIGH SCORES',
		font_name ='Times New Roman',
		font_size = 80,
		x = window.width//2, y = 9 * window.height//10,
		anchor_x ='center', anchor_y = 'top')
	
	highScore1_label = pyglet.text.Label(str(highscore[0]),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y =  650,
		anchor_x ='center', anchor_y = 'top')
		
	highScore2_label = pyglet.text.Label(str(highscore[1]),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y =  590,
		anchor_x ='center', anchor_y = 'top')
		
	highScore3_label = pyglet.text.Label(str(highscore[2]),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y =  540,
		anchor_x ='center', anchor_y = 'top')
		
	highScore4_label = pyglet.text.Label(str(highscore[3]),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y =  480,
		anchor_x ='center', anchor_y = 'top')

	highScore5_label = pyglet.text.Label(str(highscore[4]),
		font_name ='Times New Roman',
		font_size = 40,
		x = window.width//2, y =  420,
		anchor_x ='center', anchor_y = 'top')
		
	for buttons in gameOverButtons:
		buttons.position = (window.width//2.5, 250)
		global a, b
		a, b = buttons.position

	def cursorCheck(x, y):
		if (a < x < a + mainMenu.width) and (b < y < b + mainMenu.height):
			return True
		return False
	
	@window.event()
	def on_draw():
		highScore_label.draw()
		if highScore1_label.text != "0":
			highScore1_label.draw()
		if highScore2_label.text != "0":
			highScore2_label.draw()
		if highScore3_label.text != "0":
			highScore3_label.draw()
		if highScore4_label.text != "0":
			highScore4_label.draw()
		if highScore5_label.text != "0":
			highScore5_label.draw()
		
	@window.event()
	def on_mouse_motion(x, y, button, modifiers):
		if not cursorCheck(x, y):
			mainMenuSprite.draw()

	@window.event()
	def on_mouse_press(x, y, button, modifiers):
		if cursorCheck(x, y):
			mainMenuPSprite.draw()

	@window.event()
	def on_mouse_release(x, y, button, modifiers):
		if cursorCheck(x, y):
			window.close()
			mainMenuSprite.draw()
			mainMenuScreen()
			
	
	pyglet.app.run()
	
def mainMenuScreen():
	window = pyglet.window.Window(width = 1200, height = 900)
	title_label = pyglet.text.Label('DROP',
		font_name ='Times New Roman',
		font_size = 80,
		x = window.width//2, y = 9 * window.height//10,
		anchor_x ='center', anchor_y = 'top')

	mainMenuStr = ['newGame', 'newGameP', 'highScore', 'highScoreP', 'exitGame', 'exitGameP']
	mainMenuButtons = []

	for strings in mainMenuStr:
		loadImageButton = pyglet.resource.image(strings + '.png')
		imageButton = pyglet.sprite.Sprite(loadImageButton)
		mainMenuButtons.append(imageButton)

	buttonPositions = []	
	for i in range(len(mainMenuButtons)):
		if i % 2 == 0:
			if i > 0:
				mainMenuButtons[i].position = (window.width//3, mainMenuButtons[i-1].position[1] - mainMenuButtons[i].height)
			else:
				mainMenuButtons[i].position = (window.width//3, window.height//2)
		else:
			mainMenuButtons[i].position = mainMenuButtons[i-1].position
		buttonPositions.append(mainMenuButtons[i].position)

	def cursorCheckMenu(x, y, i):
		if ((buttonPositions[i][0]) < x < buttonPositions[i][0] + mainMenuButtons[i].width) and (buttonPositions[i][1] < y < buttonPositions[i][1] + mainMenuButtons[i].height):
			return True
		return False		

	@window.event()
	def on_draw():
		title_label.draw()

	@window.event()
	def on_mouse_motion(x, y, button, modifiers):
		for i in range(0, len(mainMenuButtons), 2):
			if not cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()

	@window.event()
	def on_mouse_press(x, y, button, modifiers):
		for i in range(1, len(mainMenuButtons), 2):
			if cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()

	@window.event()
	def on_mouse_release(x, y, button, modifiers):
		for i in range(0, len(mainMenuButtons), 2):
			if cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()
				if i == 0:
					window.close()
					import gui
				if i == 2:
					window.close()
					highScoreScreen()
				if i == 4:
					exit()
	pyglet.app.run()


