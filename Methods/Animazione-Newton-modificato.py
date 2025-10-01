import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Funzione f(x) e derivata f'(x)
def f(x):
    return x**3 - x - 2

def df(x):
    return 3 * x**2 - 1

# Input utente
x0 = float(input("Inserisci il valore iniziale x0: "))
tol = float(input("Inserisci la tolleranza (es. 1e-6): "))
itmax = int(input("Numero massimo di iterazioni: "))

# Metodo di Newton modificato: derivata fissa calcolata in x0
m = 1 / df(x0)
def phi(x):
    return x - m * f(x)

# Iterazioni
x_vals = [x0]
for _ in range(itmax):
    x_prev = x_vals[-1]
    x_new = phi(x_prev)
    x_vals.append(x_new)
    if abs(x_new - x_prev) < tol:
        break

# Stampa risultati
print("\nIterazioni metodo di Newton modificato:")
for i, val in enumerate(x_vals):
    print(f"x_{i} = {val:.6f}, f(x_{i}) = {f(val):.3e}")
print(f"\nApprossimazione finale: x ≈ {x_vals[-1]:.8f} (in {len(x_vals)-1} iterazioni)")

# Intervallo per il grafico
x_min, x_max = min(x_vals)-1, max(x_vals)+1
x_range = np.linspace(x_min, x_max, 400)
y_range = f(x_range)

# Setup grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_range, y_range, label='f(x)', color='blue')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title("Metodo di Newton Modificato (animato)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Elementi aggiornabili
points, = ax.plot([], [], 'ro')
v_lines, h_lines, slopes = [], [], []

n_iter = len(x_vals) - 1
for _ in range(n_iter):
    v_line, = ax.plot([], [], color='green')
    h_line, = ax.plot([], [], color='red')
    slope_line, = ax.plot([], [], '--', color='gray', alpha=0.6)
    v_lines.append(v_line)
    h_lines.append(h_line)
    slopes.append(slope_line)

iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Funzione aggiornamento animazione
def update(i):
    if i == 0:
        for vl, hl, sl in zip(v_lines, h_lines, slopes):
            vl.set_data([], [])
            hl.set_data([], [])
            sl.set_data([], [])
        points.set_data([], [])
        iter_text.set_text('')
        return [points, iter_text] + v_lines + h_lines + slopes

    x0 = x_vals[i-1]
    x1 = x_vals[i]
    y0 = f(x0)

    # Linea verticale
    v_lines[i-1].set_data([x0, x0], [0, y0])
    # Linea orizzontale
    h_lines[i-1].set_data([x0, x1], [y0, 0])
    # Tangente fissa (pendenza 1/m)
    slope_line = y0 + (x_range - x0) * (1/m)
    slopes[i-1].set_data(x_range, slope_line)

    # Aggiorna punti trovati
    points.set_data(x_vals[:i+1], [0]*(i+1))

    iter_text.set_text(f'Iterazione {i}, x_{i}={x1:.6f}')
    return [points, iter_text] + v_lines + h_lines + slopes

# Salvataggio animazione
gif_path = "newton_modificato.gif"
ani = animation.FuncAnimation(fig, update, frames=n_iter+1,
                              interval=1000, blit=True, repeat=False)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))

print(f"\nAnimazione salvata in {gif_path}")
