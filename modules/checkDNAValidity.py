def check_DNA_validity(DNA):                        # gets a DNA sequence as a string input
    possible_nucleotides = 'ACGT'
    DNA = DNA.replace(" ", "")
    for i in DNA:
        if i.upper() not in possible_nucleotides:
            return False
    return DNA.upper()                              # returning the DNA sequence after doing some repairs
