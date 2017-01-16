#cs440 project2 
#collaborated with Jun and Taiga
#!/usr/bin/python


from subprocess import Popen, PIPE
from thread import start_new_thread
from time import sleep
import random

wumpinst = Popen("wump", stdout=PIPE, stdin=PIPE)

buf = ""
op = ""
def read_chars():
	global buf
	while 1:
		c = wumpinst.stdout.read(1)
		buf += c

start_new_thread(read_chars, tuple())
sleep(.1)

def get_output():
	global buf
	global op
	op = buf
	buf = ""
	return op 


curRoom = 0
preRoom = 0
notDead = True
gameFinish = False
gameCounter = 0
loseCounter = 0
safeRoom = False
breezeRoom = False
smellRoom = False
rustleRoom = False
visitedRoom = []
batsfault = False
dontEnter = []
wasPit = ""
worstsmell = 0
moves = 0
wantgothere = []
lookfor = []
notyetshooting = True
prehunting = []
didinthit = False
justendit = False

dangernodes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0,
6:0, 7:0, 8:0, 9:0, 10:0, 
11:0, 12:0, 13:0, 14:0, 15:0,
16:0, 17:0, 18:0, 19:0, 20:0}

adjRooms = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[],
6:[], 7:[], 8:[], 9:[], 10:[], 
11:[], 12:[], 13:[], 14:[], 15:[],
16:[], 17:[], 18:[], 19:[], 20:[]}

def theverystart():
	beginning = "n" + "\n"
	wumpinst.stdin.write(beginning)
	sleep(0.2)

def initializeNewgame():
	global notDead
	global safeRoom
	global gameFinish
	global dangernodes
	global needCourage
	global dontEnter
	global worstsmell
	global batsfault
	global rustleRoom
	global smellRoom
	global breezeRoom
	global adjRooms
	global moves
	global wantgothere
	global curRoom
	global preRoom
	global lookfor
	global notyetshooting
	global prehunting
	global didnthit
	global visitedRoom
	global justendit
	for i in range(21):
		dangernodes[i] = 0
	gameFinish = False
	notDead = True
	safeRoom = False
	needCourage = False
	dontEnter = []
	worstsmell = 0
	batsfault = False
	rustleRoom = False
	smellRoom = False
	breezeRoom = False
	adjRooms = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[],
6:[], 7:[], 8:[], 9:[], 10:[], 
11:[], 12:[], 13:[], 14:[], 15:[],
16:[], 17:[], 18:[], 19:[], 20:[]}
	moves = 0
	wantgothere = []
	curRoom = 0
	preRoom = 0
	lookfor = []
	notyetshooting = True
	prehunting = []
	didnthit = False
	visitedRoom = []
	justendit = False

def gamefollower():
	newgame = "y" + "\n"
	samecave = "y" +"\n"
	wumpinst.stdin.write(newgame)
	sleep(0.2)
	get_output()
	wumpinst.stdin.write(samecave)
	sleep(0.2)
	
def dead_checker():
	global notDead
	if notDead is False:
		return True
	if notDead is True:
		return False


def JUST_DO_IT():
	global adjRooms
	global curRoom
	
	#print ("JUST DO IT!!!")
	x = adjRooms[curRoom][0]
	y = adjRooms[curRoom][1]
	z = adjRooms[curRoom][2]
	
	courage = random.randint(0, 2)
	if courage == 0:
		t = "m " + str(x) + "\n"
		wumpinst.stdin.write(t)
		sleep(0.2)
	elif courage == 1:
		t = "m " + str(y) + "\n"
		wumpinst.stdin.write(t)
		sleep(0.2)
	elif courage == 2:
		t = "m " + str(z) + "\n"
		wumpinst.stdin.write(t)
		sleep(0.2)
	return 0
		
	
def room_adding(adjacent):
	global curRoom
	global adjRooms
	global visitedRoom
	
	if curRoom not in visitedRoom:
		for i in range(len(adjacent)):
			x = adjacent[i]
			adjRooms[curRoom].append(x)
	return 0

def connection_room():
	global worstsmell
	global adjRooms
	global visitedRoom
	global lookfor
	global curRoom
	lookingRoom = []
	
	#print("connection checking!")
	
	for i in range(len(lookfor)):
		for k in adjRooms:
			t = lookfor[i]
			if t in adjRooms[k]:
				lookingRoom.append(t)
	
	#print(adjRooms)
	#print(lookingRoom)
	
	return lookingRoom

