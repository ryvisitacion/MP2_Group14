import pyglet
import random

class GameState:
	def __init__(self, saveFile = None):
		self.saveFile = savefile if saveFile is not None else 'init'
		self.dataFileCount = int()
		self.cumulativeDataFileCount = int()
		self.cashCount = int()
		self.cumulativeCashCount = int()
		self.bitcoinCount = int()
		self.collectorCount = int()
		self.databaseCount = int()
		self.laundromatCount = int()
		self.attributeList = [self.dataFileCount, self.cumulativeDataFileCount, self.cashCount, self.bitcoinCount,
self.collectorCount, self.databaseCount, self.laundromatCount]
		self.cashInDataVisible = False
		self.hireCollectorVisible = False
		self.hireLaundromatVisible = False
		self.buyBitcoinVisible = False
		self.sellBitcoinVisible = False
		self.arrestChance = 0

	def checkVisiblity(self):
		if self.dataFileCount >= 10:
			self.cashInDataVisible = True
		if self.cashCount >= 100:
			self.hireCollectorVisible = True
		if self.cashCount >= 50:
			self.hireLaundromatVisible = True
		if self.cashCount >= 5000:
			self.buyBitcoinVisible = True
		if self.bitcoinCount > 0:
			self.sellBitcoinVisible = True

	def loadSaveData(self):
		save = open(self.saveFile + '.txt', 'r')
		saveData = save.readlines()
		saveData = [x.strip() for x in saveData]
		for i in range(len(saveData)):
			self.attributeList[i] = saveData[i]
		checkVisiblity

	def collectData(self):
		self.dataFileCount += 1
		self.cumulativeDataFileCount += 1
		print("dataFileCount: {}".format(self.dataFileCount))
		self.checkVisiblity()
		
	def cashInData(self):
		if self.dataFileCount < 10:
			return
		self.dataFileCount -= 10
		n = 0
		database_modifier = self.databaseCount * 0.1
		success_chance = round(random.uniform(0.45, 0.55)) + database_modifier
		for _ in range(10):
			c = round(random.random())
			if c <= success_chance:
				n += 250
		self.cashCount += n
		self.cumulativeCashCount += n
		self.checkVisiblity()
		print("cashCount: {}".format(self.cashCount))
	
	def hireCollector(self):
		if self.cashCount < 100:
			return
		self.collectorCount += 1
		self.cashCount -= 100
	
	def hireLaundromat(self):
		if self.cashCount < 50:
			return
		self.cashCount -= 50
		self.laundromatCount += 1
	
	def buyBitcoin(self):
		if self.cashCount < 5000:
			return
		self.cashCount -= 5000
		self.bitcoinCount += 1
		self.checkVisiblity()
	
	def sellBitcoin(self):
		if self.bitcoinCount < 1:
			return
		self.bitcoinCount -= 1
		self.cashCount += 5000

	def update(self):
		self.dataFileCount += (1 * self.collectorCount)
		self.cumulativeDataFileCount += (1 * self.collectorCount)
		if self.collectorCount > 0:
				self.cashCount -= (10 * self.collectorCount)
		if self.cumulativeDataFileCount > 100:
			if self.cashCount > 3000 or self.cashCount < 0:
				if self.cashCount > 0:
					self.arrestChance = (0.1 * ((self.cashCount - 3000) // 1000)) - (self.laundromatCount * 0.05)
				if self.cashCount < 0:
					self.arrestChance = (0.2 * (self.cashCount // -100)) - (self.laundromatCount * 0.05)

	def calcScore(self):
		score = self.cumulativeCashCount + self.cumulativeDataFileCount
		return score