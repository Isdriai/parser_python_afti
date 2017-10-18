class mbr(object):
	"""docstring for mbr"""

	def verification(self):
		return self.magic_number == 0xaa55 

	def __init__(self, stream):
		super(mbr, self).__init__()
		
		