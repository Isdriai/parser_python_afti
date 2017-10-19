from section import section
import struct

class mbr(section):
	"""docstring for mbr"""

	keys = [
		("Routine", "440s"),
		("Signature", "I"),
		("Padding", "H"),
		("Boot1", "B"),
		("CHSfirst1", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("Type1", "B"),
		("CHSlast1", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("LBA1", "I"),
		("NBRsector1", "I"),

		("Boot2", "B"),
		("CHSfirst2", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("Type2", "B"),
		("CHSlast2", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("LBA2", "I"),
		("NBRsector2", "I"),

		("Boot3", "B"),
		("CHSfirst3", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("Type3", "B"),
		("CHSlast3", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("LBA3", "I"),
		("NBRsector3", "I"),

		("Boot4", "B"),
		("CHSfirst4", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("Type4", "B"),
		("CHSlast4", "3s"), # pas grave si c'est un string, c'est un champ obsolete
		("LBA4", "I"),
		("NBRsector4", "I")
	]

	def getKeys(self):
		return mbr.keys

	def pre_parse(self):
		self.file.seek(self.start+struct.calcsize(self.fmt()))
		pre_format="H"
		magic_number = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0]
		
		if magic_number != 0xaa55:
			raise NameError('Parsing failed ' + str(magic_number))
	
	def __init__(self, name, start):
		super().__init__( name,start)