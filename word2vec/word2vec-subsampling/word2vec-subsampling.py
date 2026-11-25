import torch

def subsample_keep_probs(counts: torch.Tensor,
                         t: float = 1e-5) -> torch.Tensor:
    """
    Returns the float64 keep probability for every vocabulary word.
    """
    f = counts/counts.sum()
    x = torch.sqrt(t/f)
    return x.clamp(max=1.0)
    pass