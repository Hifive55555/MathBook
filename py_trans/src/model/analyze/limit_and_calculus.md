# Limit And Calculus

## Limit

- Definition

    $\exists\{a_n\},\ \lim_{n \to \infin} a_n = A$ denotes:

    $\forall \sigma > 0,\ \exists N > 0, \\
    \text{s.t. when } n > N,\ |a_n - A| < \sigma. \\$

    $\lim_{x \to x_0} f(x)=A$ denotes:

    $\forall \sigma > 0,\ \exists \xi > 0, \\
    \text{s.t. when } x \in \mathring{U}(x, \xi),\ f(x) \in \mathring{U}(A, \sigma)$

- Algorithm
  - 极限（一元运算符）对加法和乘法构成结合律

## Sequence Limit

### $\sigma - N$

> $\forall \sigma > 0,\ \exists N > 0, \\
\text{ s.t. when } n > N,\ |a_n - N| < \sigma. \\
\Longleftrightarrow \{a_n\} \text{ is convergent.}$

### Squeeze Theorem

> $n · u_{\min} < \sum_{i=1}^n u_i < n · u_{\max}$

The numerator and denominator are homogeneous.\
The summation doesn't affect the limmit.

### Monotonically bounded criterion

> $\exists \{x_n\},\ x_{n+1}\ge x_n, \inf x_n = M \\
\Longleftrightarrow \exists \lim_{n \to \infin} x_n \le M.$\
> $\exists \{x_n\},\ x_{n+1}\le x_n, \sup x_n = m \\
\Longleftrightarrow \exists \lim_{n \to \infin} x_n \ge m.$

### By Integration Or Fraction

The general form of the limit of summation is
$$\lim_{n \to \infin} \sum_{k=1}^n f(n,k)$$

1. $f(n,k) = g(k) = u(k+1) - u(k)$
    > $\lim_{n \to \infin} \sum_{k=1}^n g(k) = \lim_{n \to \infin} [u(n+1) - u(1)]$

    See [Fraction](fraction.md)

2. $f(n,k) = \frac{1}{n} g(\frac{k}{n})$
    > $\lim_{n \to \infin} \sum_{k=1}^n \frac{1}{n} g(\frac{k}{n}) = \int_0^1 g(x) dx$

### Heine Theorem

> $\lim_{x \to x_0} f(x) = A\\
\Longleftrightarrow \exists \{x_n\},\  x_n \to x_0, \text{ s.t. } f(x_n) \to A.$\
> $x_o \to \infin \text{ also.}$

## Function Limit

## Derivation

## Differentiation

## Integration
