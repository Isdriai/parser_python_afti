from section import section
import struct

class fat32Directory(section):
	"""docstring for fat32Directory"""

	def getFormatX(self, x):
		return [
		# C'est le format pour une entrée de fichier
		("DIR_Name"+str(x), "11s"),
		("DIR_Attr"+str(x), "B"),
		("DIR_NTRes"+str(x), "B"),
		("DIR_CrtTimeTenth"+str(x), "B"),
		("DIR_CrtTime"+str(x), "H"),
		("DIR_CrtDate"+str(x), "H"),
		("DIR_LstAccDate"+str(x), "H"),
		("DIR_FstClusHI"+str(x), "H"),
		("DIR_WrtTime"+str(x), "H"),
		("DIR_WrtDate"+str(x), "H"),
		("DIR_FstClusLO"+str(x), "H"),
		("DIR_FileSize"+str(x), "I")
		]

	def getKeys(self):
		return getFormatX(self, self.nbrEntry)


	def getTailleFormat(self):
		return struct.calcsize(self.fmt())

	def pre_parse(self):
		self.file.seek(self.start)
		pre_format="11s"
		dotFile = magic_string = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0].decode('UTF-8')
		
		# 10 espaces apres le point
		if dotFile != ".          ":
			raise NameError('Parsing failed ')

		# fmt() va donner le format pour une entrée
		self.file.seek(self.start+getTailleFormat(self))
		pre_format="11s"
		dotdotFile = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0].decode('UTF-8')
		
		# 10 espaces apres le point
		if dotdotFile != "..         ":
			raise NameError('Parsing failed ')

	def anotherEntry(self):
		self.file.seek(self.start)
		pre_format="b"
		return struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format))) != 0x00:
			
	def parse(self):
		self.nbrEntry=0
		while True:
			super(self)
			self.nbrEntry++
			self.start+=getTailleFormat(self)
			anotherEntry(self) ? : break

	def __init__(self, name, start):
		super().__init__(name, start)