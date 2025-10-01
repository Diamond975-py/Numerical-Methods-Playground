
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Funzione di test
def f(x):
    return x**3 - x - 2

# Input utente
x0 = float(input("Inserisci il primo valore iniziale x0 (es. 1): "))
x1 = float(input("Inserisci il secondo valore iniziale x1 (es. 2): "))
tol = float(input("Inserisci la tolleranza (es. 1e-6): "))
itmax = int(input("Numero massimo di iterazioni (es. 50): "))

# Metodo delle secanti
x_vals = [x0, x1]
for _ in range(2, itmax+2):
    x_prev, x_curr = x_vals[-2], x_vals[-1]
    if f(x_curr) == f(x_prev):  # evita divisione per zero
        print("Divisione per zero: secante orizzontale.")
        break
    x_new = x_curr - f(x_curr) * (x_curr - x_prev) / (f(x_curr) - f(x_prev))
    x_vals.append(x_new)
    if abs(x_new - x_curr) < tol:
        break

# Stampa risultati
print("\nIterazioni metodo delle secanti:")
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
ax.set_title("Metodo delle Secanti (animato)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Elementi aggiornabili
points, = ax.plot([], [], 'ro')  # punti sull'asse x
sec_lines = []  # secanti

n_iter = len(x_vals) - 1
for _ in range(n_iter-1):
    sec_line, = ax.plot([], [], '--', color='gray', alpha=0.6)
    sec_lines.append(sec_line)

iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Funzione aggiornamento animazione
def update(i):
    if i == 0:
        for sl in sec_lines:
            sl.set_data([], [])
        points.set_data([], [])
        iter_text.set_text('')
        return [points, iter_text] + sec_lines

    if i > 1:
        x_prev, x_curr = x_vals[i-2], x_vals[i-1]
        y_prev, y_curr = f(x_prev), f(x_curr)

        # retta secante tra (x_{n-1}, f(x_{n-1})) e (x_n, f(x_n))
        sec_slope = (y_curr - y_prev) / (x_curr - x_prev)
        sec_line = y_curr + sec_slope * (x_range - x_curr)
        sec_lines[i-2].set_data(x_range, sec_line)

    points.set_data(x_vals[:i+1], [0]*(i+1))
    iter_text.set_text(f'Iterazione {i}, x_{i}={x_vals[i]:.6f}')

    return [points, iter_text] + sec_lines

# Salvataggio animazione
gif_path = "secanti.gif"
ani = animation.FuncAnimation(fig, update, frames=n_iter+1,
                              interval=1000, blit=True, repeat=False)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))

print(f"\nAnimazione salvata in {gif_path}")
