import struct

class section(object):
	"""docstring for section"""

	def fmt(self):
		fmt = "="
		for _, size in self.getKeys():
			fmt += size
		return fmt
		
	def getKeys(self):
		raise NameError("veuillez définir cette méthode, elel doit renvoyer un dictionnaire")
		
	def pre_parse(self):
		print("veuillez redefinir la fonction de pre parsage")

	def parse(self):
		#self.file.seek(self.start)
		#stream = self.file.read(struct.calcsize(self.fmt()))
		#datas = struct.unpack(self.fmt(), stream).__iter__()
		#for key, _ in self.getKeys():
		#	self.infos[key]= datas.__next__()
		offset = self.start
		for key, value in self.getKeys():
			self.file.seek(offset)
			size = struct.calcsize(value)
			stream = self.file.read(size)
			datas = struct.unpack(value, stream)[0]
			self.infos[key]= datas
			offset += size

	def __init__(self, name, start):
		self.file = open(name, "rb")
		self.start = start
		self.infos = {}
		self.pre_parse()
		self.parse()
		