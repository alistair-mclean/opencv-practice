

__version__ = '1.0'

from kivy.app import App #For the main application
from kivy.uix.floatlayout import FloatLayout #the UI Layout
from kivy.uix.label import Label #a lable to display information
from plyer import camera


class UI(FloatLayout): #the app ui
	def __init__(self, **kwargs):
		super(UI,self).__init__(**kwargs)
		self.lblCam = Label(text="Click to take a picture!") #Create a label at the center
		self.add_widget(self.lblCam) #add the label at the screen 

	def on_touch_down(self, e):
		camera.take_picture('/storage/sdcard0/example.jpg',self.done)

	def done(self, e): #receive image e as
		self.lblCam.text = e; #

class Camera(App): 
	def build(self):
		ui = UI() #create the UI
		return ui #display it

	def on_pause(self):
		#When the app opens the camera, it will need to pause the script. So we enable the pause mode with this method 
		return True

	def on_resume(self):
		#After, close the camera, we need to resume our app. 
		pass
Camera().run()