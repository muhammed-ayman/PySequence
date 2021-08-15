# Checks whether the strand is a palindrome or not. A palindrome is a string that is read backwards as read forwards (aattaa).
def is_palindrome(sequence):
	reversedSequence = sequence[::-1]
	if reversedSequence == sequence:
		return True
	else:
		return False
