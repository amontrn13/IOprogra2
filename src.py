import sys

def readFile(file):
	file_object  = open(file, 'r')
	for line in file_object:
		print(line)
	file_object.close()

def main():
	
	print("\r\n\r\n\r\n\r\n")
	print("--------------------------\n--------------------------")
	print("-Sorting Data:-")
	print("--------------------------\n--------------------------\r\n")
	readFile(sys.argv[1])


if __name__ == "__main__":
	main()