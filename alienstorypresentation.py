from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.effects.scroll import ScrollEffect
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import alienstoryarr
import aliencompletion

class AlienScreens(ScreenManager):
	pass
	
class gotoMainPopup(Popup):
	yes = ObjectProperty(None)
	no = ObjectProperty(None)
	
class QuitPopup(Popup):
	pass
	
class TwoGrid(GridLayout):
	pass
	
	
####	
class TheTwoSuper(Screen):
	i = 1
	g = TwoGrid()
	def resetter(self):
		self.ids.lab.text = self.arr[0]
		self.i = 1
		self.ids.sv.size_hint_y = .93
	
	def writer(self):
		aliencompletion.screensAdd(self.name)
			
	def on_touch_up(self, touch):
		if self.i<len(self.arr):
			self.ids.lab.text += '\n\n' + (self.arr[self.i])
			self.i += 1
			
		elif self.i == len(self.arr):
			self.butMaker()
			self.i+=1
			
	def butMaker(self):
		self.ids.sv.size_hint_y = .73
		self.g = TwoGrid()
		self.g.ids.one.text = self.but_1_text
		self.g.ids.one.bind(on_press = self.goto_FirstChoice)
		self.g.ids.two.text = self.but_2_text
		self.g.ids.two.bind(on_press = self.goto_SecondChoice)
		self.add_widget(self.g)
		
	def goto_Main(self):
		self.p = gotoMainPopup()
		self.p.yes.bind(on_press = self.MainChange)
		self.p.open()
		
	def MainChange(self,ev):
		self.p.dismiss()
		self.manager.current = 'main'
		
	def goBackPop(self):
		self.p = gotoMainPopup()
		self.p.ids.l.text = "Go Back ?"
		self.p.yes.bind(on_press = self.goBack)
		self.p.open()
		
	def goBack(self,ev):
		go = aliencompletion.screenBack()
		self.p.dismiss()
		self.manager.current = go
			
	def on_leave(self):
		self.remove_widget(self.g)
		
		
####
class TheOneSuper(TheTwoSuper):
	but_text = "Next"
	def butMaker(self):
		self.ids.sv.size_hint_y = .85
		self.g = Button(text = self.but_text, size_hint = (1,.1), pos_hint = {"y":0},on_press = self.goto_Choice)
		self.add_widget(self.g)
		
		
####
class AlienEndScreen(TheOneSuper):
	index = 14
	arr = alienstoryarr.end
	but_text = 'The End'
	def goto_Choice(self,ev):
		self.the_end()
		
	def the_end(self):
		aliencompletion.eraseScreens()
		self.manager.current = 'main'
		
####
class AlienScreen_G(TheOneSuper):
	index = 13
	arr = alienstoryarr.G
	def goto_Choice(self,ev):
		self.manager.current = 'end'

####
class AlienScreen_F(TheOneSuper):
	index = 12
	arr = alienstoryarr.F
	
	def resetter(self):
		self.i = 2
		if (AlienScreen_E.jump == True):
			self.ids.lab.text = 'You think that it might be dangerous to go there now and decide to stay with the others.'
		else:
			self.ids.lab.text = self.arr[1]
			
	def goto_Choice(self,ev):
		self.manager.current = 'G'
		
		
####
class AlienChoice_F1(TheOneSuper):
	index = 11
	arr = alienstoryarr.F1
	
	def goto_Choice(self,ev):
		self.manager.current = "F"
		
		
####
class AlienScreen_E(TheTwoSuper):
	index = 10
	arr = alienstoryarr.E
	but_1_text = 'Go to the Alien'
	but_2_text = 'Go with everyone else'
		
	def getName(self):
		names = {1:'Jane', 2:'Sam', 3:'Richard'}
		return names.get(AlienChoice_D.getChoice())
		
	def repChoice(self):
		self.i = 1
		name = self.getName()
		self.arr[0] = self.arr[0].replace('{choice}',name)
		self.arr[3] = self.arr[3].replace('{choice}',name)
		self.ids.lab.text = self.arr[0]
		
	def goto_FirstChoice(self,ev):
		AlienScreen_E.jump =  False
		self.manager.current = 'F1'
		
	def goto_SecondChoice(self,ev):
		AlienScreen_E.jump = True
		self.manager.current = 'F'

		
