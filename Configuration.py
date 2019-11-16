import json


class Configuration:

	def __init__(self, filename="./config.json"):
		'''
			self.node - url to IOTA IRI node
			self.seed - IOTA Seed of the device
			self.secLvl - security level
			self.checksum - boolean
			self.uiPath - path for UI specification file
			self.jsonPath - path for the "usedAddresses" json file
			self.qrPath - path for the qr code png
			self.price - price in iota for each second of usage/electricity
			self.owner - address of the device owner
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
			self.uiPath = c["UiPath"]
			self.jsonPath = c["jsonPath"]
			self.qrPath = c["qrCodePath"]
			self.price = c["price"]
			self.owner = c["Owner"]

	def getNodeUrl(self):
		return self.node
		
	def getSeed(self):
		return self.seed
		
	def getSecLvl(self):
		return self.secLvl
		
	def getChecksum(self):
		return self.checksum
		
	def getUiPath(self):
		return self.uiPath

	def getJsonPath(self):
		return self.jsonPath

	def getQrPath(self):
		return self.qrPath

	def getPrice(self):
		return self.price

	def getOwner(self):
		return self.owner

