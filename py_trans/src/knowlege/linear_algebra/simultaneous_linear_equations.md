# Simultaneous Linear Equations

我们把形如下面的式子称作一个线性方程组：

$$\begin{cases}
  y_1=a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n \\
  y_2=a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n \\
  \quad\ \ \vdots \\
  y_m=a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n
\end{cases}\tag{a}$$

下面我们将其用矩阵表示,并借机定义矩阵的乘法.

## Denote It By Matrix

线性方程组 $(a)$ 式可以用矩阵表示:

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

其中对于任一第 $i$ 个 $y_i$ , 都满足
$$y_i=a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n$$

反过来我们就定义这样的操作就是矩阵的**普通乘法**

## 扩展矩阵乘法的定义

令 $y=Ax,\ z=BAx=By$ , 有线性方程组
$$\begin{cases}
  y_1=a_{11}x_1+\cdots+a_{1n}x_n \\
  \quad\ \ \vdots \\
  y_p=a_{p1}x_1+\cdots+a_{pn}x_n
\end{cases}\tag{1}$$
$$\begin{cases}
  z_1=b_{11}y_1+\cdots+b_{1p}y_p \\
  \quad\ \ \vdots \\
  z_m=b_{m1}y_1+\cdots+b_{mp}y_p
\end{cases}\tag{2}$$

> **线性变换的角度理解**\
> 对于列矩阵 $x$ , 对 $x$ 执行两次线性变换, 相当于对 $x$ 执行了一次新的线性变换, 也就是说
> $$BAx=Cx$$

将 $(1)$ 代入 $(2)$ 中得
$$\begin{cases}
  z_1 &= &b_{11}(a_{11}x_1+\cdots+a_{1n}x_n)+\cdots+ \\
  &&b_{1p}(a_{p1}x_1+\cdots+a_{pn}x_n) \\
  &\ \vdots \\
  z_m &= &b_{m1}(a_{11}x_1+\cdots+a_{1n}x_n)+\cdots+ \\
  &&b_{mp}(a_{p1}x_1+\cdots+a_{pn}x_n)
\end{cases}$$

把 $x_i$ 提取公因式(下列求和条件均为 $1\le k\le p$ )
$$\begin{cases}
  z_1 &= &(\sum_{} b_{1k}a_{k1})x_1+\cdots+(\sum_{} b_{1k}a_{kn})x_n\\
  &\ \vdots \\
  z_m &= &(\sum_{} b_{pk}a_{k1})x_1+\cdots+(\sum_{} b_{pk}a_{kn})x_n
\end{cases}$$

写成矩阵的形式
$$\begin{bmatrix}
    z_1 \\ z_2 \\ \vdots \\ z_k
\end{bmatrix}=
\begin{bmatrix}
  \sum_{} b_{1p}a_{p1} &\cdots& \sum_{} b_{1p}a_{pn} \\
  \vdots&&\vdots \\
  \sum_{} b_{kp}a_{p1} &\cdots& \sum_{} b_{kp}a_{pn}
\end{bmatrix}
\begin{bmatrix}
  x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix}$$

所以对于矩阵 $C=[c_{ij}]$ 的每个第 $i$ 行第 $j$ 列的元都满足
$$c_{ij}=\sum_{k=1}^p b_{ik}a_{kj}$$

这样的 $$Cx=BAx$$
我们就称 $C$ 是 $B$ 和 $A$ 的**普通乘积**, 记作
$$C=BA$$

## **Definition** - *Matmul Product*

设 $B$ 为 $m \times p$ 的矩阵，$A$ 为 $p \times n$ 的矩阵，那么称 的矩阵 $C$ 为矩阵 $B$ 与 $A$ 的乘积，记作 $BA$ ，其中矩阵 $C$ 中的第 $i$ 行第 $j$ 列元素可以表示为：
$$(BA)_{ij}=\sum_{k=1}^p b_{ik}a_{kj}$$

> 其中简单的计算方法见分块矩阵, 几何意义见线性变换
