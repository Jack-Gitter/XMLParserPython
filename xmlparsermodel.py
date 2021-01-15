import xml.etree.ElementTree as ET

class Model():

	def __init__(self, XMLFilePath):
		self.XMLFilePath = XMLFilePath
		self.tree = ET.parse(open(self.XMLFilePath))
		self.root = self.tree.getroot()
		self.file = open(self.XMLFilePath[0:len(self.XMLFilePath)-4] + "_PARSED.txt", "w")

	def parseXMLHelper(self):
		self.parseXML(self.root, [], 0)

	def parseXML(self, root, seenElems, tabCounter):
 
			if len(list(root)) == 0:
				if root not in seenElems:
					for i in range(0, tabCounter):
						self.file.write("\t")
					self.file.write(root.tag + ": " + root.text + "\n")
					seenElems.append(root)
			else: 
				if (root not in seenElems):
					for i in range(0, tabCounter):
						self.file.write("\t")
					self.file.write(root.tag + ": " + root.text)
					tabCounter+=1

				for i in range(0, len(list(root))):
					for j in range(0, tabCounter):
						self.file.write("\t")
					if list(root)[i] not in seenElems:
						self.file.write(list(root)[i].tag + ": " + list(root)[i].text + "\n")
						seenElems.append(list(root)[i])
					self.parseXML(list(root)[i], seenElems, tabCounter+1)


			


