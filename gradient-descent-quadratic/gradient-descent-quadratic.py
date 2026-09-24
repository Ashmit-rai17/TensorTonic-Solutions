def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    def der(x):
        return 2*a*x + b
    xt = 0
    for i in range(steps):
        xt = x0 - lr*der(x0)
        x0 = xt
    return xt
    pass