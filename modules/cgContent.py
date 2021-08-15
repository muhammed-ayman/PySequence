#Calculates the G-C content of a DNA strand
from nucleotideOccurence import percentage_of_each_nucleotide

def cg_content(sequence):
	gContent = percentage_of_each_nucleotide(sequence)[0]
	cContent =percentage_of_each_nucleotide(sequence)[1]
	cgPercentage = round(gContent + cContent,2)
	return cgPercentage
