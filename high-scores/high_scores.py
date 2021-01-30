def latest(scores):
    """
    returns the last added score
    """
    return scores[-1]

def personal_best(scores):
    """
    returns the highest score from the list
    """
    return max(scores)

def personal_top_three(scores):
    """
    returns the three highest scores
    """
    return sorted(scores, reverse=True)[:3]