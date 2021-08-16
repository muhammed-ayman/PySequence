def transcribe(sequence):                                   # getting a sequence of DNA
    correspond = {'T': 'A', 'C': 'G', 'A': 'U', 'G': 'C'}   # defining a dictionary for corresponding nucleotides
    seq_ = ''                                               # an empty str to hold the transcribed strand
    for i in sequence:
        seq_ += correspond[i.upper()]
    return seq_                                             # returning the transcribed strand

