from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.effects.scroll import ScrollEffect
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from functools import partial
import alienstoryarr
import aliencompletion
import importlib
import os

class AlienScreens(ScreenManager):
	pass
		
class GotoMainPopup(Popup):
	yes = ObjectProperty(None)
	no = ObjectProperty(None)
	
class QuitPopup(Popup):
	pass

class ChoiceButtonGrid(GridLayout):
	pass


#self.curNode.__class__.__name__
#for getting name of class
####
class StoryDisplayer(Screen):
	def CheckIfNeedExtraData(self):
		if hasattr(self.curNode, "checkForExtra"):
			self.curNode.AccessExtra()

	def resetter(self, i = 0):
		self.CheckIfNeedExtraData()
		if hasattr(self, "g"):
			self.remove_widget(self.g)
		self.i = i
		self.ids.lab.text = self.curNode.story[0]
		self.ids.sv.size_hint_y = .93
		self.ids.contid.size_hint_y = 0.05
		self.ids.sv.pos_hint = {"y": 0.0}
		aliencompletion.ScreensAdd(self.curNode.__class__.__name__)

	def BeforeEntering(self):
		if AlienMain.GetIfContinued():
			curScreen = aliencompletion.GetScreens()[-1]
			self.curNode = getattr(alienstoryarr, curScreen)()
		else:
			aliencompletion.EraseScreens()
			self.curNode = alienstoryarr.StoryStart()
		self.resetter(1)

	def GotoNextPart(self, index, t):
		# Go to next part of story by using the next[] list of node
		if hasattr(self.curNode, "extraStore"):
			#store extra data in the file
			aliencompletion.SetExtra(self.curNode.extraStore, self.curNode.extraValues[index])

		s = self.curNode.GotoNextPart(index)
		if type(s) == str:
			self.p = GotoMainPopup()
			self.p.ids.l.text = "You completed the Story.\nGo to Main Menu ?"
			self.p.yes.bind(on_press = self.MainChange)
			self.p.open()
		else:
			self.curNode = s
		self.resetter()


	def MakeChoiceButtons(self):
		self.g = ChoiceButtonGrid()
		if len(self.curNode.choices) > 1:
			gridSize = .2
		else:
			gridSize = .1

		self.g.size_hint_y = gridSize
		self.ids.sv.size_hint_y = .93 - gridSize
		self.ids.sv.pos_hint = {"y": gridSize}

		choices = self.curNode.choices
		for elIndex in range(len(choices)):
			gnp = partial(self.GotoNextPart, elIndex)
			self.g.add_widget(Button(text=choices[elIndex], on_press=gnp))

		self.add_widget(self.g)

	def on_touch_up(self, touch):
		if self.i > 0:
			if self.i<len(self.curNode.story):
				self.ids.lab.text += '\n\n' + (self.curNode.story[self.i])
			elif self.i == len(self.curNode.story):
				self.MakeChoiceButtons()

		self.i += 1
		if self.i == 3:
			self.ids.contid.size_hint_y = 0.0


	#The Popup methods
	def goto_Main(self, text = "", fun = False):
		if not fun:
			fun = self.MainChange
		self.p = GotoMainPopup()
		self.p.yes.bind(on_press = fun)
		if text != "":
			self.p.ids.l.text = text			
		self.p.open()
		
	def MainChange(self,ev):
		self.p.dismiss()
		self.manager.current = 'main'
		
	def goBackPop(self):
		self.goto_Main("Go Back ?", self.goBack)
		
	def goBack(self,ev):
		go = aliencompletion.ScreenBack()
		if go == 'main':
			self.MainChange(ev)
		else:
			self.p.dismiss()
			self.curNode = getattr(alienstoryarr, go)()
			self.resetter()


####
class AlienMain(Screen):
	def GetIfContinued():
		return AlienMain.contStory

	def storyStarter(self):
		AlienMain.contStory = False
		self.GotoStory()
		
	def continueStory(self):
		AlienMain.contStory = True
		self.GotoStory()

	def GotoStory(self):
		self.manager.current = 'showstory'
			
	def quitter(self):
		p = QuitPopup()
		p.open()


####
class AlienStory(App):
	def build(self):
		alsc = AlienScreens()
		return alsc
		
if __name__ == "__main__":
	# curFileName = os.path.basename(__file__)
	# curFileName = curFileName.replace(".py","")
	AlienStory().run()
			