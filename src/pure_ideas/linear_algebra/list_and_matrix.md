# List And Matrix

$$(13,4,5,7)\qquad
\begin{bmatrix}
1&3&0\\\\ 2&0&5\\\\ 3&2&0
\end{bmatrix}$$

> ***列表*不是什么向量，它不过是一列元素罢了。**\
> ***矩阵*也不是什么线性变换，它只不过是一张表罢了。**\
> **当我们想让它们干什么的时候，它们才具备了它们的*代数结构*。**

一旦它们里面有了数，它们也许就可以具备一些性质，让里面的数发生数的运算。直觉告诉我们，也许相加就是对应位置相加，数乘就是把每个元素乘以一个数。我们的定义应该符合直觉。

## Beforhand

### \\(\mathbb{F}\\) And *Field*

\\(\mathbb{F}\\) 表示要么是 \\(\mathbb{R}\\) ，要么是 \\(\mathbb{C}\\) 。

其中，\\(\mathbb{R}\\) 表示**实数域（Real Number Field）**，\\(\mathbb{C}\\) 表示**复数域（Complex Number Field）**

其中，**实数域**表示全体实数构成的集合，并且**加法**和**乘法**分别对这个集合构成一个**阿贝尔群（Abelian Group）**，并且乘法对加法满足**分配律**。也就是说，加法和乘法分别对实数域是
1. 封闭的
2. 满足结合律
3. 存在单位元（分别是 0 和 1）
4. 存在逆元（分别用 - 和 \\(^{-1}\\) 表示）
5. 满足交换律

复数域的定义同理。

## Add

> 加法是数的运算，列表和矩阵的加法定义在数的加法。列表里的元素不一定是数，只要是可加的就行了——比如说数组和数阵（一般矩阵里都研究的是数，所以下文都认为矩阵就是数阵）。

如果要非定义列表或者矩阵的加法的话，两个具有相同结构的列表或矩阵才可以相加，那么加法就是对应位置的元素相加。

在下文我们会详细研究它们的结构，再给出准确的定义。

## Scalar Multiply

数乘就是把里面的每个元素乘上一个数。

## List

- **Definition**
  
  **列表**就是把一些元素用括号括起来，再用逗号隔开的结构。（其中括号有时可以省略）
  $$(a_1,a_2,\cdots,a_n)$$

  - 其中 \\(a_i\\) 叫做列表的**坐标（Coordinate）** ，\\(n\\) 叫做列表的**长度（Length）**
  
  - 如果满足$$a_1,a_2,\cdots,a_n\in\mathbb{F}，$$那么就称这个列表为**数组（Array）**。
  
  - 如果两个列表的坐标对应相等，则称两列表**相等**
  
- **Property** *Add*
  
  列表的加法就是对应坐标相加，满足其坐标都是可加的。

- **Property** *Scalar Multiply*
  
  列表的数乘就是对每个坐标乘以一个数，满足其坐标都是可数乘的。

- **Application**

  - \\(F^n\\)

    一列数组可以表示一个 \\(n\\) 维向量，且其分量全为数。
    所有长度为 \\(n\\) 的向量构成一个向量空间 \\(F^n\\) ，表示 \\(n\\) 维全体向量。
    $$F^n=\{(a_1,a_2,\cdots,a_n):a_1,a_2,\cdots,a_n\in\mathbb{F}\}$$

    如果这样的向量空间被定义了内积，那就是内积空间，可以做内积运算。如果把这样的列表理解成笛卡尔坐标，且 \\(\mathbb{F}=\mathbb{R}\\)，那这样的向量的空间就是欧几里得空间。

  - 陈列向量组
  
    一个列表经常用来陈列一组向量，比如一组基向量，或者一个极大线性无关组。

在使用列表时，要了解其使用场景和上下文，因为不同的使用场景默认对列表加入了新的代数结构，不可混用。

## Matrix

- **Definition**
  
  **矩阵**就是把一些以矩形阵形形式排列的元素用括号或者方括号括起来，再用空格隔开的结构。
  $$\begin{pmatrix}
  a_{11}&a_{12}&\cdots&a_{1n} \\\\
  a_{21}&a_{22}&\cdots&a_{2n} \\\\
  \vdots&\vdots&&\vdots \\\\
  a_{m1}&a_{m2}&\cdots&a_{mn} \\\\
  \end{pmatrix}$$

  - 其中 \\(a_{ij}\\) 叫做矩阵的一个**元** 。其中一行横着的元叫做矩阵的**行**，一列竖着的元叫做矩阵的**列**，\\(m\\) 叫做矩阵的**行数**，\\(n\\) 叫做矩阵的**列数**。
  
  - 我们谈论的矩阵都满足 \\(a_{ij}\in\mathbb{F}\\)
  
  - 行数和列数相同的矩阵叫做**同型矩阵**。
  
  - 如果同型矩阵 \\(A=[a_{ij}]，B=[b_{ij}]\\) ，满足 \\(a_{ij}=b_{ij}\\) ，则称两矩阵相等，记为 \\(A=B\\) 。
  
- **Property** *Add*
  
  同型矩阵的加法就是对应坐标相加。

- **Property** *Scalar Multiply*
  
  矩阵的数乘就是对每个元乘以一个数。

