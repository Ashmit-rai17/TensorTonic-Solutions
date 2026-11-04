from collections import Counter
def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    n_trees = len(predictions)
    n_samples = len(predictions[0])
    majority_vote = []
    for j in range(n_samples):
        sample_preds = [predictions[i][j] for i in range(n_trees)]
        common = Counter(sample_preds)
        max_val = max(common.values())
        tied_label = [label for label , count in common.items() if count == max_val]
        winner = min(tied_label)
        majority_vote.append(winner)
    return majority_vote
    pass