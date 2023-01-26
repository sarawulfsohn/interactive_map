#"I hereby certify that this program is solely the result of my own work and is
# in compliance with the Academic Integrity policy of the course syllabus and 
# the academic integrity policy of the CS department.”

# In order to run this program correctly, make sure its saved on the same folder
# as your Draw.py, and with the files from the compressed zip folder 

import Draw
import time
import random
import math

# list of clouds with [image, x cooordinate, y coordinate, speed, width]
clouds= [["cloud1.gif", 0,    60,  0.3, 113],[ "cloud2.gif", 0,   200, -0.5, 165], 
         ["cloud3.gif", 1009, 300, 0.6, 138],["cloud4.gif",  1009,400, -0.2, 77],
         ["cloud5.gif", 1009, 500, -0.5,131],["cloud6.gif",  0,   10,   0.1, 130]]


#list of birds [image, x coordinate, y coordinate, speed, width]
birds= [["bird1RIGHT.gif", 0,    65,  0.8, 24], ["bird2RIGHT.gif", 0,    240, 0.8,  37],
        ["bird3RIGHT.gif", 1009, 200, 1,   34], ["bird1LEFT.gif",  1009, 460, -0.9, 31],
        ["bird2LEFT.gif",  1009, 700, -0.6,52], ["bird3LEFT.gif",  1009, 200, -1,   54]]

#list of boats [boat image day right, boat image night right, x coordinate, y coordinate, speed, boat image day left, boat image night left, w, h, status]
# True = direction to the right
# False= direction to the left
boats = [ ["boat1.gif","boat1Night.gif", 40, 2,   0.4,  "boat1Left.gif", "boat1NightLeft.gif", 37, 45, True ], 
	  ["boat2.gif","boat2Night.gif", 177,120, -0.3, "boat2Left.gif", "boat2NightLeft.gif", 22, 35, True] ]

# list for time of the day, to keep track of button status [image of sun, image of moon, status]
button = ["sun.gif", "moon.gif", True]  

#keep track if info button is pressed ([image, status])
info = ["info.gif", True]
            
   
#list of people [image, x, y, w, h, state, text, x(textbox), y(textbox), w(textbox), h(textbox)]
people = [["EmberaWoman.gif",  760, 380, 51, 110, False, "mậe sakabuma! Hello, how are you?\
	   \nMy name is Anahi and I am part \nof the Emberá-Wounaan tribe. We \
	   \ntake great pride in our crafts \nand taking care of our environment, \
	   \nand we hope you too take the \ninitiative to care for our world!", 690, 250,195, 120], 
	  
          ["MenTipico.gif", 865, 170, 43, 109 , False, 'Hola! I hope you are having a \
	  \ngreat time visiting Casco Antiguo! \nBehind me is the Municipal \nPalace, house to many historical \
	  \nevents in our country, such as \nthe Declaration of Independence \nfrom Colombia in 1903, and where \
	  \nour national anthem and flag \nwere adopted that same year.', 792, 15,190, 150],
	  
	  ["molas.gif",180, 300, 39, 110, False, "Hi! My name is Malén, and I'm part \
	  \nof the Kuna tribe. The women of my \ncommunity are well known for the \
	  \nconfection of beautiful hand-stitched \nMolas. These are a combination \
	  \nof the ancestral and modern world, a \nway for us to conserve our customs, \
	  \nand part of our traditional clothing.", 100, 160, 200,136],
	  
	  ["Roman.gif",550, 200, 47, 108, False, "Hey! This is Román Torres, \
	  \nI'm a player for Panama’s national \nsoccer team, Marea Roja. In 2018,\
	  \nI scored the goal that classified \nmy country to compete in the \
	  \nRussian FIFA World Cup.",  480, 95, 185,100]]


#list of trees [imageDay, imageNight, x coordinate, y coordinate]
trees =[["palmTree1.gif", "palmTree1Night.gif",  285, 47],
	["pinkTree1.gif", "pinkTree1Night.gif",  951, 508],
	["pinkTree2.gif", "pinkTree2Night.gif",  11,  249],
	["tree1.gif",     "tree1Night.gif",      0,   468],
	["tree2.gif",     "tree2Night.gif",      985, 6],
	["yellowTree.gif","yellowTreeNight.gif", 660, 115],
	["palmTree2.gif", "palmTree2Night.gif",  775, 428]]

