import sympy as sp
import pandas as pd

# Define the symbol and function using sympy
x = sp.symbols('x')
f_ = sp.cos(x) - x

# Lambdify the function for numerical evaluation
f = sp.lambdify(x, f_, 'numpy')

# Secant method implementation
def secant_method_tol(p0, p1, tol, max_iter):
    records = []

    for n in range(max_iter):
        f_p0 = f(p0)
        f_p1 = f(p1)
        p = p1 - f_p1 * (p1 - p0) / (f_p1 - f_p0)  # Secant update formula
        records.append([n, p, abs(p - p1)])

        if abs(p - p1) < tol:  # Check if the result is within the desired tolerance
            break

        p0, p1 = p1, p  # Update guesses for the next iteration

    # Create a DataFrame with the results
    df_results = pd.DataFrame(records, columns=['Iteration', 'p_n', 'Error'])
    return df_results

# Initial guesses and parameters
p_0 = 0.5
epsilon = 1e-4  # A small perturbation to initialize p_1
p_1 = p_0 + epsilon
tolerance = 1e-10
max_iterations = 100

# Perform the Secant method with the specified tolerance and max iterations
results_df = secant_method_tol(p_0, p_1, tolerance, max_iterations)
results_df
