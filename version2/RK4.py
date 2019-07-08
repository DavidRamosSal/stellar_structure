def RK4step(f, r, y, dr):
    """Propagates the solver one step further. Takes as input the RHS of the system f, the current location r,
    the current value of the variables y, and the stepsize. Returns the value of the variables in location r + dr."""
    k1,l1,n1 = f(r,y)
    
    k2,l2,n2 = f(r+0.5*dr,[y[0]+0.5*dr*k1,y[1]+0.5*dr*l1,y[2]+0.5*dr*n1])   
    
    k3,l3,n3 = f(r+0.5*dr,[y[0]+0.5*dr*k2,y[1]+0.5*dr*l2,y[2]+0.5*dr*n2])
    
    k4,l4,n4 = f(r+dr,[y[0]+dr*k3,y[1]+dr*l3,y[2]+dr*n3])
    
    k=(dr/6)*(k1+2.0*k2+2.0*k3+k4)
    l=(dr/6)*(l1+2.0*l2+2.0*l3+l4)
    n=(dr/6)*(n1+2.0*n2+2.0*n3+n4)
    
    return [y[0]+k,y[1]+l,y[2]+n]