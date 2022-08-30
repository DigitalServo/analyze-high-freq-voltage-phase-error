# coding: utf-8
# Your code here!

import sympy as sy

# original simplify atan
def simplify_atan(sympy, expr_y, expr_x):
    fx = sympy.simplify(expr_x)
    fy = sympy.simplify(expr_y)
    tan = fy / fx
    atan = sympy.atan(tan)
    theta = sympy.simplify(atan)
    return sympy.factor(theta)

# original simplify atan
def simplify_collect(sympy, expr_input, collect_expr):
    expr = expr_input
    # expr = sympy.factor(expr)
    expr = sympy.simplify(expr)
    # expr = sympy.factor(expr)
    expr = sympy.collect(expr, collect_expr)
    return expr

#Jupyter Notebookを使う場合
# sy.init_printing()

#motor params
Li = sy.Symbol("Li", real=True)
Lm = sy.Symbol("Lm", real=True)
A = sy.Symbol("A", real=True)
K = sy.Symbol("K", real=True)
theta_gamma = sy.Symbol("theta_gamma", real=True)
theta_re = sy.Symbol("theta_re", real=True)
theta_e = sy.Symbol("theta_e", real=True)

#gain
g_pi = sy.Symbol("g_pi", real=True)
g_pm = sy.Symbol("g_pm", real=True)
g_ni = sy.Symbol("g_ni", real=True)
g_nm = sy.Symbol("g_nm", real=True)
g_pi = A*(1+K)*Li
g_pm = A*(-(1-K)*Lm)
g_ni = A*(1-K)*Li
g_nm = A*(-(1+K)*Lm)

#complex amp
c_p = sy.Symbol("c_p", real=True)
s_p = sy.Symbol("s_p", real=True)
c_n = sy.Symbol("c_n", real=True)
s_n = sy.Symbol("s_n", real=True)
c_p = g_pi + g_pm * sy.cos(2*theta_gamma)
s_p =        g_pm * sy.sin(2*theta_gamma)
c_n = g_ni + g_nm * sy.cos(2*theta_gamma)
s_n =        g_nm * sy.sin(2*theta_gamma)

#variable num
C_2p = sy.Symbol("C_2p", real=True)
S_2p = sy.Symbol("S_2p", real=True)
C_2p = c_p*c_n - s_p*s_n
S_2p = s_p*c_n + c_p*s_n
theta_re = sy.atan(C_2p / S_2p)

#hosooka
#complex amp
c_pt = sy.Symbol("c_pt", real=True)
s_pt = sy.Symbol("s_pt", real=True)
c_nt = sy.Symbol("c_nt", real=True)
s_nt = sy.Symbol("s_nt", real=True)
c_pt = c_p * sy.cos(theta_e) - s_p * sy.sin(theta_e)
s_pt = s_p * sy.cos(theta_e) + c_p * sy.sin(theta_e)
c_nt = c_n * sy.cos(theta_e) - s_n * (-sy.sin(theta_e))
s_nt = s_n * sy.cos(theta_e) + c_n * (-sy.sin(theta_e))

#original
#gamma delta tilde complex amp
c_gammat = sy.Symbol("c_gammat", real=True)
s_gammat = sy.Symbol("s_gammat", real=True)
c_deltat = sy.Symbol("c_deltat", real=True)
s_deltat = sy.Symbol("s_deltat", real=True)
c_gammat = c_pt + c_nt
s_gammat = s_pt - s_nt
c_deltat = -c_pt + c_nt
s_deltat = -(-s_pt - s_nt)

print("@calculate 220827-2 my expr")
y = s_gammat + K*s_deltat
x = c_gammat - K*c_deltat
print(simplify_collect(sy,x,sy.cos(theta_e)))
print(simplify_collect(sy,y,sy.sin(theta_e)))
print("@calculate atan my expr")
print(simplify_atan(sy, y, x))