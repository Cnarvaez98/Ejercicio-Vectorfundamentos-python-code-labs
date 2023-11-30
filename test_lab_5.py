from solution import Vector


def test_vector_suma():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 + v2
    assert resultado == Vector([5, 7, 9])

def test_vector_resta():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 - v2
    assert resultado == Vector([-3, -3, -3])

def test_vector_producto_elemento_a_elemento():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 * v2
    assert resultado == Vector([4, 10, 18])

def test_vector_producto_punto():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 @ v2
    assert resultado == 32
