from os import system

class app():
	def __init__(self, width=100, height=35, title="changeme"):
		self.setTitle(title)
		self.setSize(width, height)
		self.active = False
	
	def setTitle(self, newTitle):
		self.title = newTitle
		system("title " + str(self.title))
	
	def setSize(self, width, height):
		self.width = width
		self.height = height
		system("mode con: cols=" + str(self.width) + " lines=" + str(self.height))
