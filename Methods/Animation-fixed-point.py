import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Funzione iterativa φ(x)
def phi(x):
    return np.cos(x)

# Parametri scelti dall'utente
x0 = float(input("Inserisci il punto iniziale x0: "))
tol = float(input("Inserisci la tolleranza (es. 1e-6): "))
n_iter = int(input("Numero massimo di iterazioni: "))

# Iterazioni della successione x_{n+1} = φ(x_n)
x_vals = [x0]
for _ in range(n_iter):
    x_new = phi(x_vals[-1])
    x_vals.append(x_new)
    if abs(x_new - x_vals[-2]) < tol:
        break

print("\nIterazioni calcolate:")
for i, val in enumerate(x_vals):
    print(f"x_{i} = {val:.8f}")

# Intervallo per il grafico
x_range = np.linspace(0, 2, 400)
y_phi = phi(x_range)
identity = x_range  # y = x

# Setup grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_range, y_phi, label='φ(x) = cos(x)', color='blue')
ax.plot(x_range, identity, label='y = x', color='black', linestyle='--')
ax.set_title("Metodo del Punto Fisso (iterazioni)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()

# Elementi aggiornabili
curve_points, = ax.plot([], [], 'ro')  # Punti sulla curva φ(x)
v_lines = []
h_lines = []

for _ in range(len(x_vals)):
    v_line, = ax.plot([], [], 'r')
    h_line, = ax.plot([], [], 'r')
    v_lines.append(v_line)
    h_lines.append(h_line)

iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Funzione di aggiornamento per animazione
def update(i):
    if i == 0:
        for vl, hl in zip(v_lines, h_lines):
            vl.set_data([], [])
            hl.set_data([], [])
        curve_points.set_data([], [])
        iter_text.set_text('')
        return [curve_points, iter_text] + v_lines + h_lines

    x0 = x_vals[i-1]
    x1 = x_vals[i]
    y0 = phi(x0)

    v_lines[i-1].set_data([x0, x0], [x0, y0])  # verticale
    h_lines[i-1].set_data([x0, x1], [y0, y0])  # orizzontale

    xs = x_vals[:i]
    ys = [phi(x) for x in xs]
    curve_points.set_data(xs, ys)

    iter_text.set_text(f'Iterazione {i}, x_{i}={x1:.6f}')
    return [curve_points, iter_text] + v_lines + h_lines

# Salva animazione
gif_path = "punto_fisso.gif"
ani = animation.FuncAnimation(fig, update, frames=len(x_vals), interval=1000, blit=True, repeat=False)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))

print(f"\nAnimazione salvata in {gif_path}")
