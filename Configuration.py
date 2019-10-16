import json

class Configuration:

	def __init__(self, filename="./node_config.json"):
		'''
			self.node - url to IOTA IRI node
			self.seed
			self.secLvl - security level
			self.checksum - boolean
		'''
		self.silent = False
		self.load(filename)

	def load(self, filename):
		with open(filename, "r") as f:
			c = json.load(f)
			if not self.silent:
				print("Loaded configuration:", c)
			self.node = c["Node"]
			self.seed = c["Seed"]
			self.secLvl = c["SecurityLevel"]
			self.checksum = c["CheckSum"]

	def getNodeUrl(self):
		return self.node
		
	def getSeed(self):
		return self.seed
		
	def getSecLvl(self):
		return self.secLvl
		
	def getChecksum(self):
		return self.checksum
		
	def setNodeUrl(self, n):
		self.node = n
		
	def setSeed(self, s):
		self.seed = s
		
	def setSecLvl(self, lvl):
		self.secLvl = lvl
		
	def setChecksum(self, c):
		self.checksum = c
