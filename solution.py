class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Los vectores deben tener la misma longitud para sumarlos.")
        result = [a + b for a, b in zip(self.elements, other.elements)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Los vectores deben tener la misma longitud para restarlos.")
        result = [a - b for a, b in zip(self.elements, other.elements)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Los vectores deben tener la misma longitud para multiplicarlos elemento a elemento.")
        result = [a * b for a, b in zip(self.elements, other.elements)]
        return Vector(result)

    def __matmul__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Los vectores deben tener la misma longitud para realizar el producto punto.")
        result = sum(a * b for a, b in zip(self.elements, other.elements))
        return result

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __eq__(self, other):
        return self.elements == other.elements

# Ejemplo de uso
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Suma de vectores
sum_result = v1 + v2
print("Suma:", sum_result.elements)

# Resta de vectores
sub_result = v1 - v2
print("Resta:", sub_result.elements)

# Producto elemento a elemento
mul_result = v1 * v2
print("Producto:", mul_result.elements)

# Producto punto
dot_result = v1 @ v2
print("Producto Punto:", dot_result)

# Obtener valor en una posición
print("Valor en la posición 1:", v1[1])

# Asignar valor en una posición
v1[1] = 10
print("Nuevo valor en la posición 1:", v1[1])

# Comparar vectores
v3 = Vector([1, 2, 3])
print("¿v1 es igual a v3?", v1 == v3)
