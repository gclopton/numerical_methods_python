#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

// Define a struct to hold iteration data
struct IterationData {
    int n;
    double a_n, b_n, p_n, f_p_n;
};

// Function f(x)
double f(double x) {
    return x * x * x + 4 * x * x - 10;
}

// Bisection method
std::pair<double, std::vector<IterationData>> bisection(double a, double b, double tol, int max_iter) {
    std::vector<IterationData> iter_data;
    if (f(a) * f(b) >= 0) {
        std::cout << "Bisection method fails." << std::endl;
        return std::make_pair(0.0, iter_data); // Return empty data on failure
    }
    double a_n = a, b_n = b, m_n = 0.0;

    for (int n = 1; n <= max_iter; ++n) {
        m_n = (a_n + b_n) / 2;
        double f_m_n = f(m_n);
        iter_data.push_back({n, a_n, b_n, m_n, f_m_n});

        if (std::abs(f_m_n) < tol) {
            break;
        } else if (f(a_n) * f_m_n < 0) {
            b_n = m_n;
        } else {
            a_n = m_n;
        }
    }
    return std::make_pair(m_n, iter_data);
}

int main() {
    auto [root, data] = bisection(1, 20, 1e-5, 100);
    std::cout << "Root found: " << root << std::endl;
    std::cout << std::fixed << std::setprecision(6);

    // Print iteration data
    for (const auto& it : data) {
        std::cout << "n: " << it.n
                  << " a_n: " << it.a_n
                  << " b_n: " << it.b_n
                  << " p_n: " << it.p_n
                  << " f(p_n): " << it.f_p_n << std::endl;
    }

    return 0;
}
