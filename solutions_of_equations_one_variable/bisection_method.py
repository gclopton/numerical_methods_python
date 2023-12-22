import pandas as pd

f = lambda x: x**3 + 4*x**2 - 10

def bisection_method(a, b, tol, max_iteration):
  if f(a)*f(b) >= 0:
    print("No solution exists on this interval")
    return None

  a_n = a
  b_n = b
  records = []

  for n in range(max_iteration):
    m_n = (a_n + b_n)/2
    f_m_n = f(m_n)
    records.append([n, a_n, b_n, m_n, f_m_n])

    if abs(f_m_n) < tol:
      print("The method has converged to a solution")
      break
    elif f(a_n)*f_m_n < 0:
      b_n = m_n
    else:
      a_n = m_n
  
  table = pd.DataFrame(records, columns=["n", "a_n", "b_n", "m_n", "f_m_n"])
  return table

bisection_method(1, 2, 1e-5, 100)
