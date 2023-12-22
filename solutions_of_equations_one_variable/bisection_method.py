import pandas as pd

def f(x):
    return x**3 + 4*x**2 - 10  # Use math.sqrt for single numbers

def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    records = []
    for n in range(1, max_iter + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        records.append([n, a_n, b_n, m_n, f_m_n])  # Append iteration data
        if abs(f_m_n) < tol:
            break
        elif f(a_n) * f_m_n < 0:
            b_n = m_n
        else:
            a_n = m_n
    table = pd.DataFrame(records, columns=['n', 'a_n', 'b_n', 'p_n', 'f(p_n)'])  # Create DataFrame once
    return m_n, table

# Adjust max_iter for desired iterations
results = bisection_method(1, 2, 1e-5, 13)
print(results)
