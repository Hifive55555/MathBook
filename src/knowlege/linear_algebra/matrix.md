# Matrix

## Beforehand： List And Linear Combination

### List

- **Definition** *List*
  
  **列表**就是一列元素（括号可以省略不写）
  $$(a_1,a_2,\cdots,a_n)$$

  若 \\(\quad a_1,a_2,\cdots,a_n\in\mathbb{F}\\) ，则称 \\((a_1,a_2,\cdots,a_n)\\) 为一个**数组**。

  - **Definition** *Coordinate*\
  列表中的一个数就是列表的坐标

  - **Definition** *Length*\
  列表的长度就是列表坐标的个数

- **Property** *List*
  
  - Add\
    列表的相加就是对应位置相加
  - Scalar Multiply\
    列表的数乘就是把数乘以每一个坐标

- **Definition** \\(F^n\\)
  
  \\(F^n\\) 就是所有长度相同的数组的集合
  $$F^n=\{ (a_1,a_2,\cdots,a_n):a_1,a_2,\cdots,a_n \in F \}$$

列表是一个抽象概念，这意味着很多类似于列表的结构都可以用列表来表示。例如一个空间向量就可以用列表来表示，列表也可以用空间向量来理解。但列表和向量本质上是两种概念。在后面我们会看到，列表也可以构成一个向量空间，此时列表就是这个空间的向量。

### Linear Combination

- **Definition** *Linear Combination*
  
  线性组合就是把列表里的向量乘上一个系数在加起来。
  If \\(a\\) is a ***linear combination*** of \\((x_1,\ x_2\ ,\cdots,\ x_n)\\) , then \\(a=a_1x_1+a_2x_2+\cdots+a_nx_n\\) .

### Corollary

如果关于 \\((x_1,x_2,\cdots,x_n)\\) 的线性组合有多个，我们可以把它写成一个列表。
$$(a_{11}x_1+\cdots+a_{1n}x_n,\cdots,a_{m1}x_1+\cdots+a_{mn}x_n),\quad a_{ij}\in\mathbb{F}$$

这个列表等同于一个新的关于 \\((x_1,x_2,\cdots,x_n)\\) 的线性组合。即：
$$(a_{11},\cdots,a_{1m})x_1+\cdots+(a_{n1},\cdots,a_{nm})x_1$$

## Linear Function

> Linear function is synonymous with being proportional.

下面我们想通过线性方程来尝试理解单纯意义的矩阵（而不是直接通过线性方程组得到）。

- **Definition** *Linear Function*
  
  线性函数就是输出一个 \\((x_1,x_2,\cdots,x_n)\\) 的不同的线性组合的列表的函数。也就是说，它是 \\(\mathbb{F^n}\\) 之间的一种映射。

