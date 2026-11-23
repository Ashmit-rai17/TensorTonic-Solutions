import numpy as np

def time_based_split(timestamps: list, train_end: int, gap: int, val_end: int) -> dict:
    """
    Returns a dictionary with train_idx and val_idx as sorted integer NumPy arrays.
    """
    timestamps = np.array(timestamps)
    train_idx = np.where(timestamps < train_end)[0]
    val_idx = np.where((timestamps >= train_end+gap) & (timestamps < val_end))[0]
    return {"train_idx" : train_idx , "val_idx" : val_idx}
    pass