- **Application**

  - 表示线性方程组

    线性方程组
    $$\begin{cases}
    y_1=a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n \\\\
    y_1=a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n \\\\
    \quad\ \ \vdots \\\\
    y_1=a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n
    \end{cases}$$

    可以表示为
    $$\begin{bmatrix}
    y_1 \\\\ y_2 \\\\ \vdots \\\\ y_m
    \end{bmatrix}=
    \begin{bmatrix}
    a_{11}&a_{12}&\cdots&a_{1n} \\\\
    a_{21}&a_{22}&\cdots&a_{2n} \\\\
    \vdots&\vdots&&\vdots \\\\
    a_{m1}&a_{m2}&\cdots&a_{mn}
    \end{bmatrix}
    \begin{bmatrix}
    x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n
    \end{bmatrix}$$

    记为
    $$y=Ax$$

  - 表示线性变换

    若 \\(T\in\mathcal{L}(V,W)\\) ，\\(v_1,v_2\cdots,v_n\\) 和 \\(w_1,w_2\cdots,w_m\\) 分别是 \\(V\\) 和 \\(W\\) 的两组基。则定义 \\(m\\)-by-\\(n\\) 矩阵
    $$A=\begin{bmatrix}
    a_{11}&a_{12}&\cdots&a_{1n} \\\\
    a_{21}&a_{22}&\cdots&a_{2n} \\\\
    \vdots&\vdots&&\vdots \\\\
    a_{m1}&a_{m2}&\cdots&a_{mn}
    \end{bmatrix}$$
    是 \\(T\\) **的矩阵**。

    系数 \\(a_{ij}\\) 满足
    $$T(v_i)=a_{1i}w_1+a_{2i}w_2+\cdots+a_{mi}w_m$$
  
  - 表示一个向量的矩阵（我们教材上称之为“坐标”）
  
    若 \\(v\in V\\) 且 \\(v_1,v_2,\cdots,v_n\\) 是 \\(V\\) 的一组基。那么 \\(v\\) 可以被表示成这组基唯一的线性组合
    $$v=c_1v_1+\cdots+c_nv_n$$

    则向量 \\(v\\) **的矩阵** 可以被表示为一个列矩阵
    $$\mathcal{M}(v)=\begin{bmatrix}
    c_1 \\\\ \vdots \\\\ c_n
    \end{bmatrix}$$

    其中 \\(c_1,\cdots,c_n\\) 是标量。

### Matmul Product

矩阵在线性代数中被赋予了一个最基本的运算：**普通乘法**。

- 来源

1. 矩阵乘以一个列矩阵

    $$\begin{matrix}\\\\ \\\\ y_1 \\\\ y_2 \\\\ \vdots \\\\ y_m
    \end{matrix}
    \begin{matrix}\\\\ \\\\ \ \leftarrow\ \end{matrix}
    \begin{matrix}
      x_1\qquad x_2\quad \ \cdots\quad x_n\ \\\\
      \downarrow\ \\\\
    \begin{bmatrix}
      a_{11}&a_{12}&\cdots&a_{1n} \\\\
      a_{21}&a_{22}&\cdots&a_{2n} \\\\
      \vdots&\vdots&&\vdots \\\\
      a_{m1}&a_{m2}&\cdots&a_{mn}
    \end{bmatrix}
    \end{matrix}$$

    1. 方程组

        $$y_i=a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n$$

    2. 线性变换

        Suppose \\(V\\) and \\(W\\) are two **linear spaces**, and \\((v_1,v_2,\cdots,v_n)\\) is a basis of \\(V\\), \\((w_1,w_2,\cdots,w_m)\\) is a basis of \\(W\\). (So \\(dimV=n,\ dimW=m.)\\) And suppose \\(T \in \mathcal{L}(V,W).\\)

        对于任一 \\(v \in V\\), 都存在一个 \\(w \in W\\), s.t. \\(w=T(v)\\).\
        There is:
        $$
        v=x_1v_1+\cdots+x_nv_n \\\\
        w=y_1w_1+\cdots+y_mw_m \\\\
        $$

        There is also:
        $$\begin{align*}
        T(v) &= T(x_1v_1+\cdots+x_nv_n)\\\\
        &= x_1Tv_1+\cdots+x_nTv_n \\\\
        \end{align*}$$

        For each \\(Tv_i\\) , \\(i=(1,2,\cdots,n)\\), there is:
        $$Tv_i=a\_{i,1}w_1+\cdots+a\_{i,m}w_m$$

        So,
        $$\begin{align*}
        w=T(v)=\ &x\_.(a\_{1,1}w_1+\cdots+a\_{1,m}w_m)\ + \\\\
        &x_2(a\_{2,1}w_1+\cdots+a\_{2,m}w_m)\ + \\\\
        &\cdots\ + \\\\
        &x_n(a\_{n,1}w_1+\cdots+a\_{n,m}w_m) \\\\
        =\ &(x_1a\_{1,1}+\cdots+x_na\_{n,1})w_1\ + \\\\
        &(x_1a\_{1,2}+\cdots+x_na\_{n,2})w_2\ + \\\\
        &\cdots\ + \\\\
        &(x_1a\_{1,n}+\cdots+x_na\_{n,m})w_m\ + \\\\
        =\ &y_1w_1+\cdots+y_mw_m
        \end{align*}$$

        Hence,
        $$\begin{cases}
        y_1 &= x_1a\_{1,1}+\cdots+x_na\_{n,1} \\\\
        y_2 &= x_1a\_{1,2}+\cdots+x_na\_{n,2} \\\\
        &\vdots \\\\
        y_m &= x_1a\_{1,n}+\cdots+x_na\_{n,m}
        \end{cases}$$

        至此我们发现线性变换终不过是线性方程组的形式，因此其结果应该于线性方程组的一致。

    **结论**\
    我们定义矩阵的乘法如下：

2. 两个矩阵相乘

稍作推导
