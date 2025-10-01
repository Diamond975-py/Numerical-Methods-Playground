import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Funzione e derivata
def f(x):
    return x**4 - 2*(x**2) - 5*x + 6

def df(x):
    return 4*(x**3) - 4*x - 5

def newton_step(x):
    return x - f(x)/df(x)

# Input utente
x0 = float(input("Inserisci il valore iniziale x0: "))
tol = float(input("Inserisci la tolleranza (es. 1e-6): "))
itmax = int(input("Numero massimo di iterazioni: "))

# Iterazioni metodo di Newton
x_vals = [x0]
for _ in range(itmax):
    x_prev = x_vals[-1]
    x_new = newton_step(x_prev)
    x_vals.append(x_new)
    if abs(x_new - x_prev) < tol:
        break

# Stampa risultati numerici
print("\nIterazioni metodo di Newton:")
for i, val in enumerate(x_vals):
    print(f"x_{i} = {val:.6f}, f(x_{i}) = {f(val):.3e}")
print(f"\nApprossimazione finale: x ≈ {x_vals[-1]:.8f} (in {len(x_vals)-1} iterazioni)")

# Intervallo per il grafico
x_min, x_max = min(x_vals)-1, max(x_vals)+1
x_range = np.linspace(x_min, x_max, 400)
y_range = f(x_range)

# Setup del grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_range, y_range, label='f(x)', color='blue')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title("Metodo di Newton (animato)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Elementi grafici aggiornabili
points, = ax.plot([], [], 'ro')  # punti sull'asse x
v_lines, h_lines, tangents = [], [], []

n_iter = len(x_vals) - 1
for _ in range(n_iter):
    v_line, = ax.plot([], [], color='green')             # verticali
    h_line, = ax.plot([], [], color='red')               # orizzontali
    tangent, = ax.plot([], [], '--', color='gray', alpha=0.6)  # tangenti
    v_lines.append(v_line)
    h_lines.append(h_line)
    tangents.append(tangent)

iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Funzione per aggiornare ogni frame
def update(i):
    if i == 0:
        for vl, hl, tg in zip(v_lines, h_lines, tangents):
            vl.set_data([], [])
            hl.set_data([], [])
            tg.set_data([], [])
        points.set_data([], [])
        iter_text.set_text('')
        return [points, iter_text] + v_lines + h_lines + tangents

    x0 = x_vals[i-1]
    x1 = x_vals[i]
    y0 = f(x0)
    slope = df(x0)

    # Linea verticale dal punto (x0,0) a (x0,f(x0))
    v_lines[i-1].set_data([x0, x0], [0, y0])
    # Linea orizzontale dal punto (x0,f(x0)) fino a (x1,0)
    h_lines[i-1].set_data([x0, x1], [y0, 0])
    # Tangente nel punto (x0,f(x0))
    tangent_line = f(x0) + slope * (x_range - x0)
    tangents[i-1].set_data(x_range, tangent_line)

    # Aggiorna punti calcolati
    points.set_data(x_vals[:i+1], [0]*(i+1))

    iter_text.set_text(f'Iterazione {i}, x_{i}={x1:.6f}')
    return [points, iter_text] + v_lines + h_lines + tangents

# Salva animazione
gif_path = "newton.gif"
ani = animation.FuncAnimation(fig, update, frames=n_iter+1,
                              interval=1000, blit=True, repeat=False)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))

print(f"\nAnimazione salvata in {gif_path}")
