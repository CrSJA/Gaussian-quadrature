from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np
import math

def integrable(x):
    """Funtion to be integrated



    Args:
        x (float): any real numbre

    Returns:

        retuns the sin(x^2) of a np.array or a float depending on the imput
        
        example:
        x=np.array([-0.86113631, -0.33998104,  0.33998104,  0.86113631])
        print(integrable(x))
        
        prints:
        [0.67543596 0.1153299  0.1153299  0.67543596]    

        

    """
    return np.sin(x**2)

def gaussxw(N):
    """Calculates the zeros of Legendre polynomial and the weights on on the interval [-1,1]
    funtion created for encapsulation 

    Args:
        N (int): number of cuts of the aproximation
        
    Returns:

        a dupel containig two np.arrays, the ceros of Legendre polynomial and the weights
        example:

        (
        array([-0.86113631, -0.33998104,  0.33998104,  0.86113631]),
        array([0.34785485, 0.65214515, 0.65214515, 0.34785485])
        )

    Raises:
        ValueError: invalid literal for int() with base 10:
    """

    x, w = np.polynomial.legendre.leggauss(N)
    
    return x, w

def main():

    pass


if __name__=="__main__":
    main()