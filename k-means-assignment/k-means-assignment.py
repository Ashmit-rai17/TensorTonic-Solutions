def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    lst = []
    for point in points:
        min_index = -1 
        min_dist = float('inf')
        for i , centroid in enumerate(centroids):
            res = sum((p - c) ** 2 for p, c in zip(point, centroid))
            if res < min_dist:
                min_dist = res
                min_index=i
        lst.append(min_index)
    return lst
    pass