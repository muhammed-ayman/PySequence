#Adds a segment of DNA to an already-existing segment in a specific position that the user requires. If the user does not enter any position, the default position will be at the end of the already-existing strand. 
def ligate(toBeLigated,sequence,index=None):
	if index is not None:
		return sequence[0:index] + toBeLigated + sequence[index:len(sequence)-1]
	else:
		return sequence + toBeLigated
