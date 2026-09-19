import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    def pmf(a):
        pmf = (math.exp((-lam))*(lam**a)) / math.factorial(a)
        return pmf
    cdf = 0
    for i in range(0 , k+1):
        cdf += pmf(i)
    return {"pmf" : pmf(k) , "cdf" : cdf}
    pass