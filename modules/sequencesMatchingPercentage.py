from minimumEditDistance import minimum_edit_distance  # importing the minimum edit distance algorithm


def sequences_matching_percentage(seq_one, seq_two):  # getting two strings representing two sequences
    edit_distance = minimum_edit_distance(seq_one, seq_two)
    max_length = max(len(seq_one), len(seq_two))
    match_per = 100*(1-edit_distance/max_length)
    return match_per  # returning the matching percentage between the two sequences
