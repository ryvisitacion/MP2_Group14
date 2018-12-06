import pyglet
'''
a word on how time works in this game:
 
for ease of calculations, and cause we can create
a fictional universe where this story takes place,
each week has 7 days, each month has 4 weeks,
meaning each month has 28 days only. one year 
would have 13 months,
referred to as month 1, month 2, etc...
this implies that each year has 364 days.
 
'''
 
class gameTimeData:
	'''
	by default, gameTimeData should start on
	day 1, week 1, month 1, year 1
	when loading a save file, the day, month, and year 
	should be stored in the file, so it can be loaded
	into gameTimeData
	'''
	def __init__(self, day, week, month, year): 
		self.day = day
		self.week = week
		self.month = month
		self.year = year
	
	def addYear(self):
		self.year += 1
	
	def addMonth(self):
		if self.month <= 13:
			self.month += 1
		if self.month > 13:
			self.month = 1
			self.addYear()
	
	def addWeek(self):
		if self.week <= 4:
			self.week += 1
		if self.week > 4:
			self.week = 1
	
	def addDay(self):
		if self.day <= 28:
			self.day += 1
		if self.day % 7 == 1:
			self.addWeek()
		if self.day > 28:
			self.day = 1
			self.addMonth()
		#print("Day is now {}".format(self.day))