import sys
sys.path.append('C:/Users/Ahmed/Documents/GitHub/CSCI-101-Project/modules')
from checkDNAValidity import check_DNA_validity
from checkRNAValidity import check_RNA_validity
from nucleotideOccurence import number_of_each_nucleotide
from nucleotideOccurence import percentage_of_each_nucleotide
from complementDNA import complement_DNA
from complementDNA import reverse_complement
from cgContent import cg_content
from IsPalindrome import is_palindrome
from Ligate import ligate
from restrictionEnzyme import restriction_enzyme
from shortTandemRepeat import STPs
from reverseTranscriptase import reverse_transcriptase
import time

def mainInterface():
	print("Hello! This is a software that helps you analyze DNA & RNA strands\n")
	print("You can also  translate DNA & RNA strands to the corresponding polypeptide chain!\n")
	time.sleep(2)
	mainChoice = input("To analyze DNA & RNA strands, press 1. To proceed with the central dogma process, press 2. \n")
	while not (mainChoice == "1" or mainChoice == "2"):
		print("\nThere is an error...")
		time.sleep(1)
		mainChoice = input("To analyze DNA & RNA strands, press 1. To proceed with the central dogma process, press 2. \n")
	return int(mainChoice)

def Analyze():
	print("\nHello again! Now you are doing excellent analysis job!\n")
	print("Do you want single strand analysis or multi-strand analysis?\n")
	singleOrMultiChoice = input("For Single, press 1. For Multi, press 2. \n")
	while not (singleOrMultiChoice == "1" or singleOrMultiChoice == "2"):
		print("\nThere is an error...")
		time.sleep(1)
		singleOrMultiChoice = input("For Single, press 1. For Multi, press 2.\n")
	return int(singleOrMultiChoice)
def centralDogma():
	print("\nHello again! Now you are doing excellent gene-to-protein job!\n")
	print("Do you want to work with RNA or DNA?\n")
	RNAOrDNA = input("For RNA, press 1. For DNA, press 2. \n")
	while not (RNAOrDNA == "1" or RNAOrDNA == "2"):
		print("\nThere is an error...")
		time.sleep(1)
		RNAOrDNA = input("For RNA, press 1. For DNA, press 2.\n")
	return int(RNAOrDNA)

def singleStrandAnalysis():
	print("This is the list of features accessible to you: ")
	print("For counting the number of nucleotides and finding their percentage, press 1.\n For finding the complementary strand, press 2. \n For finding the G-C content press 3. \n For checking whether the strand is a palindrome or not, press 4. \n For ligating a segment withing the strand, press 5. \n To search whether a certain segment is found or not, press 6. \n For counting the number of times a segment occurs withing the strand, press 7.\n For finding the reverse of the complementary strand, press 8.\n For Reverse Transcriptase, press 9.\n")
	featureChoice = input("Enter your choice here: ")
	while not (featureChoice == "1" or featureChoice == "2" or featureChoice == "3" or featureChoice == "4" or featureChoice == "5" or featureChoice == "6" or featureChoice == "7" or featureChoice == "8" or featureChoice == "9"):
		print("\nThere is an error...\n")
		time.sleep(1)
		featureChoice = input("Enter your choice here: ")
	if featureChoice == "9":
		rnaSeq = input("Enter your RNA sequence here: \n")
		while check_RNA_validity(rnaSeq) == False:
			rnaSeq = input("Error! Enter your RNA sequence: \n")
		return rnaSeq, int(featureChoice)
	else:
		dnaSeq = input("Enter your DNA Sequence here: ")
		while check_DNA_validity(dnaSeq) == False:
			dnaSeq = input("Error! Enter your DNA sequence: \n")
		return dnaSeq, int(featureChoice)

def multiStrandAnalysis():
	print("hi from multi strand analysis!")
	# Do the sort of stuff related to multi strand analysis here.

def singleStrandFeaturesDNA (dnaseq,feature):
	if feature == 1:
		print("Your nucleotide occurrence in the strand is: [g,c,t,a]")
		print(number_of_each_nucleotide(dnaseq))
		time.sleep(1)
		print("Their percentages are: ",percentage_of_each_nucleotide(dnaseq))
	elif feature == 2:
		print("Your complementary strand is: ",complement_DNA(dnaseq))
	elif feature == 3:
		print("The G-C content in your strand is: ",cg_content(dnaseq))
	elif feature == 4:
		if is_palindrome(dnaseq) == True:
			print("Your strand is a palindrome!")
		else:
			print("Your strand is NOT a palindrome!")
	elif feature == 5:
		segmentToBeLigated = input("What do you want to ligate? ")
		while check_DNA_validity(segmentToBeLigated) == False:
			segmentToBeLigated = input("Error! Enter your to-be ligated segment: \n")
		index = int(input("After nucleotide number what do you want to add your segment? If at the end, write -1: "))
		while index > len(dnaseq) or (index < 0 and index != -1):
			index = int(input("After nucleotide number what do you want to add your segment? If at the end, write -1: "))
		print("Your segment after ligation is: ",ligate(segmentToBeLigated,dnaseq,index))
	elif feature == 6:
		searchSegment = input("What segment do you want to search for? ")
		while check_DNA_validity(searchSegment) == False:
			searchSegment = input("Error! What segment do you want to search for? ")
		if restriction_enzyme(dnaseq,searchSegment) == True:
			print("Your segment exists in the strand! ")
		else:
			print("Sorry! Your segment does not exist in the strand! ")
	elif feature == 7:
		countSegment = input("What is the segment do you want to find its count in the string? ")
		while check_DNA_validity(countSegment) == False:
			countSegment = input("What is the segment do you want to find its count in the string? ")
		print("The segment you entered occurs ",STPs(dnaseq,countSegment)," times!")
	elif feature == 8:
		print("The reverse of the complement of your enetred strand is: ",reverse_complement(dnaseq))


def singleStrandFeaturesRNA(rnaseq):
		print("Your DNA strand from your entered RNA strand is: ",reverse_transcriptase(rnaseq))

if mainInterface() == 1: 
	if Analyze() == 1:
		callSingleStrandAnalysis = singleStrandAnalysis()
		if callSingleStrandAnalysis[1] == 9:
			singleStrandFeaturesRNA(callSingleStrandAnalysis[0])
		else:
			singleStrandFeaturesDNA(callSingleStrandAnalysis[0], callSingleStrandAnalysis[1])
	else:
		multiStrandAnalysis()

else: 
	if centralDogma() == 1:
		print("hi from RNA central dogma")
	else:
		print("hi from DNA central dogma")