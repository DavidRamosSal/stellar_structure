delta=0.1
def stepsize(y,dy):
    """Adaptive stepsize. It takes the current value of the variables and it's gradients. The parameter delta is defined externally."""
    return delta*((1/y[0])*dy[0]-(1/y[1])*dy[1])**(-1)