#Adds a segment of DNA to an already-existing segment in a specific position that the user requires. If the user does not enter any position, the default position will be at the end of the already-existing strand. 
def ligate(toBeLigated,sequence,index):
	if index == -1:
		return sequence.upper() + toBeLigated.upper()
	else:
		return sequence[0:index].upper() + toBeLigated.upper() + sequence[index:len(sequence)].upper()

print(ligate("gg","atagtccgaaggctag",-1))
