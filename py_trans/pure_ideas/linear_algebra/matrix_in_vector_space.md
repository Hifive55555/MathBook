# Why Do We Use Matrix?

矩阵在矩阵论和线性代数里的含义是大有不同的，准确地来说，我们在线性代数里是用向量空间的眼光看待矩阵；在这里，矩阵更多的是一种工具，一种表示的方式。当然，也有另一种眼光，它告诉我们矩阵本身就有着某种线性映射 (Linear Map) 的性质，我们在这一章暂且不谈。

## List

**列表**（List）是我认为在教材里缺失的一个重要概念，我之前常常把它和行向量搞混，虽然在计算上它的确可以被当作行向量计算，但它本身只是 $R^n$ 的一个向量；这一点必须要牢记，因为向量空间里的向量不一定是列表，而我们关注的是向量空间本身的性质而不是这个向量本身（*在计算的的时候列表常常与矩阵一同计算，但这种计算并不适用于其他向量*）

### Begin from a simple solution

当我们要量化一个**东西**的时候，这个东西往往在不同的方面可以进行不同的量化，例如一个 Apple，它至少有 Sweetness 和 Color 两种属性，我们管这种属性叫做 **Feature** 。

就拿 Apple 为例，假设每种 Apple 都可以被这两种 Feature 表示，我们可以说，Apple 就是这两个种特征的“和”（因为加法的良好属性，公因子相同的项才可以合并，也就是说如果把 Feature 当中一个因子单位，那么不同的 Feature 就是互不相干的）。那么对于一个苹果 $a \in Apple$ ，我们就说 $a=xS+yC$ ，$x$ 和 $y$ 就是这两个 Feature 的**量化值**。

显然，对于全体苹果构成的“苹果空间”（我们暂不讨论究竟构不构成一个空间，只是先熟悉下这个说法），我们真正关心的是它们的量化值，以及这些值之间的运算关系，<!-- 而 $S$ 和 $C$ 什么的已经是我们约定好了的，没必要每次都把它们写出来，我想我们可以换一个更方便的写法： -->我觉得我们可以搞一个合并单位 $SC$ 放到最后写好了，前面的值依顺序用 List 的方式写出来：

$$a= \begin{bmatrix}x\\y\end{bmatrix}(S,C)$$

- **Definition**

  if $a$ is a combinaton of $(x_1,x_2,\cdots,x_n)$, and the value of each dimension can be listed as $(a_1,a_2,\cdots,a_n)$. Like:
  $$a = a_1x_1 + a_2x_2 + \cdots + a_nx_n$$
  We say the matrix of $a$
  $$\mathcal{M(a)}=
  \begin{bmatrix}a_1 \\
  a_2 \\
  \vdots \\
  a_n
  \end{bmatrix},$$
  which tells the ***value*** of $a$.

## Linear Simultaneous Equations

A easier way to denote **linear simultaneous equations** is to write it without **Brace** and lots of **equal sign**.

- **Definition**

  $\begin{cases}
  x_1=y_1 \\
  x_2=y_2 \\
  \\ \vdots \\
  x_n=y_n
  \end{cases}$
  can be replaced by
  $\begin{bmatrix}
  x_1 \\ x_2 \\ \vdots \\ x_n
  \end{bmatrix}=
  \begin{bmatrix}
  y_1 \\ y_2 \\ \vdots \\ y_n
  \end{bmatrix}$
  or
  $\begin{bmatrix}
  x_1 & x_2 & \cdots & x_n
  \end{bmatrix}=
  \begin{bmatrix}
  y_1 & y_2 & \cdots & y_n
  \end{bmatrix}.$

  The shap of the matrix doesn't matter, instead of the one-by-one position.
- **Example**

  Write
  $$\begin{cases}
  x=
  \end{cases}$$

### Linear Map

Suppose $V$ and $W$ are two **linear spaces**, and $(v_1,v_2,\cdots,v_n)$ is a basis of $V$, $(w_1,w_2,\cdots,w_m)$ is a basis of $W$. (So $dimV=n,\ dimW=m.)$ And suppose $T \in \mathcal{L}(V,W).$

- Question: can we denote $T$ ?
- **Solution**

  $\\exist v \in V$, there exists only one $w \in W$, s.t. $w=T(v)$.\
  There is:
  $$
  v=x_1v_1+\cdots+x_nv_n \\
  w=y_1w_1+\cdots+y_mw_m \\
  $$

  There is also:
  $$\begin{align*}
  T(v) &= T(x_1v_1+\cdots+x_nv_n)\\
  &= x_1Tv_1+\cdots+x_nTv_n \\
  \end{align*}$$

  For each $Tv_i$ , $i=(1,2,\cdots,n)$, there is:
  $$Tv_i=a\_{i,1}w_1+\cdots+a\_{i,m}w_m$$

  So,
  $$\begin{align*}
  w=T(v)=\ &x\_.(a\_{1,1}w_1+\cdots+a\_{1,m}w_m)\ + \\
  &x_2(a\_{2,1}w_1+\cdots+a\_{2,m}w_m)\ + \\
  &\cdots\ + \\
  &x_n(a\_{n,1}w_1+\cdots+a\_{n,m}w_m) \\
  =\ &(x_1a\_{1,1}+\cdots+x_na\_{n,1})w_1\ + \\
  &(x_1a\_{1,2}+\cdots+x_na\_{n,2})w_2\ + \\
  &\cdots\ + \\
  &(x_1a\_{1,n}+\cdots+x_na\_{n,m})w_m\ + \\
  =\ &y_1w_1+\cdots+y_mw_m
  \end{align*}$$

  Hence,
  $$\begin{cases}
  y_1 &= x_1a\_{1,1}+\cdots+x_na\_{n,1} \\
  y_2 &= x_1a\_{1,2}+\cdots+x_na\_{n,2} \\
  &\vdots \\
  y_m &= x_1a\_{1,n}+\cdots+x_na\_{n,m}
  \end{cases}$$

  $$\begin{bmatrix}
  y_1 \\ y_2 \\ \vdots \\ y_m
  \end{bmatrix}=\begin{bmatrix}
  x_1a\_{1,1}+\cdots+x_na\_{n,1} \\
  x_1a\_{1,2}+\cdots+x_na\_{n,2} \\
  \vdots \\
  x_1a\_{1,n}+\cdots+x_na\_{n,m}
  \end{bmatrix}$$