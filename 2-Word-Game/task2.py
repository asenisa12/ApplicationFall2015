import sys
import os

tableData = []
tableRows = []
wordLen =0

def parseFile(name,x,y):
	with open(name, encoding='utf-8') as f:
		tableData = f.readlines()
		f.close()
		if len(tableData)<y:
			print("Error: incorect sizeY!")
			return False

		for elem in tableData:
			if len(elem.strip("\n"))<x:
				print("Error: incorect sizeX!")
				return False
			tableRows.append(list(elem[:x]))
			if elem == tableData[y-1]:
				break
			

		return True
	return False

def printTable():
	for elem in tableRows:
		for char in elem:
			end_ = ''
			if(char == elem[-1]):
				end_ ='\n'
			print("["+char+"]",end = end_)


def getDiagonals(x,y, oposite):
	range1 = range(0,y)
	if oposite:
		range1 = reversed(range1)

	diagonals = []
	size = x
	for i in range1:
		if size<wordLen:
			break
		diagonal = []
		i_ = i
		for j in range(0,size):
			diagonal.append(tableRows[i_][j])
			if oposite:
				i_-=1
			else:
				i_+=1

			if i_<0 or i_>y-1:
				size-=1
				break
		diagonals.append(diagonal)

	size = x-1
	for i in range(1,x):
		i_ = i
		if size<wordLen:
			break	
		diagonal = []

		range2 = range(0,size)
		if oposite:
			range2 = reversed(range(0,y))

		for j in range2:
			diagonal.append(tableRows[j][i_])
			i_+=1
			if i_>x-1:
				break
		size-=1
		diagonals.append(diagonal)

	return diagonals		

def getVertical(x,y):
	cols = []
	for i in range(0,x):
		col = []
		for j in range(0,y):
			col.append(tableRows[j][i])
		cols.append(col)

	return cols

def countWord(wordName, x,y):
	possibleRows = tableRows
	possibleRows += getDiagonals(x,y, True)+getDiagonals(x,y, False)
	possibleRows += getVertical(x,y)
	count = 0
	for elem in possibleRows:
		row = ''.join(elem)
		if wordName in row:	
			count+=1
		elif wordName[::-1] in row:
			count+=1

	print(str(count))
	return count

def main():
	fileName = ""
	hasError = False

	if len(sys.argv)>1:
		fileName = sys.argv[1]
		if os.path.isfile(fileName)==False:
			print("Error: file '"+fileName+"' dont exist!")
		else:
			sizeX = int(input("input x size: "))
			sizeY = int(input("input y size: "))

			if parseFile(fileName,sizeX,sizeY):
				printTable()
				word = str(input("input word: "))
				global wordLen
				wordLen = len(word)
				wordCount = countWord(word,sizeX,sizeY)
	else:
		print("Error: file name is not input!")



if __name__ == '__main__':
	main()