def wumplookingRoom():
	global adjRooms
	global visitedRoom
	global curRoom
	global wantgothere
	
	lookingRoom = []
	
	for i in range(len(wantgothere)):
		for k in adjRooms:
			t = wantgothere[i]
			if t in adjRooms[k]:
				if t not in lookingRoom:
					lookingRoom.append(t)
	
	#print("looking room is", lookingRoom)
	return lookingRoom

def previous_safe_checker():
	global safeRoom
	global adjRooms
	global visitedRoom
	global preRoom
	
	if preRoom == 0:
		return True
	
	x = adjRooms[preRoom][0]
	y = adjRooms[preRoom][1]
	z = adjRooms[preRoom][2]
	
	l = dangernodes[x]
	m = dangernodes[y]
	n = dangernodes[z]
	
	dangers = [l, m, n]
	
	sumdanger = sum(dangers)
	if sumdanger == -3:
		safeRoom = True
	return 0
		
		

def smell_hunter():
	global worstsmell
	global adjRooms
	global visitedRoom
	global wantgothere
	global prehunting
	
	for i in adjRooms:
		if worstsmell in adjRooms[i]:
			prehunting.append(i)
			
	for i in range(len(prehunting)):
		for k in adjRooms:
			t = prehunting[i]
			if t in adjRooms[k]:
				wantgothere.append(k)
	return 0

def special_smell_hunter():
	global adjRooms
	global visitedRoom
	global wantgothere
	global dontEnter
	global prehunting
	global worstsmell
	
	
	
	if len(dontEnter) >= 3:
		for i in dangernodes:
			x = dangernodes[i]
			if x == 10:
				worstsmell = i
			elif x == 110:
				worstsmell = i
			elif x == 1010:
				worstsmell = i
			elif x == 1110:
				worstsmell = i

	for i in adjRooms:
		if worstsmell in adjRooms[i]:
			prehunting.append(i)
	
	for i in range(len(prehunting)):
		for k in adjRooms:
			b = prehunting[i]
			if b in adjRooms[k]:
				wantgothere.append(k)
	return 0
			
		
def danger_adder(dmessage, roomlist):
	global dangernodes
	global visitedRoom
	global curRoom
	frontier = []
	global adjRooms
	global breezeRoom
	global smellRoom
	global rustleRoom 
	breezeRoom = False
	smellRoom = False
	rustleRoom = False
	#print("in the danger_adder")
	counter = 0
	
	for i in range(len(roomlist)):
		t = roomlist[i]
		if t not in visitedRoom:
			frontier.append(t)

			
	for i in range(len(visitedRoom)):
		t = visitedRoom[i]
		if t in dangernodes:
			dangernodes[t] = -1
	
	
	if "whoosh" in dmessage:
		breezeRoom = True
	
	if "rustle" in dmessage:
		rustleRoom = True

	if "sniff" in dmessage:
		smellRoom = True
	
	if "whoosh" not in dmessage:
		counter += 1
	
	if "rustle" not in dmessage:
		counter += 1
	
	if "sniff" not in dmessage:
		counter += 1
		
	if counter == 3:
		for i in range(len(frontier)):
			x = frontier[i]
			dangernodes[x] = -1
	"""
	if ("whoosh" and "rustle" and "sniff") not in dmessage:
		for i in range(len(frontier)):
			x = frontier[i]
			dangernodes[x] = -1
	"""	
	#print(frontier)
	
	if len(frontier) >= 1:
		for i in range(len(frontier)):
			x = frontier[i]
			j = dangernodes[x]
			if j != -1 and x not in dontEnter:
				if breezeRoom is True:
					dangernodes[x] += 100
					"""
					if smellRoom is True:
						dangernodes[x] += 10
					if rustleRoom is True:
						dangernodes[x] += 1000
					"""
				if rustleRoom is True:
					dangernodes[x] += 1000
					"""
					if smellRoom is True:
						dangernodes[x] += 10
					if breezeRoom is True:
						dangernodes[x] += 100
					"""
				if smellRoom is True:
					dangernodes[x] += 10
					"""
					if breezeRoom is True:
						dangernodes[x] +=100
					if breezeRoom is True:
						dangernodes[x] += 1000
					"""
	#print(dangernodes)
	if len(frontier) >= 1:
		for i in range(len(frontier)):
			x = frontier[i]
			if dangernodes[x] >= 2000:
				if x not in dontEnter:
					dontEnter.append(x)
			elif dangernodes[x] >= 200 and dangernodes[x] < 1000:
				if x not in dontEnter:
					dontEnter.append(x)
			elif dangernodes >= 1200:
				if x not in dontEnter:
					dontEnter.append(x)
			
	for i in range(len(dangernodes)):
		t = dangernodes[i]
		if t == 20:
			worstsmell = i
		elif t == 120:
			worstsmell = i
		elif t == 1020:
			worstsmell = i
		elif t == 1120:
			worstsmell = i

	return 0
		
