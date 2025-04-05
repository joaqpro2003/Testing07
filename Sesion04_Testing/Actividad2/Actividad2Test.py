from Actividad2 import isPrime, isPrime2

def test_primos():
    # Pruebas para isPrime (función original con bug)
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(9) == True  # <- Esta falla con la versión original
    assert isPrime(23) == True

    # Pruebas para isPrime2 (función corregida)
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(9) == False
    assert isPrime2(23) == True

    print("Todas las pruebas de Actividad2 pasaron correctamente.")

if __name__ == "__main__":
    test_primos()
