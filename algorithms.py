def insert_and_sort_top_scores(top_scores, new_score):
    new_scores_list = []
    inserted = False
    i = 0
    while i < 5:
        current_score = top_scores[i]
        if not inserted and new_score[1] < current_score[1]:
            new_scores_list += [new_score]
            inserted = True
        if len(new_scores_list) < 5:
            new_scores_list += [current_score]
        i += 1
    return new_scores_list
