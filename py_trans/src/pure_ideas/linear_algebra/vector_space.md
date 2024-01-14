# Vecotor Space

**向量空间**是一种代数结构，它被定义为带有**加法**和**数乘**的集合。向量空间的元素被称作**向量**。\
也就是是说向量没有一个确切的面貌，只要它们满足可加和可数乘的就行，最熟悉的例子是*几何向量*或*矢量(Euclidean vectors, geometric vector, spatial vector)*，表示具有大小和方向的对象。其他例子，还包括*坐标空间(Coordinate spaces)、复数、函数空间(Function spaces)、线性方程组(linear equations)*。

- **Definition** *Vector Space*

  **向量空间**是定义了加法和数乘的向量的集合。

  给定域 $\mathbb{F}$ ，向量空间 $V$ 记为 $\mathbb{F}-向量空间$ 。其二元运算：

  - 向量加法：+ : $V × V → V$ 记作 $v + w,\ ∃ v,w ∈ V$
  - 数乘：· : $F × V → V$ 记作 $av,\ ∃a ∈ F$ 且 $v ∈ V$

  并且满足如下8条公理：

  1. 加法结合律：$u + (v + w) = (u + v) + w$
  2. 加法单位元：$V$ 存在零向量 $o，∀ v ∈ V , v + o = v$
  3. 加法逆元：$∀v∈V,\ ∃w∈V$ ，使得 $v + w = o$
  4. 加法交换律：$v + w = w + v$
  5. 数乘与*域乘法*兼容性(compatibility): $a(b v) = (ab)v$
  6. 数乘单位元: $1 v = v$ , $1$ 指域F的乘法单位元
  7. 数乘对于向量加法满足分配律：$a(v + w) = a v + a w$
  8. 数乘对于*域加法*满足分配律: $(a + b)v = a v + b v$

  另，若 $\mathbb{F}$ 是实数域 ℝ，则 $V$ 称为实数向量空间；若 $\mathbb{F}$ 是复数域 ℂ ，则 $V$ 称为复数向量空间；若 $\mathbb{F}$ 是有限域，则 $V$ 称为有限域向量空间。

  > 对于**域加法**和**域乘法**的定义详见 [List And Matrix](list_and_matrix.md)

- **Definition** *Vector*
  
  向量就是向量空间里的元素。

- **Example**

  - $F^n$ and  $F^{\infty}$ **坐标空间**

    在上一篇中我们提到了**列表**的一个应用，也就是 $F^n$ ，它表示表示 $n$ 维分量全为数全体向量。我们把它叫做**坐标空间**。
    $$F^n=\{(a_1,a_2,\cdots,a_n):a_i\in\mathbb{F}\}$$

    如果这个列表有无穷个元素，那么所有这样的列表构成一个向量空间，记为 $F^{\infty}$ 。
    $$F^{\infin}=\{(a_1,a_2,\cdots):a_i\in\mathbb{F}\}$$

    在这个向量空间中向量的加法就被定义为列表的加法，数乘亦然。
  
  - $F^S$ **函数空间**

    如果把一个函数 $f:x\mapsto y$ 的每个 $x$ 看作向量的一个分量，我们惊讶地发现，函数相加不就是这些分量相加嘛，数乘亦然。

    **Definition**
    - 如果 $S$ 是一个集合，$F^S$ 表示所有从 $S$ 映射到 $\mathbb{F}$ 的函数的集合。
    - 对于 $f,g\in F^S$ ，加法 $f+g\in F^S$ 被定义为
      $$(f+g)(x)=f(x)+f(g)\qquad\forall x\in\mathbb{F}$$
    - 对于 $\lambda\in\mathbb{F},\ f\in F^S$ ，数乘 $\lambda f\in F^S$ 被定义为
      $$(\lambda f)(x)=\lambda f(x)\qquad\forall x\in\mathbb{F}$$

    通过向量空间的八条法则的判定，易得 $F^S$ 是一个向量空间，我们称之为**函数空间**。

> 在下文中，我们默认 $V$ 表示一个向量空间。

## SubSpaces

- **Definition** *SubSpace*

  如果 $U$ 是 $V$ 的一个子集，并且如果 $U$ 也是一个向量空间（满足那八条法则），就称 $U$ 是 $V$ 的**向量子空间**。

- **Application**
  
  - .

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
