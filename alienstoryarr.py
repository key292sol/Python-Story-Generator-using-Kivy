import aliencompletion

class StoryParts():
	start = ['In some few years from now into the future, scientists have discovered life on Mars and want to inspect it so they can know more about it.','They want to send a group of astronauts there to do that. They choose you as one of the people to go there.','You will have to stay away from your family for years and stay there.','Will you accept this and go ?']
	A1  = ['You accepted to go to Mars. ', 'You say goodbye to your family and go in the rocket to Mars with 3 other astronauts. The other 3 were Sam, Jane and Richard. They rocket also had a machine to catch the alien and it could move too. ', 'The rocket takes off and takes you to Mars. Sam says that we should go out and search for the life forms but Jane says that we should stay in the ship for some time because it will be easier to take them if they are near the ship.', 'What do you want to do ?']
	A2  = ['You think that the aliens can be dangerous and decide to stay at home with your family without knowing about the life on Mars.']
	B1  = ['Nobody was joining Sam in going out so even Sam decided to not go out.', 'After waiting for some time too no life form came near the spaceship. Sam said again that we should go out and lure them towards the spaceship.']
	B2  = ['You decide to go out with Sam to search for the life form. The others decide to stay in the spaceship. You both wear your spacesuits and go out.', 'While searching you see a Mars rover which was broken by one of the aliens. ', 'After some time you see something moving at some distance. Sam asks you if you want to lure it to the spaceship so that it is easier to catch it to do research on it or if you want to follow it and find out about how their civilization looks like first.']
	C1  = ['You decide to lure the creature to the spaceship but you have no idea about how to lure it there.', "You shout but the creature doesn't turn back and you fail to lure it. You try a couple of more things but even they don't work.", "You can't talk to the creature because they won't understand you and you don't know how they would react to something unknown.", 'You give up and decide to call the spaceship to send the machine to catch the alien.']
	C2  = ['You decide to follow the life form because you are interested in their civilization.', 'You have a family on Earth so you are interested in how these aliens have developed their civilization. ', 'You miss your family on Earth and think about what they would have been doing now. ', "You and Sam follow the organism for some time from some distance as you don't want to be seen by it.", 'The alien stops midway and stays there. You and Sam decide to call the spaceship to send the machine for catching the alien.']
	C   = ['The machine arrives and the alien is caught and is being brought to the spaceship.', 'You and Sam saw the alien from up close after it had been caught. It had huge eyes and tentacles. It was about 5 feet tall. It looked more like an octopus monster from an horror movie rather than the aliens from sci-fi movies.','The space station above Mars had a chamber to put this alien in there so it had to be taken there.', ' You and Sam saw the alien holding something using one of its tentacles. It looked like the alien had taken a bite from it.', ' You saw that thing on your way to the spaceship so you and Sam decided to pick them up so that the alien can survive.', 'The alien is loaded into the spaceship and the spaceship launches to the space station. The alien is put inside of the container meant for it and you and the others do their normal work.', 'After some time, while you are working with Richard you both hear some sounds coming from around the area where the alien is kept. Richard says that it might just be Sam doing his work.']
	D1  = ["You decided to check out the sound and go to the chamber where the alien is kept.", "It doesn't look like something happened there. The alien looks calm. ","You see that a lose screw is floating around in the room. It came out from the one of the parts of the alien container. ", "You fix it and then check the whole room and return to Richard and tell him about it. ","Richard says that something might have hit the container while floating around in zero gravity. You agree with him."]
	D   = ["You agree with Richard and continue doing your work.","After some time, you and the other 3 astronauts start doing the research and observations on the alien.", "While everyone is doing the observations you notice a scratch on the glass shield between you and the alien. ", "You think it won't be a problem because you are supposed to send the alien on Mars again after the observations are done. But you still tell everyone else about the scratch and everyone says the same thing that you were thinking.","Most of the observations and research related to the alien are done and the other few are supposed to be completed after a certain period of time.", "The 4 of you have some fun together for some time. ", "You need to send the results back to Earth and you need a helping hand with you. Who are you going to take with yourself ?"]
	E   = ["You chose {choice} to help you with the sending of data. ","While you two are working, after some time the other two decide to continue the tests. They come to inform both of you that they are going to continue the tests now.","They both inform you two and go towards the room of the alien and you continue your work. ","After a couple of moments you hear a loud sound coming from there. The sound startles you and {choice}.","It sounded like some glass broke and something hard hit on a wall or a floor. Both of you get worried about the other two and decide to go and check on them. ","As you start to go towards there, you see the both of them coming towards you. ","They tell you that the alien has broke the glass and is trying to escape. ","Another sound similar to the last one comes from the room. The lights in the space station turn red.","Jane suggests everyone that they should go in the control room and close the door of the aliens room. Everyone agrees with her and heads to the control room.","While everyone is heading to the control room you want to see the alien. What do you do?"]
	F1  = ["You decide to go to the aliens room.","You move towards there while floating in zero gravity through the red passageway. The sound of the banging on the glass increases in volume as you reach closer.","You reach the room's door.","You stop there before looking.","You here a loud scream by the alien. The alien is banging on the glass to get out. You are scared.","You peek from the door at the alien. The container has been broken. Three of the tentacles are out of the container and the alien is trying to get out through the hole but it can't.","There is also some kind of liquid coming out of its tentacles. It might possibly be the blood of the alien.","It hits again and the hole gets bigger.","The alien looks at you as you stand still and terrified. The alien lets out a screech while trying to get out through the hole.","Suddenly, you are pulled out of the room.","You turn and see Sam next to you. He was the one who pulled you out.","He then calls the others and tells them to shut the door. You and Sam proceed to go to the control room."]
	F   = ["Everyone is in the control room and the door for the alien's room has been closed.","Jane says that we need to send the alien back on Mars and to do that we need put it in the spaceship.","Richard proceeds to say that we can't do that by just closing all the doors because there is a chance it might just roam in the station and not go in the ship and we will need someone to pilot the ship.","You remember the alien food you collected while bringing the alien here. It hasn't been used till now.","You tell everyone else about it. They agree that we can use it to lure the alien to the ship.You and Richard say that you want to be the one who do that.","The others tell you that they worried about you. But you say that the alien might be doing this to go back to Mars and it might not like that we kidnapped it from its home."]
	G   = ["You place the alien food in the passageway in line going towards the ship. You put the rest of it in the back of the ship.","Richard is sitting in the ship waiting for you. You come and sit at the controls.","You tell Jane and Sam to open the door of the alien's room. They open the door and the alien comes out.","The alien looks at the floating food and collects it. It is not eating it but it is following the path.","When it enters the spaceship, the door to go out of it is closed and it is then released to be sent to Mars. The alien is hitting the doors because it is trapped once again.","You and Richard take the ship to Mars. The landing was difficult due to the shaking caused by the alien."]
	end = ["When the landing is done, the door is opened for the alien to go out. After the alien has climbed out of the ship and moved away from the ship, the doors are closed and the ship flies back towards the station.","\nWhen you and Richard reach the station everyone is relieved that the everyone is safe.The results of the first observations are present on the space station.","The research could not have been completed because the alien broke free.","But, at least all 4 of you are alive."]

