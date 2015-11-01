import json
import os
 
modulesFile = None
installedPack = []
notInstalledPack = []

def readDepen(name, data):
	dependencies = data[name]
	notInstalledPack.append(name)
	packsList = []

	print("installing "+name)  

	if((not dependencies)==False):
		depMessage = "In order to install "+str(name)+\
		", we need"

		for elem in dependencies:
			if((elem in installedPack)==False):
				packsList.append(elem)


		if packsList:	
			for elem in packsList:
				if(elem != packsList[0]):
					if(elem == packsList[-1]):
						depMessage+=" and"
					else:
						depMessage+=", "

				depMessage+=(" "+elem)
	 
			print(depMessage)
                       
		for elem in packsList:
			readDepen(elem, data)


def installedPackNames():
	names=[]

	if os.path.isfile('installed_modules'):
		with open('installed_modules', encoding='utf-8') as f:
			lines = f.readlines()
			if(os.stat("installed_modules").st_size > 0):
				lines.pop(0)

			for elem in lines:
				names.append((elem[4:].strip('\n')))
			f.close()
	else:
		modulesFile = open('installed_modules','a')
		modulesFile.close()

	return names
               
 
def parseJSON(fname):
        jsonFile = open(fname)
        data = json.loads(jsonFile.read())
        jsonFile.close()
        return data

def addInstalledPacks():
	with open('installed_modules',"w+", encoding='utf-8') as f:
		f.seek(0)
		f.truncate()
		all_packages = installedPack+notInstalledPack 

		f.write("installed_modules/\n")
		for elem in all_packages:
			line = ""
			if(elem == all_packages[-1]):
				line+="└── "
			else:
				line+="├── "
			line+=elem
			f.write(line+"\n")

		f.close()
 
def main():
	packages = parseJSON("all_packages.json")
	dep = parseJSON("dependencies.json")

	installedPack = installedPackNames()
 
	for module in dep["dependencies"]:
		if((module in installedPack)==False):
			readDepen(module, packages)

	if notInstalledPack:
		addInstalledPacks()

	print("All done!")

if __name__ == '__main__':
	main()