####
class AlienChoice_D(TheTwoSuper):
	index = 9
	arr = alienstoryarr.D
	but_text = ("Jane","Sam","Richard")
	
	def goto_Next(self,num):
		AlienChoice_D.choice = num
		self.manager.current = 'E'
		
	def getChoice():
		return AlienChoice_D.choice
	
	def resetter(self):
		self.i = 1
		if (AlienScreen_C.jump):
			self.ids.lab.text = self.arr[0]
		else:
			self.i += 1
			self.ids.lab.text = self.arr[1]
	
	def butMaker(self):
		self.ids.sv.size_hint_y = .75
		self.g = GridLayout(cols = 1, pos_hint = {'top':.2}, size_hint = (1,.2), spacing = (2,2))
		for i in range(3):
			self.g.add_widget(Button(text = self.but_text[i], on_press = lambda *x: self.goto_Next(i+1)))
		self.add_widget(self.g)
		
		
####
class AlienChoice_D1(TheOneSuper):
	index = 8
	arr = alienstoryarr.D1
	
	def goto_Choice(self,ev):
		self.manager.current = 'D'
	
		
####
class AlienScreen_C(TheTwoSuper):
	index = 7
	arr = alienstoryarr.C
	
	but_1_text = 'Check Out the Sound'
	but_2_text = 'Keep doing your work'
	
	def goto_FirstChoice(self,ev):
		AlienScreen_C.jump = False
		self.manager.current = 'D1'
		
	def goto_SecondChoice(self,ev):
		AlienScreen_C.jump = True
		self.manager.current = 'D'
		
		
####
class AlienChoice_C2(TheOneSuper):
	index = 6
	arr = alienstoryarr.C2
	
	def goto_Choice(self,ev):
		self.manager.current = 'C'

				
####
class AlienChoice_C1(TheOneSuper):
	index = 5
	arr = alienstoryarr.C1
	
	def goto_Choice(self,ev):
		self.manager.current = 'C'
		
	
####
class AlienChoice_B2(TheTwoSuper):
	arr = alienstoryarr.B2
	
	index = 4
	but_1_text = 'Lure It'
	but_2_text = 'Follow It'
			
	def goto_FirstChoice(self,ev):
		self.manager.current = 'C1'
		
	def goto_SecondChoice(self,ev):
		self.manager.current = 'C2'

				
####
class AlienChoice_B1(TheOneSuper):
	arr = alienstoryarr.B1
	
	index = 3
	but_text = 'Go Out'
			
	def goto_Choice(self,ev):
		self.manager.current = 'B2'

				
####
class AlienChoice_A2(TheOneSuper):
	index = 2
	but_text = 'The End'
	arr = alienstoryarr.A2
	def goto_Choice(self,ev):
		self.the_end()
		
	def the_end(self):
		aliencompletion.eraseScreens()
		self.manager.current = 'main'

		
####
class AlienChoice_A1(TheTwoSuper):
	index = 1
	arr = alienstoryarr.A1
	
	but_1_text = 'Stay In'
	but_2_text = 'Go Out'
	
	def goto_FirstChoice(self,ev):
		self.manager.current = 'B1'
		
	def goto_SecondChoice(self,ev):
		self.manager.current = 'B2'

		
####
class AlienFirst(TheTwoSuper):
	index = 0
	arr = alienstoryarr.start
	
	but_1_text = 'Yes'
	but_2_text = 'No'
			
	def goto_FirstChoice(self,ev):
		self.manager.current = 'A1'
		
	def goto_SecondChoice(self,ev):
		self.manager.current = 'A2'
		

####
class AlienMain(Screen):
	def storyStarter(self):
		aliencompletion.eraseScreens()
		self.manager.current = 'Start'
		
	def continueStory(self):
		seq = aliencompletion.getScreens()
		try:
			self.manager.current = seq[-1]
		except:
			self.manager.current = 'Start'
			
	def quitter(self):
		p = QuitPopup()
		p.open()


####
class AlienStory(App):
	def build(self):
		alsc = AlienScreens()
		return alsc
		
if __name__ == "__main__":
	AlienStory().run()
