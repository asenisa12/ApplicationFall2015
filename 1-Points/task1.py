def main():
	x = int(input("input x: "))
	y = int(input("input y: "))
	wraping = 1

	for a in input("write the string: "):
		if(a=='>'):
			x+=wraping*1
		elif(a=='<'):
			x-=wraping*1
		elif(a=='v'):
			y-=wraping*1
		elif(a=='^'):
			y+=wraping*1
		elif(a=='~'):
			wraping=-1

	print("x: "+str(x)+"y: "+str(y))


if __name__ == '__main__':
	main()