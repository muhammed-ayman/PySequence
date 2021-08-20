#Takes the user's entered RNA sequence and changes it into a DNA sequence by replacing each "u"" with a "t"
def reverse_transcriptase(rna_sequence):
	return rna_sequence.replace("U","T")