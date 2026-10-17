import numpy as np
def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    centroid = []
    assignments = np.array(assignments)
    points = np.array(points)
    dim = points.shape[1] if points.size > 0 else 0
    for j in range(k):
        mask = (assignments == j)
        pointsj = points[mask]
        if len(pointsj)==0:
            centroid.append(np.zeros(dim).tolist())
        else:
            centroid.append(np.mean(pointsj , axis=0).tolist())
    return centroid
    pass