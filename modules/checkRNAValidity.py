def check_RNA_validity(RNA):                        # gets a RNA sequence as a string input
    possible_nucleotides = 'ACGU'
    RNA = RNA.replace(" ", "")
    for i in RNA:
        if i.upper() not in possible_nucleotides:
            return False
    return RNA.upper()                              # returning the RNA sequence after doing some repairs
