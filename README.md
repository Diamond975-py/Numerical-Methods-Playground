# Numerical Methods Animations

This project contains a collection of Python scripts that visually demonstrate several **root-finding algorithms**.  
The goal is to provide both an **educational overview** and **animated intuition** for how iterative methods converge (or fail to converge) when solving nonlinear equations.

## Implemented Methods

### 1. Continuous Bisections
The **bisection method** is one of the simplest and most reliable techniques for finding a root of a continuous function.  
It works by repeatedly halving an interval `[a, b]` that contains a root, selecting the subinterval where the sign of the function changes.  
- **Pros**: Always convergent (if conditions are met).  
- **Cons**: Converges slowly (linearly).  

---

### 2. Fixed-Point Iteration
The **fixed-point method** is based on rewriting the equation `f(x) = 0` as `x = g(x)` and iterating `x_{n+1} = g(x_n)`.  
Convergence depends on properties of `g` (specifically `|g'(x)| < 1` near the solution).  
- **Pros**: Simple and general.  
- **Cons**: Convergence is not always guaranteed and can be slow.  

---

### 3. Method of Constant Directions
This method generalizes iterative updates by moving in a **fixed direction** in each step.  
It is often used in optimization but can also be applied to root-finding problems, where each step tries to improve the approximation in a constant direction until convergence.  
- **Pros**: Conceptually simple.  
- **Cons**: Efficiency strongly depends on the choice of direction.  

---

### 4. Newton’s Method
Newton’s method is a classical and powerful root-finding technique.  
It updates approximations according to:  

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

- **Pros**: Very fast (quadratic convergence near the solution).  
- **Cons**: Requires the derivative, and convergence is not guaranteed if the initial guess is poor.  

---

### 5. Modified Newton’s Method
This is a variation of Newton’s method where the derivative is not recalculated at each iteration, but kept fixed from the initial guess:  

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_0)}
\]

- **Pros**: Reduces computational cost when evaluating derivatives is expensive.  
- **Cons**: Convergence speed is lower than standard Newton’s method (typically linear).  

---

### 6. Secant Method
The secant method avoids computing derivatives by approximating them with finite differences:  

\[
x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}
\]

- **Pros**: Faster than bisection and does not require derivatives.  
- **Cons**: Convergence is slower than Newton’s method (superlinear, but not quadratic).  

---

## Project Overview

Each Python script in this repository provides a **visual demonstration** of one or more of these methods.  
Animations are generated using **Matplotlib** to illustrate how the sequence of approximations evolves over iterations.  
This helps build intuition about:
- Convergence speed  
- Sensitivity to the initial guess  
- Differences between methods  

---

## Requirements

To run the scripts, you need:
- Python 3.8+  
- [NumPy](https://numpy.org/)  
- [Matplotlib](https://matplotlib.org/)  

Install dependencies with:
```bash
pip install numpy matplotlib
