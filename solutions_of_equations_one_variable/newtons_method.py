import numpy as np
import pandas as pd
import sympy as sp

x = sp.symbols('x')

f_ = sp.cos(x) - x
f = sp.lambdify(x, f_, 'numpy')

df_ = sp.diff(f_, x)
df = sp.lambdify(x, df_, 'numpy')

def newtons_method(p_0, tol, max_iter):
    p = p_0
    records = []

    for n in range(max_iter):
        p_n = p - f(p)/df(p)
        records.append([n, p_n, abs(p_n - p)])

        if abs(p_n - p) < tol:
            break
        else:
            p = p_n

        table = pd.DataFrame(records, columns=["n", "p_n", "abs(p_n - p"])
    return table

newtons_method(0.5, 1e-5, 100)