# Node super class exists if we want to add a function in all of the nodes
class Node():
	curNodeName = ""

	def GotoNextPart(self, index):
		if len(self.nextParts) == 0:
			return "main"
		return self.nextParts[index]


class StoryStart(Node):
	def __init__(self):
		self.nextParts = [A1(), A2()]
		self.choices = ["Yes", "No"]
		self.story = StoryParts.start

class A1(Node):
	def __init__(self):
		self.nextParts = [B1(), B2()]
		self.choices = ["Stay In", "Go Out"]
		self.story = StoryParts.A1

class A2(Node):
	def __init__(self):
		self.nextParts = []
		self.choices = ["The End"]
		self.story = StoryParts.A2

class B1(Node):
	def __init__(self):
		self.nextParts = [B2()]
		self.choices = ["Go Out"]
		self.story = StoryParts.B1

class B2(Node):
	def __init__(self):
		self.nextParts = [C1(), C2()]
		self.choices = ["Lure It", "Follow It"]
		self.story = StoryParts.B2

class C1(Node):
	def __init__(self):
		self.nextParts = [C()]
		self.choices = ["Next"]
		self.story = StoryParts.C1

class C2(Node):
	def __init__(self):
		self.nextParts = [C()]
		self.choices = ["Next"]
		self.story = StoryParts.C2

class C(Node):
	def __init__(self):
		self.nextParts = [D1(), D()]
		self.choices = ["Check out the Sound", "Keep doing your work"]
		self.story = StoryParts.C

class D1(Node):
	def __init__(self):
		self.nextParts = [D()]
		self.choices = ["Next"]
		self.story = StoryParts.D1

class D(Node):
	def __init__(self):
		self.nextParts = [E()]
		self.choices = ["Jane", "Sam", "Richard"]
		self.story = StoryParts.D
		self.extraStore = "D"
		self.extraValues = self.choices

	def GotoNextPart(self, index):
		return E()

class E(Node):
	def __init__(self):
		self.nextParts = [F1(), F()]
		self.choices = ["Go to the Alien", "Go with everyone else"]
		self.story = StoryParts.E
		self.extraStore = "E"
		self.extraValues = [" ", 'You think that it might be dangerous to go there now and decide to stay with the others.']
		self.checkForExtra = "D"

	def AccessExtra(self):
		name = aliencompletion.GetExtra(self.checkForExtra)["NodeData"].replace("\n","")
		for index in range(len(self.story)):
			self.story[index] = self.story[index].replace("{choice}", name)


class F1(Node):
	def __init__(self):
		self.nextParts = [F()]
		self.choices = ["Next"]
		self.story = StoryParts.F1

class F(Node):
	def __init__(self):
		self.nextParts = [G()]
		self.choices = ["Next"]
		self.story = StoryParts.F
		self.checkForExtra = "E"

	def AccessExtra(self):
		val = aliencompletion.GetExtra(self.checkForExtra)["NodeData"].replace("\n","")
		if val != " ":
			self.story.insert(0, val)

class G(Node):
	def __init__(self):
		self.nextParts = [AlienEnd()]
		self.choices = ["Next"]
		self.story = StoryParts.G

class AlienEnd(Node):
	def __init__(self):
		self.nextParts = []
		self.choices = ["Next"]
		self.story = StoryParts.end
