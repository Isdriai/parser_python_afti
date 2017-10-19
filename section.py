import struct

class section(object):
	"""docstring for section"""

	def fmt(self):
		acc = "="
		for key in self.getKeys():
			acc += key[1]
		return acc
		
	def getKeys(self):
		raise NameError("veuillez définir cette méthode, elel doit renvoyer un dictionnaire")
		
	def pre_parse(self):
		print("veuillez redefinir la fonction de pre parsage, si elle rencontre un probleme, elle doit renvoyer un NameError(\"\"")

	def parse(self):
		self.file.seek(self.start)
		stream = self.file.read(struct.calcsize(self.fmt()))
		datas = struct.unpack(self.fmt(), stream).__iter__()
		for key, _ in self.getKeys():
			self.infos[key]= datas.__next__()

	def __init__(self, name, start):
		self.file = open(name, "rb")
		self.start = start
		self.infos = {}
		self.pre_parse()
		self.parse()
		