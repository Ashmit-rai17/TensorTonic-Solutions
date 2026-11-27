import torch

def noise_distribution(counts: torch.Tensor,
                       alpha: float = 0.75) -> torch.Tensor:
    """
    Returns the float64 negative-sampling distribution over the vocabulary.
    """
    counts = counts**alpha
    return counts / torch.sum(counts)
    pass