#list of windowLocations [x, y, w, h, time remaining, status]
#to be used for blinkWindows
windows= [ [380, 210, 10, 20, random.randint(2,10), False], #windows yellow building 
           [380, 240, 10, 20, random.randint(2,10), False], 
           [380, 270, 10, 20, random.randint(2,10), False], 
           [380, 300, 10, 20, random.randint(2,10), False], 
           [400, 210, 10, 20, random.randint(2,10), False],
           [400, 240, 10, 20, random.randint(2,10), False],
           [400, 270, 10, 20, random.randint(2,10), False], 
           [400, 300, 10, 20, random.randint(2,10), False], 
           [420, 210, 10, 20, random.randint(2,10), False], 
           [420, 240, 10, 20, random.randint(2,10), False], 
           [420, 270, 10, 20, random.randint(2,10), False], 
           [420, 300, 10, 20, random.randint(2,10), False], 
           [110, 260, 20, 30, random.randint(2,10), False],#windows red building 
           [140, 260, 20, 30, random.randint(2,10), False], 
           [170, 260, 20, 30, random.randint(2,10), False],
           [200, 260, 20, 30, random.randint(2,10), False], 
           [790, 110, 15, 30, random.randint(2,10), False],#windows Municipal Palace
           [815, 110, 15, 30, random.randint(2,10), False], 
           [910, 110, 15, 30, random.randint(2,10), False],
           [935, 110, 15, 30, random.randint(2,10), False], 
           [790, 70,  15, 20, random.randint(2,10), False],
           [815, 70,  15, 20, random.randint(2,10), False], 
           [910, 70,  15, 20, random.randint(2,10), False], 
           [935, 70,  15, 20, random.randint(2,10), False], 
           [880, 490, 15, 30, random.randint(2,10), False], #windows grey building 
           [910, 490, 15, 30, random.randint(2,10), False], 
           [940, 490, 15, 30, random.randint(2,10), False], 
           [970, 490, 15, 30, random.randint(2,10), False]] 

# list of arch locations[x, y, w, h, time remaining, status]
#to be used for blinkWindows
arches =  [[230, 290, 20, 20, random.randint(2,10), False], # blue building
           [260, 290, 20, 20, random.randint(2,10), False], 
           [290, 290, 20, 20, random.randint(2,10), False], 
           [320, 290, 20, 20, random.randint(2,10), False], 
           [350, 290, 20, 20, random.randint(2,10), False],  
           [230, 330, 20, 20, random.randint(2,10), False],
           [260, 330, 20, 20, random.randint(2,10), False], 
           [290, 330, 20, 20, random.randint(2,10), False], 
           [320, 330, 20, 20, random.randint(2,10), False], 
           [350, 330, 20, 20, random.randint(2,10), False],
           [390, 500, 20, 30, random.randint(2,10), False], # Museum of the Canal
           [420, 500, 20, 30, random.randint(2,10), False], 
           [450, 500, 20, 30, random.randint(2,10), False], 
           [480, 500, 20, 30, random.randint(2,10), False], 
           [510, 500, 20, 30, random.randint(2,10), False], 
           [395, 460, 10, 20, random.randint(2,10), False],
           [425, 460, 10, 20, random.randint(2,10), False],
           [455, 460, 10, 20, random.randint(2,10), False],
           [485, 460, 10, 20, random.randint(2,10), False],
           [515, 460, 10, 20, random.randint(2,10), False],
           [395, 430, 10, 10, random.randint(2,10), False],
           [425, 430, 10, 10, random.randint(2,10), False],
           [455, 430, 10, 10, random.randint(2,10), False],
           [485, 430, 10, 10, random.randint(2,10), False],
           [515, 430, 10, 10, random.randint(2,10), False],
           [790, 170, 15, 20, random.randint(2,10), False], #Municipal Palace
           [815, 170, 15, 20, random.randint(2,10), False],
           [910, 170, 15, 20, random.randint(2,10), False],
           [935, 170, 15, 20, random.randint(2,10), False],
           [880, 540, 15, 20, random.randint(2,10), False], #grey building
           [910, 540, 15, 20, random.randint(2,10), False],
           [940, 540, 15, 20, random.randint(2,10), False],
           [970, 540, 15, 20, random.randint(2,10), False],
           [880, 460, 15, 20, random.randint(2,10), False], 
           [910, 460, 15, 20, random.randint(2,10), False],
           [940, 460, 15, 20, random.randint(2,10), False],
           [970, 460, 15, 20, random.randint(2,10), False]]       



