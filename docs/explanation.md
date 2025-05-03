# Explanation of the method

The Gaussian Cuadrature is based on the Rieman Sum

$$
\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}
$$

the key idea is that tere is information to be obtiain by chosing the $w_k$ and $x_k$, in general they don't have to be homogeniusly distributed and it is posible to obtain a beter aproximation. A particularly interesting result is that tere is a rule to obtain the $x_k$ and $w_k$.

the rule is as folows:

let the legendre be

$$
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}
$$

then the $x_k$ are the zeros of the polynomials and the $w_k$ are choseen in the folowing way:

$$w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}}$$


note that this polynomial are only define in the interval $[-1,1]$ but it is posible to escalate the $x_k$ and the $w_k$ to any interval by using the procedure:

$$x=0.5  (b - a) \cdot x + 0.5  (b + a)$$

$$w=0.5 * (b - a) * w$$

were the $x$ and $y$ on the right of the equation haven't been scalated and $[a,b]$ is the new interval

that in essence is the methot for solving the integral, for more information regarding the implementation visit [reference](reference.md)
