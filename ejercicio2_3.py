from scipy.optimize import linprog

# Coeficientes de la función objetivo (el negativo es porque linprog minimiza, y queremos maximizar)
c = [-200, -300, -500]

# Matriz de coeficientes de las restricciones
A = [
    [2, 1, 3],  # Restricción de materias primas
    [3, 2, 4],  # Restricción de mano de obra
    [4, 3, 6]   # Restricción de tiempo de máquina
]

# Límites de las restricciones
b = [100, 120, 150]

# Restricciones de no-negatividad
x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds]

# Resolviendo el problema
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Imprimiendo los resultados
print("Cantidad óptima de Producto A:", result.x[0])
print("Cantidad óptima de Producto B:", result.x[1])
print("Cantidad óptima de Producto C:", result.x[2])
print("Ganancia máxima:", -result.fun)