#loop through all the windows, and change the state, if their time has passed
def blinkWindows():
	now= time.time()
	last_digit = int(repr(now)[-1]) # get last digit of now
	
	for window in windows:
		window[4]= random.randint(1,1000) #assign random int to time remaining
		if last_digit> window[4]:         #if time remaining is less than now
			window[5]= not window[5]  #negate state		
			window [4] = last_digit + random.randint (10,20) #re-assign time-remaining
	
	for archh in arches:
		archh[4]= random.randint(1,1000) #assign random int to time remaining
		if last_digit> archh[4]:         #if time remaining is less than now
			archh[5] = not archh[5]	 #negate state		
			archh[4] = last_digit + random.randint (10,20) #re-assign time-remaining	

	

# check buttons that were clicked, update variables
def buttonClicked():
	if Draw.mousePressed():
		curX= Draw.mouseX() #get x coordinate of mouse click
		curY= Draw.mouseY() #get y coordinate of mouse click
		
		# check if click was within the day/night button range
		if curX >=1035 and curX<=1075 and curY>=412 and curY<=454:
			button[2] = not button[2] #negate false statement'
		
		#check if click was within the info button range
		if curX >=1035 and curX<=1075 and curY>=465 and curY<=505:
			info[1] =not info[1] #negate false statement
			

		for person in people:
			# check if click was within the image range
			# bigger than x, smaller than x+width
			# bigger than y, smaller than y+height
			if curX >= person[1] and curX <= person[1]+person[3] and\
			   curY >= person[2] and curY <= person[2]+person[4]:
				person[5] = not person[5] #negate false statement
							
#a function that will draw the imported gif images from a 2d list
def drawImage (images):
	for image in images: #loop through 2d list, draw image
		Draw.picture(image[0], image[1], image[2])

#a function that will draw the imported gif images from a 2d list that has day and night elements
def drawImageNight(images):
	for image in images:
		if button[2]==True:
			Draw.picture(image[0], image[2], image[3])
		else:
			Draw.picture(image[1], image[2], image[3])

#function that will draw the left or right facing gif, depending on direction. Used for boats		
def drawImageDirection(images):
	for image in images:
		
		#if its on day mode and going to the right
		if button[2]==True and image[9]==True:
			Draw.picture(image[0], image[2], image[3])
		
		# if its on day mode and going to the left	
		elif button[2]==True and image[9]==False:
			Draw.picture(image[5], image[2], image[3])
			
		# if its on night mode and going to the right
		elif button[2]==False and image[9]==True:
			Draw.picture(image[1], image[2], image[3])
		
		# if its on night mode and going to the left	
		elif button[2]==False and image[9]==False:
			Draw.picture(image[6], image[2], image[3])		
	
		
#moving function for clouds and birds
def moving(items):
	
	counter= 0
	if counter%5 ==0: #update variables to make items move
		for x in items: #loop through elements of list
			x[1]+=x[3] #add the speed to the x coordinate
			
			#if the x coordinate is outside of canvas width to the right
			if x[1]>=1100:
				x[1]=0 #re-assign x coordinate to be 0 (right side)
				x[2]= random.randint(0,590) #re-assign y coordinate to a random position
			
			#if the x coordinate is outside of canvas width to the Left
			elif x[1]+x[4]<=0:
				x[1]=1099 #re-assign x coordinate to be 1009 (left side)
				x[2]= random.randint(0,590) #re-assign y coordinate to a random position
	counter += 2 #update counter
	
		
