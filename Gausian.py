from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

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
    funtion created for abstracion

    Args:
        N (int): number of cuts of the aproximation
        
    Returns:

        a dupel containig two np.arrays, the ceros of Legendre 
        polynomial and the weights
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

def gaussxwab(a, b, x, w):
    """Re-escales the interval legendre polynomial
    
    Args:
        a (float): infirior limit of the new interval
        b (float): upper limit of the new interval
        x (numpy-array): sampling points to be evaluated
        w (numpy-array): weights of the reiman sum

    Returns:

        a dupel containig two np.arrays, the ceros of Legendre 
        polynomial and the weights
        example:

        (
        array([-0.86113631, -0.33998104,  0.33998104,  0.86113631]),
        array([0.34785485, 0.65214515, 0.65214515, 0.34785485])
        )

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def Gausian_Cuadrature_0_Pi(N,f):
    """evaluates the integral of a funtion fom [0,pi] using the 
    gaussian cuadrature

    Args:
        N (int): number of cuts use in the aproximation
        f (PyFunction_Type): funtion to be integrated

    Returns: 
        
        a float that is the result of the integration

    """

    PMP=gaussxw(N)
    PMPE=gaussxwab(0,np.pi,PMP[0],PMP[1])

    return  np.sum(PMPE[1]*(f(PMPE[0])))

def main():
    """main funtion,
    evaluates the integral of our functon and graphs the results
    """


    x_axis=np.arange(1,21,1)
    y_axis=np.zeros(20)

    for a in range(len(x_axis)): # esto parece ser inivitable
        y_axis[a]=Gausian_Cuadrature_0_Pi(x_axis[a],integrable )
    print(y_axis)
    plt.plot(x_axis,y_axis)

if __name__=="__main__":
    main()