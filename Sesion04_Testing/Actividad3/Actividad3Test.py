from Actividad3 import stats

def test_stats():
    # Caso 1: lista con número impar de elementos
    lst1 = [3, 1, 2]
    stats(lst1)

    # Caso 2: lista con número par de elementos
    lst2 = [4, 2, 5, 2]
    stats(lst2)

    # Caso 3: lista con una moda clara
    lst3 = [7, 7, 3, 5, 7, 3]
    stats(lst3)

    print("✅ Pruebas de Actividad3 ejecutadas correctamente.")

if __name__ == "__main__":
    test_stats()