#function to move boat			
def moveBoat(items):
	counter= 0
	if counter%5 ==0: #move boat with updated variables	
		for x in items:
			x[2]+=x[4] # add speed to x coordinate	
	
			#check if the boat got to the border of the sea 
			# the 'sea area' is divided into 3 rectangles
			
			# if boat's x is bigger than rect1's right limit and smaller 
			# than rect1's y limit
			if x[2]+x[7]>=800 and x[3]+x[8]<115:
				x[4] *= -1     #change direction of speed
				x[9]= not x[9] #negate True/False statement (dictates dirction)
			
			# if boat's x is bigger than rect2's right limit and in between 
			# rect2's y limit			
			elif x[2]+x[7]>=475 and x[3]+x[8]<=175 and x[3]+x[8]>=115:
				x[4] *= -1     #change direction of speed
				x[9]= not x[9] #negate True/False statement (dictates dirction)
			
			# if boat's x is bigger than rect3's right limit and in between 
			# rect3's y limit		
			elif x[2]+x[7]>=250 and x[3]+x[8]>175:
				x[4] *= -1      #change direction of speed
				x[9]= not x[9]  #negate True/False statement (dictates dirction)
			
			# if the boats y coordinate got to the left of canvas width
			elif x[2]<=0:
				x[2] =0        #re-assign x coordinate to be 0
				x[4] *=-1      #change direction of speed
				x[9]= not x[9] #negate True/False statement (dictates dirction)
	counter += 2 #update counter
			

#a function to draw tet
# inputs: size of font, font style, text to display, x, y, wether its bold or not
def DrawString( size, font, color, text, x, y, state):
	Draw.setFontSize(size)
	Draw.setFontFamily(font)
	Draw.setColor(color)
	Draw.setFontBold(state)
	Draw.string(text, x, y)
			

#function to draw arches
def arch(x,y,w,h):
	Draw.filledRect(x,y,w,h) #draws the rectangle
	Draw.filledOval(x, y-w/2, w-1, w-1) #draws circle over rectangle
	

