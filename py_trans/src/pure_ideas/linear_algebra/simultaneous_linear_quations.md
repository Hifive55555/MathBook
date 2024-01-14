# Simultaneous Linear Equations

1. 矩阵乘以一个列矩阵

    1. 线性变换

        > 线性变换的详细定义参见下一篇文章
        我们发现线性变换终不过是线性方程组的形式，因此其结果应该于线性方程组的一致。

    2. 线性方程组

        我们用这样的图来直观地感受矩阵之于线性方程组的操作:

        $$\begin{matrix}\\ \\ y_1 \\ y_2 \\ \vdots \\ y_m
        \end{matrix}
        \begin{matrix}\\ \\ \ \leftarrow\ \end{matrix}
        \begin{matrix}
          \ x_1\qquad x_2\quad \cdots\quad x_n\ \ \\
          \downarrow\ \\
        \begin{bmatrix}
          a_{11}&a_{12}&\cdots&a_{1n} \\
          a_{21}&a_{22}&\cdots&a_{2n} \\
          \vdots&\vdots&&\vdots \\
          a_{m1}&a_{m2}&\cdots&a_{mn}
        \end{bmatrix}
        \end{matrix}$$

        我们就定义这样的操作为矩阵的普通乘法,得到结果称为普通乘积.
        $$\begin{bmatrix}
        y_1 \\ y_2 \\ \vdots \\ y_m
        \end{bmatrix}=
        \begin{bmatrix}
          a_{11}&a_{12}&\cdots&a_{1n} \\
          a_{21}&a_{22}&\cdots&a_{2n} \\
          \vdots&\vdots&&\vdots \\
          a_{m1}&a_{m2}&\cdots&a_{mn}
        \end{bmatrix}
        \begin{bmatrix}
          x_1 \\ x_2 \\ \vdots \\ x_n
        \end{bmatrix}$$

        其中对于任一第 $i$ 个 $y_i$ , 都满足
        $$y_i=a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n$$

        因此每一个矩阵都有一个含义--**线性变换**.

2. 两个矩阵相乘

    对于列矩阵 $x$ , 对 $x$ 执行两次线性变换, 相当于对 $x$ 执行了一次新的线性变换, 也就是说
    $$BAx=Cx$$

    令 $y=Ax,\ z=BAx=By$ , 有线性方程组
    $$\begin{cases}
      y_1=a_{11}x_1+\cdots+a_{1n}x_n \\
      \quad\ \ \vdots \\
      y_m=a_{m1}x_1+\cdots+a_{mn}x_n
    \end{cases}\tag{1}$$
    $$\begin{cases}
      z_1=b_{11}y_1+\cdots+b_{1m}y_m \\
      \quad\ \ \vdots \\
      z_k=b_{k1}y_1+\cdots+b_{km}y_m
    \end{cases}\tag{2}$$

    将 $(1)$ 代入 $(2)$ 中得
    $$\begin{cases}
      z_1 &= &b_{11}(a_{11}x_1+\cdots+a_{1n}x_n)+\cdots+ \\
      &&b_{1m}(a_{m1}x_1+\cdots+a_{mn}x_n) \\
      &\ \vdots \\
      z_k &= &b_{k1}(a_{11}x_1+\cdots+a_{1n}x_n)+\cdots+ \\
      &&b_{km}(a_{m1}x_1+\cdots+a_{mn}x_n)
    \end{cases}$$

    把 $x_i$ 提取公因式(下列求和条件均为 $1\le i\le m,\ 1\le j\le k$ )
    $$\begin{cases}
      z_1 &= &(\sum_{} b_{1j}a_{i1})x_1+\cdots+(\sum_{} b_{1j}a_{in})x_n\\
      &\ \vdots \\
      z_k &= &(\sum_{} b_{kj}a_{i1})x_1+\cdots+(\sum_{} b_{kj}a_{in})x_n
    \end{cases}$$

    写成矩阵的形式
    $$\begin{bmatrix}
        z_1 \\ z_2 \\ \vdots \\ z_k
    \end{bmatrix}=
    k\left\{\begin{matrix}\\ \\ \\ \\
    \end{matrix}\right.
    \overbrace{
    \begin{bmatrix}
      \sum_{} b_{1j}a_{i1} &\cdots& \sum_{} b_{1j}a_{in} \\
      \vdots&&\vdots \\
      \sum_{} b_{kj}a_{i1} &\cdots& \sum_{} b_{kj}a_{in}
    \end{bmatrix}
    }^{n}
    \begin{bmatrix}
      x_1 \\ x_2 \\ \vdots \\ x_n
    \end{bmatrix}$$

    所以对于矩阵 $C=[c_{ij}]$ 的每个第 $\alpha$ 行第 $\beta$ 列的元都满足
    $$c_{\alpha \beta}=\sum_{} b_{\alpha j}a_{i \beta}$$

    这样的 $$Cx=BAx$$
    我们就称 $C$ 是 $B$ 和 $A$ 的**普通乘积**, 记作
    $$C=BA$$

- **Definition** *Matmul Product*