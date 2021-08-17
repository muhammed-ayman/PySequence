def generate_triplets(seq):                    # getting the sequence that is wanted to be sliced into triplets
    seq_ = []
    for i in range(0, len(seq), 3):
        if i + 3 < len(seq):
            seq_.append(seq[i:i+3].upper())
        else:
            seq_.append(seq[i:].upper())
    return seq_                                # returning a list of 3-char-strings(triplets)
