
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Metodo delle bisezioni
def bisezioni(f, a, b, tol=1e-6, itmax=50):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise Exception("La funzione non cambia segno agli estremi dell'intervallo")

    it = 0
    xs, cs = [], []
    while it < itmax and (b - a) > tol:
        it += 1
        c = (a + b) / 2
        fc = f(c)
        xs.append((a, b, c))  # salvo estremi e punto medio
        cs.append(c)
        if fc == 0:
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return cs, xs, it

# Funzioni di test
def f1(x):
    return x - np.cos(x)

def f2(x):
    return x - np.exp(-x)

# Input utente
choice = int(input("Scegli la funzione: 1) f(x)=x-cos(x), 2) f(x)=x-exp(-x): "))
f = f1 if choice == 1 else f2
a = float(input("Inserisci estremo sinistro a: "))
b = float(input("Inserisci estremo destro b: "))
tol = float(input("Inserisci tolleranza (es. 1e-6): "))
itmax = int(input("Numero massimo di iterazioni: "))

# Calcolo bisezioni
cs, xs, it = bisezioni(f, a, b, tol, itmax)

print("\nIterazioni:")
for i, (a_i, b_i, c_i) in enumerate(xs, 1):
    print(f"Iterazione {i}: a={a_i:.6f}, b={b_i:.6f}, c={c_i:.6f}, f(c)={f(c_i):.3e}")

print(f"\nApprossimazione finale: c ≈ {cs[-1]:.8f} (in {it} iterazioni)")

# Setup grafico
x_range = np.linspace(a, b, 400)
y_vals = f(x_range)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_range, y_vals, label='f(x)', color='blue')
ax.axhline(0, color='black', linestyle='--')
ax.set_title("Metodo delle Bisezioni")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Elementi aggiornabili
v_lines = []
mid_points, = ax.plot([], [], 'ro')  # punti c

for _ in range(len(xs)):
    v_line_left, = ax.plot([], [], 'r')
    v_line_right, = ax.plot([], [], 'r')
    v_lines.append((v_line_left, v_line_right))

iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Funzione di aggiornamento per animazione
def update(i):
    if i == 0:
        for vl, vr in v_lines:
            vl.set_data([], [])
            vr.set_data([], [])
        mid_points.set_data([], [])
        iter_text.set_text('')
        return [mid_points, iter_text] + [vl for vl, vr in v_lines] + [vr for vl, vr in v_lines]

    a_i, b_i, c_i = xs[i-1]

    v_lines[i-1][0].set_data([a_i, a_i], [0, f(a_i)])
    v_lines[i-1][1].set_data([b_i, b_i], [0, f(b_i)])

    cs_partial = [row[2] for row in xs[:i]]
    mid_points.set_data(cs_partial, [f(c) for c in cs_partial])

    iter_text.set_text(f'Iterazione {i}, c={c_i:.6f}')
    return [mid_points, iter_text] + [vl for vl, vr in v_lines] + [vr for vl, vr in v_lines]

# Salva animazione
gif_path = "bisezioni.gif"
ani = animation.FuncAnimation(
    fig, update, frames=len(xs)+1, interval=1000,
    blit=True, repeat=False
)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))

print(f"\nAnimazione salvata in {gif_path}")
