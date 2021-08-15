#Searches whether a certain segment is found within a DNA strand or not
def restriction_enzyme(sequence,site):
	searchingSegment = sequence.find(site)
	if searchingSegment == -1:
		return False
	else:
		return True