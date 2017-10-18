import struct
import functools
import pdb

class FAT32:

	keys = [
		("BS_jmpBoot1", "B"),
		("BS_jmpBoot2", "B"),
		("BS_jmpBoot3", "B"),
		("BS_OEMName", "Q"),
		("BPB_BytsPerSec", "H"),
		("BPB_SecPerClus", "B"),
		("BPB_RsvdSecCnt", "H"),
		("BPB_NumFATs", "B"),
		("BPB_RootEntCnt", "H"),
		("BPB_TotSec16", "H"),
		("BPB_Media", "B"),
		("BPB_FATSz16", "H"),
		("BPB_SecPerTrk", "H"),
		("BPB_NumHeads", "H"),
		("BPB_HiddSec", "I"),
		("BPB_TotSec32", "I"),
		("BPB_FATSz32", "I"),
		("BPB_ExtFlags", "H"),
		("BPB_FSVer", "H"),
		("BPB_RootClus", "I"),
		("BPB_FSInfo", "H"),
		("BPB_BkBootSec", "H"),
		("BPB_Reserved", "12s"), 
		("BS_DrvNum", "B"),
		("BS_Reserved1", "B"),
		("BS_BootSig", "B"),
		("BS_VolID","I"),
		("BS_VolLab", "11s") 
	]

	def fmt():
		acc = "="
		for key in FAT32.keys:
			acc += key[1]
		return acc


	## Regarde si l'attribue start est bien insiqué, si ce n'est pas le cas, il n'arrivera pas à parser par la suite,
	## pour ne pas perdre trop de temps, on essaye juste de récupérer des éléments qu'on connait
	def pre_parse(self):
		## le magic number se trouve 420 bytes apres les informations que l'on va parser,
		## pour le 8c, c'est la taille du nom qui est traiter de facon particuliere
		print(self.start+struct.calcsize(FAT32.fmt()+"8c420x"))
		self.file.seek(self.start+struct.calcsize(FAT32.fmt()+"8c420x"))
		pre_format="H"
		magic_number = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0]
		
		if magic_number != 0xaa55:
			raise NameError('Parsing failed ' + str(magic_number))

		self.file.seek(self.start+struct.calcsize(FAT32.fmt()))
		pre_format="8c"
		magic_string = b''.join(struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))).decode('UTF-8')
		if magic_string != "FAT32   ":
			raise NameError('Parsing failed ' + magic_string)
		self.infos["MAGIC_NUMBER"]=magic_number
		self.infos["MAGIC_STRING"]=magic_string

	def parse(self):
		self.file.seek(self.start)
		stream = self.file.read(struct.calcsize(FAT32.fmt()))
		datas = struct.unpack(FAT32.fmt(), stream).__iter__()
		pdb.set_trace()
		for key, _ in FAT32.keys:
			self.infos[key]= datas.__next__()

	def __init__(self, name, start):
		super(FAT32, self).__init__()
		self.file = open(name, "rb")
		self.start = start
		self.infos = {}
		self.pre_parse()
		self.parse()