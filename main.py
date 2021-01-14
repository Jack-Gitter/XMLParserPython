from xmlparsermodel import Model
"""from xmlparserview import View"""

model = None 
while model == None: 
	try:
		filepath = input("please enter the absolute path of the XML file you wish to parse \n")
		model = Model(filepath)
		model.parseXMLHelper()
	except FileNotFoundError:
		print()
		print("the file path that you have enetered is invalid \n")

"""view = View()
view.dispW()"""