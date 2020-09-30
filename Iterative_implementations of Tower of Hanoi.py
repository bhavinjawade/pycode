#implementation of  Tower of Hanoi  using recursion

def Toh(num, source, destination, auxillary): 
	if num == 1: 
		print("Move disk 1 from rod", source, "to rod", destination)
		return
	Toh(num - 1, source, auxillary, destination) 
	print("Move disk", num, "from rod", source, "to rod", destination)
	Toh(num - 1, auxillary, destination, source) 
		
# Main code
num = int(input("Enter the number"))
Toh(num, 'A', 'C', 'B') 
# A, C, B are the name of rods 
# A is source rod, B is auxillary rod, C is destination rod