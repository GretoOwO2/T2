import random
import math

def generate_matrix(n):
    return [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

def farthest_coordinate(coords):
    filtered = [c for c in coords if c[0] > 0 and c[1] < 0]
    if not filtered:
        return None, 0.0
    def distance(c):
        return math.hypot(c[0], c[1])
    def dc(arr, left, right):
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        left_best = dc(arr, left, mid)
        right_best = dc(arr, mid + 1, right)
        return left_best if distance(left_best) >= distance(right_best) else right_best
    best = dc(filtered, 0, len(filtered) - 1)
    return best, distance(best)

def main():
    n = int(input("Ingrese la cantidad de pares de coordenadas: "))
    coords = generate_matrix(n)
    print("Lista de coordenadas generadas:")
    for pair in coords:
        print(pair)
    best_coord, best_dist = farthest_coordinate(coords)
    if best_coord:
        print(f"\nCoordenada más alejada con X>0 e Y<0: {best_coord} (distancia = {best_dist:.2f})")
    else:
        print("\nNo se encontró ninguna coordenada con X>0 e Y<0.")

if __name__ == "__main__":
    main()
