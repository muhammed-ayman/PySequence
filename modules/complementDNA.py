#Takes the user's entered sequence and calculates its complementary strand
def complement_DNA(sequence):
	complementarySeq = ""
	for i in range(len(sequence)):
		if sequence[i] == "G" or sequence[i] == "g":
			complementarySeq += "c"
		elif sequence[i] == "C" or sequence[i] == "c":
			complementarySeq += "g"
		elif sequence[i] == "T" or sequence[i] == "t":
			complementarySeq += "a"
		else:
			complementarySeq += "t"
	return complementarySeq


#Takes the output of the complement function and reverses it
def reverse_complement(sequence):
	return complement(sequence)[::-1]
