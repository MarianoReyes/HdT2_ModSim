import matplotlib.pyplot as plt
import numpy as np
import pulp

''' 2.1.2 '''

# Crear el problema de maximización
prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Definir las variables de decisión: x = cantidad de productos A, y = cantidad de productos B
x = pulp.LpVariable("x", lowBound=0, cat='Integer')
y = pulp.LpVariable("y", lowBound=0, cat='Integer')

# Definir la función objetivo: Z = 10x + 15y (ganancia total)
prob += 10*x + 15*y, "Ganancia_Total"

# Agregar las restricciones
prob += 2*x + 4*y <= 100, "Horas_de_Mano_de_Obra"
prob += 3*x + 2*y <= 120, "Unidades_de_Materia_Prima"

# Resolver el problema
prob.solve()

# Imprimir los resultados
print("Cantidad de productos A a producir:", x.value())
print("Cantidad de productos B a producir:", y.value())
print("Ganancia total maximizada: $", pulp.value(prob.objective))


''' 2.1.4 '''


# Definir las restricciones

def restriccion_mano_de_obra(x):
    return (100 - 2*x) / 4


def restriccion_materia_prima(x):
    return (120 - 3*x) / 2


# Rango de valores de x para graficar
x = np.linspace(0, 50, 100)

# Restricciones
y1 = restriccion_mano_de_obra(x)
y2 = restriccion_materia_prima(x)

# Graficar las restricciones
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2x + 4y ≤ 100")
plt.plot(x, y2, label="3x + 2y ≤ 120")

# Agregar la restricción de no-negatividad
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Área factible
plt.fill_between(x, np.minimum(y1, y2), where=(y1 >= 0) & (
    y2 >= 0), alpha=0.3, color='gray', label="Área factible")

# Punto óptimo
plt.plot(34, 8, 'ro', label="Punto óptimo (34, 8)")

# Etiquetas y leyenda
plt.xlabel("Cantidad de productos A")
plt.ylabel("Cantidad de productos B")
plt.title("Área factible y punto óptimo")
plt.legend()
plt.grid(True)
plt.xlim(0, 50)
plt.ylim(0, 50)

# Mostrar la gráfica
plt.show()
