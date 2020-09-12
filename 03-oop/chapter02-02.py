

class Box:
	def  __init__(self, length, width, height):
		self.length = length;
		self.width = width;
		self.height = height

	def reset(self, length, width, height):
		self.length = length
		self.width = width
		self.height = height

	def volume(self):
		return self.length * self.width * self.height

	def dimensionsStr(self):
		return f"Length: {self.length}\tWidth: {self.width}\tHeight: {self.height}"

a = Box(1, 2, 3)
b = Box(2, 4, 6)

print('Box a volume: {}'.format(a.volume()))
print('Box b volume: {}'.format(b.volume()))

print('Box a dimensions: {}'.format(a.dimensionsStr()))
print('Box b dimensions: {}'.format(b.dimensionsStr	()))
