import matplotlib.pyplot as plt
import numpy as np
import pulp

''' 2.2.2 '''

# Crear un problema de maximización
prob = pulp.LpProblem("AsignacionDeRecursos", pulp.LpMaximize)

# Definir las variables
x_A = pulp.LpVariable("x_A", lowBound=0, cat="Integer")
x_B = pulp.LpVariable("x_B", lowBound=0, cat="Integer")
x_C = pulp.LpVariable("x_C", lowBound=0, cat="Integer")

# Definir la función objetivo
ganancia_A = 1500 * x_A
ganancia_B = 2500 * x_B
ganancia_C = 4000 * x_C
prob += ganancia_A + ganancia_B + ganancia_C, "GananciaTotal"

# Definir restricciones
prob += 2 * x_A + 3 * x_B + 5 * x_C <= 15, "TiempoDisponible"
prob += x_A + 2 * x_B + 3 * x_C <= 10, "PersonalDisponible"

# Resolver el problema
prob.solve()

# Imprimir resultados
print("Asignación óptima de recursos:")
print("Tarea A:", int(x_A.value()))
print("Tarea B:", int(x_B.value()))
print("Tarea C:", int(x_C.value()))

# Mostrar la ganancia total
print("Ganancia Total:", pulp.value(prob.objective))

''' 2.2.4 '''

# Datos del problema
ganancias = [1500, 2500, 4000]
horas_disponibles = 15
personas_disponibles = 10

# Valor fijo de x_C
x_C_fixed = 20  # Cambia este valor para ver diferentes proyecciones

# Rango de valores para x_A y x_B
x_range = np.arange(0, 7)  # Rango arbitrario

# Restricción de tiempo disponible
tiempo_restriccion = (horas_disponibles - 5 * x_C_fixed - 3 * x_range) / 2

# Restricción de personal disponible
personal_restriccion = (personas_disponibles - 3 * x_C_fixed - x_range) / 2

# Encontrar las combinaciones factibles de (x_A, x_B)
x_A_feasible = []
x_B_feasible = []
for x_A in x_range:
    for x_B in x_range:
        if tiempo_restriccion[x_A] >= 0 and personal_restriccion[x_B] >= 0:
            x_A_feasible.append(x_A)
            x_B_feasible.append(x_B)

# Graficar la región factible proyectada
plt.figure(figsize=(8, 6))
plt.scatter(x_A_feasible, x_B_feasible, color='blue', label='Región Factible')
plt.xlabel('x_A (Recursos asignados a Tarea A)')
plt.ylabel('x_B (Recursos asignados a Tarea B)')
plt.title('Región Factible Proyectada (x_A, x_B) para x_C = {}'.format(x_C_fixed))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
