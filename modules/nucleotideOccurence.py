#Calculates the number of occurrence of each nucleotide within a strand of DNA and store them in a list.
def number_of_each_nucleotide(sequence):
	counterG, counterC, counterT, counterA = 0,0,0,0
	for i in range(len(sequence)):
		if sequence[i] == "g" or sequence[i] == "G":
			counterG += 1
		elif sequence[i] == "c" or sequence[i] == "c":
			counterC += 1
		elif sequence[i] == "t" or sequence[i] == "T":
			counterT += 1
		else:
			counterA += 1
	numbers = [counterG,counterC,counterT,counterA]
	return numbers


#Calculates the percentage of occurence of each nucleotide within a strand of DNA and store them in a list
def percentage_of_each_nucleotide(sequence):
	percentageOfG = (number_of_each_nucleotide(sequence)[0]/len(sequence)) * 100; percentageOfC = (number_of_each_nucleotide(sequence)[1]/len(sequence)) * 100; percentageOfT = (number_of_each_nucleotide(sequence)[2]/len(sequence)) * 100; percentageOfA = (number_of_each_nucleotide(sequence)[3]/len(sequence)) * 100
	percentages = [round(percentageOfG,2),round(percentageOfC,2),round(percentageOfT,2),round(percentageOfA,2)]
	return percentages
