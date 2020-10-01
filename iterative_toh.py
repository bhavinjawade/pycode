#! usr/bin/python3.1

from copy import deepcopy

"""
Solves a three-peg Towers of Hanoi problem. Constants
are hard-coded as the algorithm will break anyway if
used on a THP configuration with pegs != 3.

Convention:
	source peg is peg 0
	intermediate peg is peg 1
	destination peg is peg 2

@author Chad Estioco
"""

PEGS = ["source", "intermediate", "destination"]

def __is_solved(peg_set, disk_count):
	spam = list(range(disk_count))
	spam.reverse()
	solved_dest_state = list(map(lambda x: x + 1, spam))
	return len(peg_set[0]) == 0 and \
	       len(peg_set[1]) == 0 and \
	       len(peg_set[2]) == disk_count and \
	       peg_set[2] == solved_dest_state

def __move_smallest(leftwards, peg_set):
	"""
	Moves the smallest disk. If leftwards is True, smallest disk will
	move leftwards. Else, it moves rightwards. (Both assuming wrap-
	around condition.)
	"""
	i = 0
	
	while i < 3:
		peek_index = len(peg_set[i]) - 1
		if peek_index >= 0 and \
		   peg_set[i][peek_index] == 1:
			
			if leftwards:
				next_index = i - 1
				if next_index < 0:
					next_index = 2
			else:
				next_index = (i + 1) % 3
			
			peg_set[next_index].append(peg_set[i].pop())
			print("Move smallest peg to", PEGS[next_index])
			break
		
		i += 1

def __find_legal_peg(pegs, move_peg):
	"""
	Finds the peg to which we make a legal move with the topmost
	disk of move_peg.
	
	In reading this code, note that the peg-indexing conventions
	stated above doesn't apply for this section of the code.
	"""
	peg_set = deepcopy(pegs)
	disk = peg_set[move_peg][len(peg_set[move_peg]) - 1]
	# Remove move_peg temporarily (and hence peg-indexing conventions
	# will cease to apply...temporarily
	spam_peg = peg_set.pop(move_peg)
	top0 = len(peg_set[0]) - 1
	top1 = len(peg_set[1]) - 1
	
	if (top0 >= 0 and \
	    peg_set[0][top0] > disk) or top0 < 0:
		spam_peg0 = peg_set[0]
		peg_set.insert(move_peg, spam_peg)
		return peg_set.index(spam_peg0)
	else:
		spam_peg1 = peg_set[1]
		peg_set.insert(move_peg, spam_peg)
		return peg_set.index(spam_peg1)

def __legal_move(peg_set, disk_count):
	"""
	Makes a legal move on the given peg_set. We will use
	disk_count as the variable to remember the smallest
	peg not equal to 1.
	"""
	i = 0
	disk_count += 1
	smallest_disk_peg = 4
	
	#Find the smallest peg not equal to 1
	while i < 3:
		peek_index = len(peg_set[i]) - 1
		
		if peek_index >= 0 and \
		   peg_set[i][peek_index] != 1 and \
		   peg_set[i][peek_index] < disk_count:
			disk_count = peg_set[i][peek_index]
			smallest_disk_peg = i;
		
		i += 1
	
	legal_peg = __find_legal_peg(peg_set, smallest_disk_peg)
	move_disk = peg_set[smallest_disk_peg].pop()
	print("Move disk of size", move_disk, "from",
	      PEGS[smallest_disk_peg], "to", PEGS[legal_peg])
	peg_set[legal_peg].append(move_disk)

def solve(disk_count):
	"""Solves a Towers of Hanoi puzzle with n disks."""
	is_odd = (disk_count % 2) == 1
	spam = list(range(disk_count))
	spam.reverse()
	source = list(map(lambda x: x + 1, spam))
	peg_set = [source, [], []]
	__move_smallest(is_odd, peg_set)
	
	while not __is_solved(peg_set, disk_count):
		__legal_move(peg_set, disk_count)
		__move_smallest(is_odd, peg_set)

disk_count = int(input("Create a puzzle with how many disks? "))

while disk_count >= 3:
	solve(disk_count)
	disk_count = int(input("Create a puzzle with how many disks? "))
