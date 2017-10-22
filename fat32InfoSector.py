from section import section
import struct

class fat32InfoSector(section):
	"""docstring for mbr"""

	keys = [
		# La signature va etre parsée lors du pré parsage
		("FSI_LeadSig", "I"), 
		("FSI_Reserved1", "480s"),
		("FSI_StrucSig", "I"),
		("FSI_Free_Count", "I"),
		("FSI_Nxt_Free", "I"),
		("FSI_Reserved2", "12s"), # pas grave si c'est un string, c'est un champ inutilisé
		("FSI_TrailSig", "I")
	]

	def getKeys(self):
		return fat32InfoSector.keys

	def pre_parse(self):
		self.file.seek(self.start)
		pre_format="I"
		FSI_LeadSig = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0]
		
		if FSI_LeadSig != 0x41615252:
			raise NameError('Parsing failed ' + str(FSI_LeadSig))

		self.file.seek(self.start+struct.calcsize("I480s"))
		pre_format="I"
		FSI_StrucSig = struct.unpack(pre_format, self.file.read(struct.calcsize(pre_format)))[0]
		
		if FSI_StrucSig != 0x61417272:
			raise NameError('Parsing failed ' + str(FSI_StrucSig))

		# on enregistre ni FSI_StrucSig ni FSI_LeadSig car ce sera fait dans le parsage

	def __init__(self, name, start):
		super().__init__(name, start)