def previous_was_danger():
	global safeRoom
	global adjRooms
	global visitedRoom
	global preRoom
	
	if preRoom == 0:
		return True
	x = adjRooms[preRoom][0]
	y = adjRooms[preRoom][1]
	z = adjRooms[preRoom][2]
	
	l = dangernodes[x]
	m = dangernodes[y]
	n = dangernodes[z]
	
	options = [x,y,z]
	actualoptions = []
	
	dangers = [l, m, n]
	
	deldangers = []
	"""
	for i in range(len(dangers)):
		if dangers[i] == -1:
			deldangers.append(i)
	
	for i in range(len(deldangers)):
		t = deldangers[i]
		if t in dangers
	"""
	sumdanger = sum(dangers)
	
	if sumdanger == 0:
		return False
	if sumdanger >= 200 and sumdanger < 1000:
		return True
	if sumdanger >= 2000:
		return True
	return False
		
"""
def wump_shoot():
	global notyetshooting
	global prehunting
	global worstsmell
	global didinthit
	global moves
	
	if moves >= 25:
		notyetshooting = False
		if worstsmell > 0:
			t = "s " + str(worstsmell) + "\n"
			wumpinst.stdin.write(t)
			sleep(0.2)
			return 0
		x = random.randint(1, 20)
		t = "s " + str(x) + "\n"
		wumpinst.stdin.write(t)
		sleep(0.2)
		return 0
	
	
	if didinthit is True:
		t = "s "+ str(worstsmell) + "\n"
		wumpinst.stdin.write(t)
		sleep(0.2)
		return 0
	
	t = "s " + str(worstsmell) + "\n"
	didinthit = True
	wumpinst.stdin.write(t)
	sleep(0.2)
	return 0
"""
	
	
def next_move():
	global gameFinish
	global notDead
	if gameFinish is True:
		return 0
	global curRoom
	global dangernodes
	global dontEnter
	global adjRooms
	global batsfault
	global visitedRoom
	global preRoom
	global worstsmell
	global moves
	global wantgothere
	global lookfor
	global notyetshooting
	global didinthit
	global justendit
	
	moves += 1
	#print("im in room,", curRoom, "and at the moves of",moves)
	#if worstsmell > 0:
		#print("i feel smell from...", worstsmell)
	
	supersafe = False
	objective = False
	youcango = False
	trueobjective = False
	cantgo = False
	
	if moves >= 25:
		notyetshooting = False
	
	if notyetshooting is False:
			t = "s " + str(worstsmell) + "\n"
			wumpinst.stdin.write(t)
			sleep(0.2)
			return 0

	#print("looking for!", lookfor)
	
	if len(wantgothere) > 0:
		trueobjective = True
	
	
	dellooms = []
	
	for i in range(len(lookfor)):
		t = lookfor[i]
		if t in visitedRoom:
			dellooms.append(t)
			
	for i in range(len(dellooms)):
		t = dellooms[i]
		if t in lookfor:
			lookfor.remove(t)
	
	for i in range(len(wantgothere)):
		t = wantgothere[i]
		if t == curRoom:
			notyetshooting = False
			return 0
	
	if worstsmell > 0:
		smell_hunter()
	elif moves > 15:
		special_smell_hunter()
		trueobjective = True
	
	
	x = adjRooms[curRoom][0]
	y = adjRooms[curRoom][1]
	z = adjRooms[curRoom][2]
	
	
	options = [x,y,z]
	realoptions = options
	
	l = dangernodes[x]
	m = dangernodes[y]
	n = dangernodes[z]
	
	dangers = [l, m, n]
	
	
	retreat_options = []
	prob_nextmove = []
	
	if x in visitedRoom:
		retreat_options.append(x)
	if y in visitedRoom:
		retreat_options.append(y)
	if z in visitedRoom:
		retreat_options.append(z)
	if dangernodes[x] == -1 and x not in visitedRoom:
		prob_nextmove.append(x)
	if dangernodes[y] == -1 and y not in visitedRoom:
		prob_nextmove.append(y)
	if dangernodes[z] == -1 and z not in visitedRoom:
		prob_nextmove.append(z)
	
	if len(prob_nextmove) > 0:
		youcango = True
	
	for i in range(len(dangernodes)):
		t = dangernodes[i]
		if t == -1:
			if i not in visitedRoom and i not in lookfor:
				lookfor.append(i)
	
	isitconnected = []
	
	if len(lookfor) > 0:
		isitconnected = connection_room()
	shouldgo = []
	mustgo = []
	
	#print ("this is isit connected", isitconnected)
	
	if len(isitconnected) > 0:
		for i in range(len(isitconnected)):
			t = isitconnected[i]
			if t in options:
				shouldgo.append(t)
	
	#if len(shouldgo) >=1:
	#print ("this is the shouldgos", shouldgo)
	
	if youcango is False and len(shouldgo) > 0:
		objective = True
	
	if trueobjective is True:
		#print("is trueobjective true?")
		wumpconnected = wumplookingRoom()
		for i in range(len(wumpconnected)):
			t = wumpconnected[i]
			if t in retreat_options:
				mustgo.append(t)
	
	if trueobjective is True:
		for i in range(len(retreat_options)):
			t = retreat_options[i]
			for k in range(len(mustgo)):
				if t in mustgo:
					enter = "m " + str(t) + "\n"
					wumpinst.stdin.write(enter)
					sleep(0.2)
					return 0
				if t not in mustgo:
					cantgo = True 
	
	if len(retreat_options) == 2 and breezeRoom is True:
		for i in range(len(options)):
			t = options[i]
			if t not in retreat_options:
				dangernodes[t] += 200
	
	if len(retreat_options) == 2 and rustleRoom is True:
		for i in range(len(options)):
			t = options[i]
			if t not in retreat_options:
				dangernodes[t] += 2000
	
	if objective is True:
		#print("is objective true?")
		for i in range(len(shouldgo)):
			t = shouldgo[i]
			if t in retreat_options:
				enter = "m " + str(t) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
			if t not in retreat_options:
				cantgo = True
	
	if cantgo is True:
		#print("i hope this is not the problem")
		if len(retreat_options) == 1:
			p = retreat_options[0]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(retreat_options) == 2:
			t = random.randint(0,1)
			p = retreat_options[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(retreat_options) == 2:
			t = random.randint(0,1)
			p = retreat_options[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
	
	sumdangers = sum(dangers)
	if breezeRoom is True and rustleRoom is False and objective is False and youcango is False:
		#if (sumdangers >= len(dangers)*100):
		previous_was_danger()
		if previous_was_danger() is True:
			JUST_DO_IT()
			return 0

	if breezeRoom is True and rustleRoom is True and objective is False and youcango is False:
		#if (sumdangers >= len(dangers)*1000) and -1 not in dangernodes:
		previous_was_danger()
		if previous_was_danger() is True:
			JUST_DO_IT()
			return 0
	
	if rustleRoom is True and breezeRoom is False and objective is False and youcango is False:
		if previous_was_danger() is True:
			JUST_DO_IT()
			return 0
	#if breezeRoom is True and smellRoom is True and rustleRoom is False and youcango is False:
		
	if youcango is True:
		if len(prob_nextmove) == 1:
			p = prob_nextmove[0]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(prob_nextmove) == 2:
			t = random.randint(0,1)
			p = prob_nextmove[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(prob_nextmove) == 3:
			t = random.randint(0,2)
			p = prob_nextmove[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
	
	if breezeRoom is True and rustleRoom is False and youcango is True:
		if len(prob_nextmove) == 1:
			p = prob_nextmove[0]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(prob_nextmove) == 2:
			t = random.randint(0,1)
			p = prob_nextmove[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
	
	if breezeRoom is False and rustleRoom is True and youcango is True:
		if len(prob_nextmove) == 1:
			p = prob_nextmove[0]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		if len(prob_nextmove) == 2:
			t = random.randint(0,1)
			p = prob_nextmove[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
	
	sameroom_options = []
	compare_options = []
	
	if sumdangers < 0:
		supersafe = True
		for i in range(len(options)):
			t = options[i]
			if t in visitedRoom: 
				sameroom_options.append(t)
			if t not in visitedRoom:
				compare_options.append(t)
	
	if trueobjective is False and supersafe is True:
		if len(compare_options) > 0:
			if len(compare_options) == 1:
				p = compare_options[0]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
			if len(compare_options) == 2:
				t = random.randint(0,1)
				p = compare_options[t]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
			if len(compare_options) == 3:
				t = random.randint(0,2)
				p = compare_options[t]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0

	
	previous_safe_checker()
	if safeRoom is True and rustleRoom is False and breezeRoom is False and trueobjective is False:
		for i in range(len(options)):
			t = options[i]
			if t not in visitedRoom:
				compare_options.append(t)
				dangernodes[t] = -1
				
	if safeRoom is True and rustleRoom is False and breezeRoom is False and trueobjective is False:
		if len(compare_options) > 0:
			if len(compare_options) == 1:
				p = compare_options[0]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
			if len(compare_options) == 2:
				t = random.randint(0,1)
				p = compare_options[t]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
			if len(compare_options) == 3:
				t = random.randint(0,2)
				p = compare_options[t]
				enter = "m " + str(p) + "\n"
				wumpinst.stdin.write(enter)
				sleep(0.2)
				return 0
	
	if rustleRoom is True and breezeRoom is False and smellRoom is False and youcango is False:
		if len(retreat_options) == 0:
			t = random.randint(0,2)
			p = options[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		elif len(retreat_options) == 1:
			previous_was_danger()
			if previous_was_danger() is True:
				JUST_DO_IT()
				return 0
			
	if rustleRoom is True and smellRoom is True and breezeRoom is False and youcango is False:
		if len(retreat_options) == 0:
			t = random.randint(0,2)
			p = options[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		elif len(retreat_options) == 1:
			previous_was_danger()
			if previous_was_danger() is True:
				JUST_DO_IT()
				return 0
	
	if smellRoom is True and breezeRoom is False and rustleRoom is False and youcango is False:
		if len(retreat_options) == 0:
			t = random.randint(0,2)
			p = options[t]
			enter = "m " + str(p) + "\n"
			wumpinst.stdin.write(enter)
			sleep(0.2)
			return 0
		elif len(retreat_options) == 1:
			JUST_DO_IT()
			return 0
	
	return 0

def message_checker():
	global op
	message = op
	newmessage = []
	nextroomlist=[]
	global curRoom
	global batsfault
	#print("extra message", message)
	newmessage = message.split()
	global dangernodes
	global notDead
	global preRoom 
	global visitedRoom
	global dontEnter
	global moves
	global adjRooms
	global gameFinish
	
	waspit = False
	if curRoom > 0:
		preRoom = curRoom
	
	roomnow = "You are in room"
	z = message.find(roomnow)
	u = z + 20
	#print("roomnow at", z)
	
	for i in range(21):
	  x = "room " + str(i)
	  if x in message:
			  #print("this must be the number", i)
			  curRoom = i
	
	if "Without" in message:
		dontEnter.append(curRoom)
		waspit = True
		
	
	if "humongous" in message:
		dontEnter.append(preRoom)
		batsfault = True
		preRoom = 0
	
	for i in range(21):
		x = str(i) + ","
		if x in newmessage:
			nextroomlist.append(i)
	
	for i in range(21):
		x = str(i) + "."
		if x in newmessage:
			nextroomlist.append(i)
		
	if curRoom not in visitedRoom:
	  #print(curRoom)
	  room_adding(nextroomlist)
	  visitedRoom.append(curRoom)
	  #print("this is visited rooms", visitedRoom)
	  danger_adder(message, nextroomlist)
	  if wasPit is True:
		visitedRoom.remove(curRoom)
	  
		  
	if "sinking" in newmessage:
		notDead = False
		
	if "*chomp*" in newmessage:
		notDead = False
	
	if "CHOMP" in message:
		notDead = False
		
	if "rampages" in message:
		notDead = False
		
	if "AAAUUUUGGGGGHHHHHhhhhhhhhh" in message:
		notDead = False
		
	if "dinner" in message:
		notDead = False
	
	if dead_checker() is True:
		gameFinish = True
		global loseCounter
		gameCounter += 1
		loseCounter += 1
	
	if "groan" in message:
		global gameCounter
		gameCounter += 1
		gameFinish = True
		print("this cant be true")
	
	return 0

print(get_output())
sleep(0.2)
theverystart()
initializeNewgame()

for i in range(10):
	while gameFinish is not True:
		get_output()
		message_checker()
		next_move()
		sleep(0.2)
		
	print("finished game:", i)
	gamefollower()
	sleep(0.2)
	initializeNewgame()
	


print("one game finished")

print("game played", gameCounter)
print("game lost", loseCounter)