For \\(x,y\in\mathbb{R}\\),\
a linear function \\(f:\mathbb{R}\to\mathbb{R}\\) is such that \\(f(x)=ax\\) ;\
a linear function \\(f:\mathbb{R^2}\to\mathbb{R}\\) is such that \\(f(x,y)=ax+by\\) ;\
a linear function \\(f:\mathbb{R}\to\mathbb{R^2}\\) is such that \\(f(x)=(ax,bx)\\) ;\
a linear function \\(f:\mathbb{R^2}\to\mathbb{R^2}\\) is such that \\(f(x,y)=(a_1x+b_1y,a_2x+b_2y)\\) ;\
(We'll talk about this case latter for why it can be think proportional)

For \\(x=(x_1,\cdots,x_n)\in\mathbb{R^n}\\) ,\
a linear function \\(f:\mathbb{R^{n}}\to\mathbb{R^m}\\) is such that\
\\(f(x_1,\cdots,x_n)=
(\overbrace{\underbrace{a_{11}x_1+\cdots+a_{1n}x_n}_{n},\cdots,a_{m1}x_1+\cdots+a_{mn}x_n}^{m})\\) ;

If a linear function \\(f:x\mapsto y,x\in\mathbb{R^n},y\in\mathbb{R^m}\\) , i.e. \\((y_1,\cdots,y_m)=f(x_1,\cdots,x_n)\\), it can be denoted by a ***linear simultaneous equations***
$$\begin{cases}
y_1=a_{11}x_1+\cdots+a_{1n}x_n\\\\
y_2=a_{21}x_1+\cdots+a_{2n}x_n\\\\
\quad\ \ \vdots\\\\
y_m=a_{m1}x_1+\cdots+a_{mn}x_n
\end{cases}$$

or at a form of list (vertical)
$$\begin{matrix}y_1,\\\\ y_2,\\\\ \vdots,\\\\ y_m
\end{matrix}=
\overbrace{
  \begin{matrix}
  a_{11}x_1+\cdots+a_{1n}x_n,\\\\
  a_{21}x_1+\cdots+a_{2n}x_n,\\\\
  \vdots\ ,\\\\
  a_{m1}x_1+\cdots+a_{mn}x_n
\end{matrix}}^{n}
\tag{2.1}$$

There may be another way to look at it.
$$(y_1,\cdots,y_m)=
\begin{matrix}
  x_1\overbrace{(a_{11},\cdots,a_{m1})}^{m}\ +\\\\
  x_2(a_{11},\cdots,a_{m1})\ +\\\\
  \cdots+\\\\
  x_n(a_{1n},\cdots,a_{mn})\ \ \
\end{matrix}
\tag{2.2}$$

\\((2.1)\\) 式和 \\((2.2)\\) 式长得很像啊，就好像只是翻转了一下。而且我们很想把 \\((2.2)\\) 式提取公因式的操作应用到 \\((2.1)\\) 式上。我想也许有更优雅并且更清晰的方式去书写。

## Matrice

一个 \\(\mathbb{R^n}\to\mathbb{R^m}\\) 的线性变换，不过就是输入 \\(n\\) 个参数然后输出 \\(m\\) 个参数。我们不妨用一个矩形的数阵去表示。
$$\begin{matrix}\\\\ \\\\ y_1,\\\\ y_2,\\\\ \vdots,\\\\ y_m
\end{matrix}
\begin{matrix}\\\\ \\\\ \ \leftarrow\ \end{matrix}
\begin{matrix}
  x_1,\ x_2\ ,\cdots,\ x_n\ \ \\\\
  \downarrow\ \\\\
\begin{bmatrix}&&&&&&\\\\ \\\\ \\\\ \\\\ \\\\ \end{bmatrix}
\end{matrix}$$

现在我们把单纯的列表改写成一个竖着的数阵，把这样的函数操作用点乘表示（也可以省略），并且从右往左书写。
$$\begin{bmatrix}y_1\\\\ y_2\\\\ \vdots\\\\ y_m\end{bmatrix}=
\begin{bmatrix}\\\\&& \\\\ \\\\ \\\\ \end{bmatrix}
\begin{bmatrix}x_1\\\\ x_2\\\\ \vdots\\\\ x_n\end{bmatrix}$$

因为这是线性变换，所以每个 \\(y\\) 都是 \\(x_1,\ x_2\ ,\cdots,\ x_n\\) 的线性组合。

### Column Martix

A single column matrix can be thought of that *"creating a list"*.

For example, \\(\begin{bmatrix}x\\\\ y\end{bmatrix}\\) can be thought of \\(\begin{bmatrix}x\\\\ y\end{bmatrix}·1\\) , which means a linear function from "\\(1\\)" to \\(\mathbb{R^2}\\) through **dilation**. So a column matrix create a column matrix itself via scale "\\(1\\)".

### Row Matrix

A row matrix can be thought of that *"receive and calculate (compress)"*.

For example, \\(\begin{bmatrix}a&b\end{bmatrix}\\) has a function below.\
In the case \\(\begin{bmatrix}a&b\end{bmatrix} \begin{bmatrix}x\\\\ y\end{bmatrix}\\) , \\(\begin{bmatrix}a&b\end{bmatrix}\\) receives two variables \\((x,y)\\) and sums them up, resulting in \\(ax+by\\) .

### \\(m\times n\\) Matrix

- **Definition** *\\(m\times n\\) Matrix*
  
  A \\(m\times n\\) matrix is a matrix with n columns and m rows.

> A matrix has doulbe perspective through its *column* and *row*.

Let's say a matrix \\(M=\begin{bmatrix}a_1&b_1\\\\a_2&b_2 \end{bmatrix}\\) .

- **Column**
  
  Let \\(a=\begin{bmatrix}a_1\\\\ a_2\end{bmatrix}\\) , \\(b=\begin{bmatrix}b_1\\\\ b_2\end{bmatrix}\\) . Then \\(a\\) and \\(b\\) are two *columns* of \\(M\\) .\
  Hence we say \\(M=\begin{bmatrix}a&b\end{bmatrix}\\) (Here we've defined the block matrix).

  In the column perspective, \\(M\\) is a row matrix with the function of *"receive and calculate (compress)"*. And since now \\(a\\) and \\(b\\) are colume matrix, to remain the form, what \\(M\\) receives are always the same \\(2\times 1\\) matrices.

  So, the function of \\(M\\) is to receive two \\(2\times 1\\) matrices and add them up.
  $$\begin{bmatrix}a&b\end{bmatrix}
  \begin{bmatrix}x\\\\ y\end{bmatrix}=ax+by=
  \begin{bmatrix}a_1\\\\ a_2\end{bmatrix}x+
  \begin{bmatrix}b_1\\\\ b_2\end{bmatrix}y=
  \begin{bmatrix}a_1x+b_1y\\\\ a_2x+b_2y\end{bmatrix}$$

- **Row**
  
  Let \\(c=[a_1\quad b_1],\ d=[a_2\quad b_2]\\) . Then \\(M=\begin{bmatrix}c\\\\ d\end{bmatrix}\\) , a column matrix, with the function *"creating a list"*. As well, to remain the output form, \\(M\\) always gives us \\(2\times 1\\) matrices.

  But it's quit difficult to get a glimpse of the whole process of \\(M\\)'s function as we can't infer its input form by it's output. Nevertheless, we've know it's input form from above.

  So to remain the form, let \\(z=\begin{bmatrix}x\\\\ y\end{bmatrix}\\). So,
  $$\begin{bmatrix}c\\\\ d\end{bmatrix}z=
  \begin{bmatrix}cz\\\\ dz\end{bmatrix}=
  \begin{bmatrix}
    [a_1\quad b_1]·\begin{bmatrix}x\\\\ y\end{bmatrix}\\\\
    [a_2\quad b_2]·\begin{bmatrix}x\\\\ y\end{bmatrix}
  \end{bmatrix}=
  \begin{bmatrix}a_1x+b_1y\\\\ a_2x+b_2y\end{bmatrix}$$

  > So far we might know the basic principle of block matrix - if every elements of two matrices is meaningful when two of them are calculated, then the operation between the two matrices is permitted.

> **剧透**
>
> 对以上的操作全部执行转置，行与列的性质恰好互换了，并且乘法运算变成了从左往右。

## Rewrite Linear Function With Matrice

> Matrice makes it elegant when we denote linear operations.

- \\((2.1)\\)
  
  [上文 - Linear Function](#linear-function)
  
  $$y=\begin{bmatrix}y_1\\\\ y_2\\\\ \vdots\\\\ y_m\end{bmatrix}=
  \begin{bmatrix}
    a_{11}x_1+\cdots+a_{1n}x_n\\\\
    a_{21}x_1+\cdots+a_{2n}x_n\\\\
    \vdots\\\\
    a_{m1}x_1+\cdots+a_{mn}x_n\\\\
  \end{bmatrix}=
  \begin{bmatrix}a_{1,·}x\\\\ a_{2,·}x\\\\ \vdots\\\\ a_{m,·}x\\\\ \end{bmatrix}=
  \begin{bmatrix}a_{1,·}\\\\ a_{2,·}\\\\ \vdots\\\\ a_{m,·}\\\\ \end{bmatrix}x=
  Ax
  $$

  So,
  $$g_i(x)=a_{i,·}\ x$$

  which infers that \\(y\\) is a list of \\(g_i(x)\\) , or a list of linear combinations of \\(x_1,x_2,\cdots,x_n\\) .

- \\((2.2)\\)

  $$y^T=\begin{bmatrix}y_1&\cdots&y_m\end{bmatrix}=
  x_1a_{·,1}+\cdots+x_na_{·,n}=
  \begin{bmatrix}x_1&\cdots&x_n\end{bmatrix}
  \begin{bmatrix}a_{·,1}\\\\ \vdots\\\\ a_{·,n}
  \end{bmatrix}=x^TA^T$$

  Or,
  $$y=\begin{bmatrix}y_1&\cdots&y_m\end{bmatrix}=
  a_{·,1}x_1+\cdots+a_{·,n}x_n=
  \begin{bmatrix}a_{·,1}&\cdots&a_{·,n}\end{bmatrix}
  \begin{bmatrix}x_1\\\\ \vdots\\\\ x_n\end{bmatrix}=Ax$$

  So,
  $$h_j(x_j)=x_ja_{·,j}$$

  which infers that \\(y\\) is a sum of \\(h_j(x)\\) , or a linear combination of \\(a_{·,1},a_{·,2},\cdots,a_{·,n}\\) consists of lists.

### Conclusion

- **A *linear combination* can be denoted by a row matrix multiplies a column matrix**
  
  If \\(a\\) is combination of \\(x_1,x_2,\cdots,x_n\\) , or if \\(a=a_1x_1+a_2x_2+\cdots+a_nx_n\\) , then,

  $$a=\begin{bmatrix}x_1&\cdots&x_n\end{bmatrix}
  \begin{bmatrix}a_{1}\\\\ \vdots\\\\ a_{n}
  \end{bmatrix}$$

- **linear simultaneous equations**
  - **A *linear simultaneous equations* is a *list* of *linear combination***
  - **A *linear simultaneous equations* is *linear combination* consists of *lists***
  
- **A *linear simultaneous equations* can be denoted by a \\(m\times n\\) matrix multiplies a column matrix**

$$\begin{bmatrix}y_1\\\\ y_2\\\\ \vdots\\\\ y_m\end{bmatrix}=
\begin{bmatrix}
  a_{11}&a_{12}&\cdots&a_{1n}\\\\
  a_{21}&a_{22}&\cdots&a_{2n}\\\\
  \vdots&\vdots&&\vdots&\\\\
  a_{m1}&a_{m2}&\cdots&a_{mn}\\\\
\end{bmatrix}
\begin{bmatrix}x_1\\\\ x_2\\\\ \vdots\\\\ x_n\end{bmatrix}$$

It's the same that
$$y=Ax$$