# DrawScene: responsible for redrawing the entire canvas
def drawScene():
	#draw background
	# t is a variable that will modify the color of the buildings depending
	# wether its on day/night mode
	if button[2]==True: #if its on day mode
		t=0 
		Draw.picture("background.gif", 0, 0) # day background
	
	else: #if its on night mode
		t= 40 #the color will be modified by 40 points, making it darker
		Draw.picture("backgroundNight.gif", 0, 0) # night background
	
	#draw boats
	drawImageDirection(boats)	
		
	# Draw yellow building (tall one with square windows)
	Draw.setColor(Draw.color(199-t,169-t,88-t))
	Draw.filledRect(370,200,70,120)  #building
	
	for x in range(0,41,20): #windows
		for y in range(0,91,30):
			Draw.setColor(Draw.BLACK)
			Draw.filledRect(380+x,y+210,10,20)
			
	# Draw red building (first one to the left)
	Draw.setColor(Draw.color(190-t,134-t,106-t))# building top part
	Draw.filledRect(100,250,130,90)      
	
	Draw.setColor(Draw.color(216-t,158-t,126-t)) #building bottom part
	Draw.filledRect(100,295,130,45)
	
	Draw.setColor(Draw.color(189-t, 87-t, 59-t))
	coords = [91,250, 120,221,210,221,239,250]  #draw roof of building
	Draw.filledPolygon(coords)
	
	Draw.setColor(Draw.BLACK)
	for x in range (0,91,30):
		Draw.setColor(Draw.BLACK) 
		Draw.filledRect(x+110,260,20,30) #upper windows
	arch(150, 310, 30, 30)                   #door
	
	# Draw blue building (second one from the left)
	Draw.setColor(Draw.color(172-t,190-t,204-t)) 
	Draw.filledRect(220,270,160,80) #building
	
	Draw.setColor(Draw.BLACK)
	for x in range (0,121,30):
		for y in range (0,41,40):
			arch(230+x, 290+y, 20, 20)  #windows
	
	# Draw Museum of the Canal (the one in the bottom middle)
	Draw.setColor(Draw.color(233-t, 233-t, 233-t))
	Draw.filledRect(370,410,180,120)  #building top part
	
	Draw.setColor(Draw.color(153-t, 153-t, 153-t))
	Draw.filledRect(370,485,180,46) #bottom frieze
	
	Draw.setColor(Draw.color(230-t, 170-t, 133-t))
	coords=[380,390,540,390, 560, 410, 360, 410] #roof
	Draw.filledPolygon(coords)
	
	Draw.setColor(Draw.BLACK)
	for x in range (0,121,30): 
		arch(390+x, 500, 20, 30) #lower doors	
		arch(395+x, 460, 10, 20) #middle windows
		arch(395+x, 430, 10, 10) #upper windows
		
	
	#Draw Municipal Palace (top right corner)
	Draw.setColor(Draw.color(188-t, 178-t, 156-t))
	Draw.filledRect(770, 60, 210, 130)#building
	
	Draw.setColor(Draw.color(160-t, 149-t, 128-t))
	Draw.filledRect(770,98,210,50) #middle frieze
	
	Draw.setColor(Draw.color(204-t, 191-t, 166-t))
	Draw.filledRect(847,32,54,157) #middle column
	
	Draw.setColor(Draw.color(160-t, 149-t, 128-t))
	coords=[849,12, 899, 12, 910, 32, 838, 32] #roof
	Draw.filledPolygon(coords)
	
	Draw.setColor(Draw.BLACK)
	for x in range (0,26, 25): 
		arch(790+x, 170, 15,20) #lower side doors
		arch(910+x, 170, 15,20)
		Draw.filledRect(790+x,110, 15,30)  #middle side windows
		Draw.filledRect(910+x,110, 15,30)
		Draw.filledRect(790+x,70, 15,20) #upper side windows
		Draw.filledRect(910+x,70, 15,20)
	Draw.filledRect(860,150,30,40) # principal door
	arch(860,90,30,50) #middle arch
	arch(860,53,30,14) #top arch
	
	# Draw grey building (bottom right corner)
	Draw.setColor(Draw.color(225-t, 227-t, 224-t))
	Draw.filledRect(860, 440, 145, 120) #building
	
	Draw.setColor(Draw.color(52-t, 86-t, 86-t))
	coords= [840, 440, 861, 420, 1004, 420, 1025, 440] #roof
	Draw.filledPolygon(coords)
	
	Draw.setColor(Draw.BLACK)
	for x in range(0,91,30):
		arch(880+x,540,15,20) #lower doors
		Draw.filledRect(880+x,490,15,30) #middle windows
		arch(880+x,460,15,20) #upper windows
		
	#Draw clock tower
	Draw.setColor(Draw.color(188-t, 181-t, 162-t))
	Draw.filledRect(970,361,66,45) #draw bottom rect
	
	Draw.setColor(Draw.color(219-t, 211-t, 186-t))
	Draw.filledRect(970, 286,66,75) #draw middle rect
	
	Draw.setColor(Draw.color(226-t, 218-t, 197-t))
	Draw.filledRect(973,228,59,52) #draw upper rect
	
	Draw.setColor(Draw.color(198-t, 191-t, 172-t))
	coords=[963, 350,1043, 350, 1036, 361, 970, 361]
	Draw.filledPolygon(coords) #draw bottom trapezoid
	
	Draw.setColor(Draw.color(229-t, 222-t, 202-t))
	coords=[963, 275,1043, 275, 1036, 286, 970, 286]
	Draw.filledPolygon(coords) #draw middle trapezoid
	
	Draw.setColor(Draw.color(234-t, 226-t, 208-t))
	coords= [965, 221,1040,221,1032,228,973,228]
	Draw.filledPolygon(coords) #draw upper trapezoid
	
	Draw.setColor(Draw.BLACK)
	Draw.filledOval(984, 236, 34, 34) #clock circle
	arch(990, 302, 26,46) #middle arch
	
	
	#will change window color to yellow (make it 'light up')
	if button[2]==False: #if its on night mode
		for window in windows:
			if window[5]==True:
				Draw.setColor(Draw.color(244,233,122))
				Draw.filledRect(window[0], window[1], window[2], window[3]) #draw yellow window
		for archh in arches:
			if archh[5]==True:
				Draw.setColor(Draw.color(244,233,122)) 
				arch(archh[0], archh[1], archh[2], archh[3])#draw yellow arch
	
	#roof building B (places here so when the windows light up the roof is on top
	Draw.setColor(Draw.color(255-t, 255-t, 255-t)) 
	coords = [237, 253, 371, 253, 397, 270, 211, 270] 
	Draw.filledPolygon(coords)	
	
		
	drawImage(people) #Draw people from the people list
	drawImageNight(trees) #draw trees from the tree list
	
	# if the person was clicked on, draw text box
	for person in people:
		if person[5] == True:
			Draw.setColor(Draw.color(72,197,220))
			# draw text box
			Draw.filledRect(person[7], person[8], person[9], person[10])
			DrawString(9, 'Times New Roman', Draw.WHITE, person[6],person[7]+10, person[8]+5, False)
	
	drawImage(birds) #draw birds from bird list
	drawImage(clouds) #draw clouds from cloud list
	
	#draw day/night button
	Draw.setColor(Draw.color(198,143,151))
	Draw.filledRect(1035,412,40,40) #draw button
	if button[2] == True: #if its on day mode
		Draw.picture(button[0], 1037.5, 413.5) #draw picture of sun
	else: #if its on night mode
		Draw.picture(button[1], 1039.5, 415.5) #draw picture of moon
		
		

