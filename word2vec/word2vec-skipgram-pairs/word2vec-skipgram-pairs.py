import torch

def skipgram_pairs(token_ids: torch.Tensor, window: int) -> torch.Tensor:
    """
    Returns the ordered center-context pairs as an int64 tensor.
    """
    res = []
    for i in range(len(token_ids)):
        for j in range(max(0 , i-window) , min(len(token_ids) , i+window+1)):
            if i != j:
                res.append([token_ids[i] , token_ids[j]])
    if len(res) == 0:
        return torch.empty((0,2) , dtype = torch.int64)
    else:
        return torch.tensor(res , dtype = torch.int64)
    pass