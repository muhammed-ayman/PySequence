#Adds a segment of DNA to an already-existing segment in a specific position that the user requires. If the user does not enter any position, the default position will be at the end of the already-existing strand. 
def ligate(toBeLigated,sequence,index):
	if index == -1:
		return sequence + toBeLigated
	else:
		return sequence[0:index] + toBeLigated + sequence[index:len(sequence)]