#function that will draw the intro scene and intro button
def drawIntro():
	#draw the info button
	if info[1]==True: #if the info button was clicked
		
		Draw.setColor(Draw.color(72,197,220))
		Draw.filledPolygon([1075,485,1035,465,1035,505]) #draw button as a triangle
		Draw.filledRect(50,50,1000,500)	#draw info rectangle
		
		#Draw the text on display
		DrawString(25, "Arial", Draw.WHITE, "Welcome to", 470, 140, False) 
		DrawString(50, "Arial", Draw.WHITE, "CASCO ANTIGUO", 290, 180, True)
		DrawString(16, "Arial", Draw.WHITE, \
			   "This area was labeled by UNESCO as a Cultural World Heritage Site, as it's origins date back \
		\nto 1673. In Casco, you can enjoy cultural visits to museums, a taste of the local cuisine, and unique \
		\nnightlife activities. The area is home to various cultures within the country, and each contributes \
		\nto the diverse folklore felt in Panamá city. \n \nTo learn more, click on the avatars!", 100, 300, False)
		DrawString(10, 'Arial', Draw.WHITE,"to start, click on triangle", 900 ,475, False)

	else: #When the info button is not pressed
		Draw.setColor(Draw.color(198,143,151))
		Draw.filledRect(1035,465,40,40) #draw button as a square
		Draw.picture(info[0], 1048,470) #draw info icon
			
		
# function that will draw the moving hands of the clock	
def drawClock(angle):
	Draw.setColor(Draw.WHITE)
	#get x location of hand: x of middle of circle * cos of angle * radius
	endX = 1001 + math.cos(math.radians(angle)) * 17 
	#get x location of hand: y of middle of circle * sin of angle * radius
	endY = 253 + math.sin(math.radians(angle)) * 17 
	Draw.line(1001, 253, endX, endY)  # Draw the hand
	

def main(): 
	
	Draw.setCanvasSize(1100,600) #draw canvas
	ang=0 #angle for the hands of clock
	
	while True:	
		#check for a click and update relevant variables
		buttonClicked()
		
		# update variables associated with moving things
		ang = (ang+0.1) % 360 #angle of clock hand
		
		moveBoat(boats)
		moving(clouds)
		moving(birds)
		blinkWindows()
		Draw.show()				
		
		Draw.clear()
		drawScene()
		
		drawClock(30 + ang) #update variables of clock hands
		drawIntro()
			
		Draw.show()		

main()