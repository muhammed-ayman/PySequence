from minimumEditDistance import minimum_edit_distance  # importing the minimum edit distance algorithm


def sequences_matching_percentage(seq_one, seq_two):  # getting two strings representing two sequences
    match_per = (len(seq_one) + len(seq_two)
                 - minimum_edit_distance(seq_one, seq_two)) * 100 \
        / (len(seq_one) + len(seq_two))
    return match_per  # returning the matching percentage between the two sequences
