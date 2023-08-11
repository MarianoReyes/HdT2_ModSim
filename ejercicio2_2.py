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
