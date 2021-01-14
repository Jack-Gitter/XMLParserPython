from xmlparsermodel import Model
import xml.etree.ElementTree as ET

model = None 
finished = False

while model == None or finished == False: 
	try:
		filepath = input("please enter the absolute path of the XML file you wish to parse \n")
		model = Model(filepath)
		model.parseXMLHelper()
		finished = True
	except FileNotFoundError:
		print()
		print("the file path that you have enetered is invalid \n")
	except ET.ParseError:
		print()
		print("the xml file you have inputted is not formatted correctly, please try again")
