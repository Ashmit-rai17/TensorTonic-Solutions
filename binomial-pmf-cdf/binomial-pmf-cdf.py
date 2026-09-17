import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    def pmf(a):
        return math.comb(n , a)*(p**a)*((1-p)**(n-a))
    cdf = 0
    for i in range(0 , k+1):
        cdf += pmf(i)
    return {"pmf" : float(pmf(k)) , "cdf" : float(cdf)}
    pass