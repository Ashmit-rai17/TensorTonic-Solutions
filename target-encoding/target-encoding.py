def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    dict = {}
    ctr = {}
    for item in categories:
        dict[item] = 0
        ctr[item] = 0
    for item in categories:
        ctr[item] += 1
    for i in range(0 , len(categories)):
        dict[categories[i]] += targets[i]
    for i in range(0 , len(categories)):
        categories[i] = dict[categories[i]] / ctr[categories[i]]
    return categories
    # Write code here
    pass