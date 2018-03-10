class Network(object):
	def __str__(self):
		return "I am a __str__ "
	def __repr__(self):
		return "I am a __repr__ "
if __name__ == '__main__':
	mtd = Network()
	print (mtd)
	print (mtd.__repr__())
