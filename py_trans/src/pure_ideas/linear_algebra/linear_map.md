# Linear Map

Suppose $V$ and $W$ are two **linear spaces**, and $(v_1,v_2,\cdots,v_n)$ is a basis of $V$, $(w_1,w_2,\cdots,w_m)$ is a basis of $W$. (So $dimV=n,\ dimW=m.)$ And suppose $T \in \mathcal{L}(V,W).$

- Question: can we denote $T$ ?
- **Solution**

  对于任一 $v \in V$, 都存在一个 $w \in W$, s.t. $w=T(v)$.\
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
  $$Tv_i=a_{i,1}w_1+\cdots+a_{i,m}w_m$$

  So,
  $$\begin{align*}
  w=T(v)=\ &x_1(a_{1,1}w_1+\cdots+a_{1,m}w_m)\ + \\
  &x_2(a_{2,1}w_1+\cdots+a_{2,m}w_m)\ + \\
  &\cdots\ + \\
  &x_n(a_{n,1}w_1+\cdots+a_{n,m}w_m) \\
  =\ &(x_1a_{1,1}+\cdots+x_na_{n,1})w_1\ + \\
  &(x_1a_{1,2}+\cdots+x_na_{n,2})w_2\ + \\
  &\cdots\ + \\
  &(x_1a_{1,n}+\cdots+x_na_{n,m})w_m\ + \\
  =\ &y_1w_1+\cdots+y_mw_m
  \end{align*}$$

  Hence,
  $$\begin{cases}
  y_1 = x_1a_{1,1}+\cdots+x_na_{n,1} \\
  y_2 = x_1a_{1,2}+\cdots+x_na_{n,2} \\
  \quad\ \ \vdots \\
  y_m = x_1a_{1,n}+\cdots+x_na_{n,m}
  \end{cases}$$

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
